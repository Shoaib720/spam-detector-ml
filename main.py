from fastapi import FastAPI
from uvicorn import run
from pydantic import BaseModel
from model.spam_detector_util import is_spam

app = FastAPI(
  title='Scam Message Detector API',
  description='Scam Detector Machine Learning Model API',
  version='0.1.0'
)

class TextInput(BaseModel):
  text: str

@app.get('/', status_code=200)
def health_check():
  return {
    'message': 'Service is RUNNING',
    'title': 'Scam Message Detector API',
    'version': 'v0.1.0',
    'developer': 'Shoaib S. Shaikh'
  }

@app.post('/detect', status_code=200)
def detect_spam(payload: TextInput):
  return {
    'message': 'Success',
    'status': 200,
    'input': payload.text,
    'is_spam': is_spam(payload.text)
  }

if __name__ == '__main__':
  run(app, host='0.0.0.0',port=8000)