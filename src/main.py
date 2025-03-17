import os
import pandas as pd

from openai import OpenAIError
from dotenv import load_dotenv
from llm.agent import Agent

load_dotenv()

RAW_PATH = os.getenv("RAW_DATA")
PROCESSED_PATH = os.getenv("PROCESSED_DATA")
CSV_FILE = os.getenv("CSV_FILE")
CSV_EVALUATED_FILE = os.getenv("CSV_EVALUATED_FILE")

ERROR_RESPONSE = { "content_score" : None, "content_explanation" : None, "format_score" : None, "format_explanation" : None }

def safe_llm_call(agent: Agent, ticket: str, reply: str) -> dict:
	"""Safely calls the LLM agent to evaluate a customer support response.

	Args:
		agent (Agent): The LLM agent responsible for evaluating the response.
		ticket (str): The customer support ticket message.
		reply (str): The AI-generated response to be evaluated.

	Returns:
		dict: A dictionary containing the evaluation results from the agent, or `ERROR_RESPONSE` in case of failure.
	"""
	if (ticket is None) or (reply is None):
		return ERROR_RESPONSE
	try:
		response = agent.evaluate_response(ticket=ticket, reply=reply)
		return response
	except OpenAIError as e:
		print(f"")
		return ERROR_RESPONSE

def main():
    # Read the csv file
    df = pd.read_csv(os.path.join(RAW_PATH, CSV_FILE))
    
    # Add the new columns 
    df["content_score"] = None
    df["content_explanation"] = None
    df["format_score"] = None
    df["format_explanation"] = None
    
    # Create the LLM Agent
    agent = Agent()
    
    # Iterate in the df and calls in every row to the llm to fill the new columns
    for ind, row in df.iterrows():
        response = safe_llm_call(
            agent=agent,
            ticket=row["ticket"],
            reply=row["reply"],
            )
        df.loc[ind, ["content_score", "content_explanation", "format_score", "format_explanation"]] = [
			response["content_score"],
			response["content_explanation"],
			response["format_score"],
			response["format_explanation"]
		]
        
    # Save the new df in a csv
    processed_file_path = os.path.join(PROCESSED_PATH, CSV_EVALUATED_FILE)
    df.to_csv(processed_file_path, index=False)
    
    print(f"Evaluated {CSV_FILE} saved in {CSV_EVALUATED_FILE}!")
    return

if __name__ == "__main__":
    main()