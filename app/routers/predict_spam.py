from fastapi import APIRouter, Request, HTTPException
from app.services.spam_service import predict_spam
from app.models.predict_schema import ReviewRequest , ReviewResponse
router = APIRouter()

@router.post('/predict/review_spam', response_model=ReviewResponse)
def predict_spam_review(request: ReviewRequest):
    try:
        return predict_spam(request.review)
    except Exception as e:
        raise HTTPException(status_code=500 , detail=str(e))
