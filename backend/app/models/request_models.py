from pydantic import BaseModel


class YouTubeRequest(BaseModel):
    url: str


class QueryRequest(BaseModel):
    query: str
