import os
import time
from flask import Flask

app = Flask(__name__)

def safe_cast(val, to_type, default=107107):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

@app.route('/')
def sleeper():
    time.sleep(0.1)
    return "Slept well"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
