import os

from openai import OpenAI
from dotenv import load_dotenv

from llm.prompts import CONTENT_PROMPT, FORMAT_PROMPT
from llm.schemas import ContentSchema, FormatSchema

class Agent:
    """Main class that contains the llm calls to OpenAI API."""
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def call_llm(
        self,
        prompt:str,
        response_format=None,
        model:str="gpt-4o-mini",
        temperature:float=0.3,
    ):
        """Calls the OpenAI API.

        Args:
            prompt (str): The given prompt.
            response_format (FormatSchema): format schema for the response.
            model (str, optional): Set the model from the OpenAI models availables. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the temperature model. Defaults to 0.3.

        Returns:
            Schema: Returns the format schema with the new scores and explanations.
            or
            str: Returns a response from OpenAI API if there is not a response_format
        """
        
        messages=[
            {"role": "system", "content": prompt}
        ]
        
        if response_format:
            response = self.client.beta.chat.completions.parse(
                model=model,
                messages=messages,
                response_format=response_format,
            )
        else:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
        
        return (
            response.choices[0].message.parsed
            if response_format
            else response.choices[0].message.content
        ) 
        
    def evaluate_response(self, ticket:str, reply:str) -> dict:
        """Evaluates an AI-generated customer support response based on content and format.

        This method calls the LLM twice: once to evaluate the **content** of the response (relevance, correctness, completeness) 
        and once to evaluate the **format** (clarity, structure, grammar/spelling). It returns a dictionary containing 
        both evaluation scores and explanations.

        Args:
            ticket (str): The customer support message submitted by the user.
            reply (str): The AI-generated response that needs evaluation.

        Returns:
            dict: A dictionary containing the evaluation results with the following keys:
                - "content_score" (int | None): Score (1-5) for the quality of the response's content.
                - "content_explanation" (str | None): Explanation of the content evaluation.
                - "format_score" (int | None): Score (1-5) for the response's formatting quality.
                - "format_explanation" (str | None): Explanation of the format evaluation.

        If the LLM evaluation fails or does not return a valid response, the corresponding values will be set to `None`.
        """
        
        content_response = self.call_llm(
            prompt=CONTENT_PROMPT.format(ticket=ticket, reply=reply),
            response_format=ContentSchema
        )
        
        format_response = self.call_llm(
            prompt=FORMAT_PROMPT.format(ticket=ticket, reply=reply),
            response_format=FormatSchema
        )
        
        return { 
            "content_score" : content_response.score if content_response.score else None, 
            "content_explanation" : content_response.explanation if content_response.explanation else None, 
            "format_score" : format_response.score if format_response.score else None, 
            "format_explanation" : format_response.explanation if format_response.explanation else None,
        }
        
        
        
