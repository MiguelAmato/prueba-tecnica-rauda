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
	"""_summary_

	Args:
		agent (Agent): _description_
		ticket (str): _description_
		reply (str): _description_

	Returns:
		dict: _description_
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
    df = pd.read_csv(os.path.join(RAW_PATH, CSV_FILE))
    
    df["content_score"] = None
    df["content_explanation"] = None
    df["format_score"] = None
    df["format_explanation"] = None
    
    agent = Agent()
    
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
        
    
    processed_file_path = os.path.join(PROCESSED_PATH, CSV_EVALUATED_FILE)
    df.to_csv(processed_file_path, index=False)
    return

if __name__ == "__main__":
    main()