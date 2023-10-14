import pickle
from pathlib import Path

__version__ = '0.1.0'

BASE_PATH = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_PATH}/spam_detection_{__version__}.pkl", 'rb') as f:
  model = pickle.load(f)

def is_spam(text):
  if(model.predict([text]) == 1):
    return True
  else:
    return False