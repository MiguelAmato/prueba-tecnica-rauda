import os

from openai import OpenAI
from dotenv import load_dotenv

from llm.prompts import PROMPT
from llm.schemas import FormatSchema

class Agent:
    """Main class that contains the llm calls to OpenAI API."""
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def call_llm(
        self,
        prompt:str,
        response_format:FormatSchema=None,
        model:str="gpt-4o-mini",
        temperature:float=0.3,
    ) -> str:
        """Calls the OpenAI API .

        Args:
            prompt (str): The column that we want to score.
            response_format (FormatSchema): format schema for the response.
            model (str, optional): Set the model from the OpenAI models availables. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the temperature model. Defaults to 0.3.

        Returns:
            str: Returns the format schema with the new scores and explanations. 
        """
        
        messages=[
            {"role": "system", "content": PROMPT.format(text=prompt)}
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