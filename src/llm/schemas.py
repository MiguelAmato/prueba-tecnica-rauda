from pydantic import BaseModel


class ContentSchema(BaseModel):
    """Content schema for the LLM call."""

    score: int
    explanation: str


class FormatSchema(BaseModel):
    """Format schema for the LLM call."""

    score: int
    explanation: str
