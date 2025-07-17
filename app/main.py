from fastapi import FastAPI
from app.routers.predict_spam import router as spam_router
app = FastAPI()

app.include_router(spam_router , prefix='/api/v1')
