from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

app = FastAPI()

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Create SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

class SentimentRequest(BaseModel):
    text: str

@app.post("/analyze_sentiment/")
async def analyze_sentiment(data: SentimentRequest):
    try:
        text = data.text
        scores = sid.polarity_scores(text)
        
        if scores['compound'] >= 0.05:
            sentiment = 'Positive'
        elif scores['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        response_data = {
            "sentiment": sentiment,
            "scores": scores
        }

        return JSONResponse(content=response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
