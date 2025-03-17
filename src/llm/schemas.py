from pydantic import BaseModel

class FormatSchema(BaseModel):
    """Format schema for the LLM call."""
    
    content_score: int
    content_explanation: str
    format_score: int
    format_explanation: str