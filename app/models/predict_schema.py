
from pydantic import BaseModel

class ReviewRequest(BaseModel):
    review: str

class ReviewResponse(BaseModel):
    is_spam : bool
    confidence: float
