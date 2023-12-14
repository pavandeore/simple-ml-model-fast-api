install packages

pip install fastapi uvicorn nltk  --break-system-packages


----

to run 

uvicorn main:app --reload


----


make HTTP POST request to http://127.0.0.1:8000/analyze_sentiment/

with body

{
  "text" : "Nice i love it"
}


