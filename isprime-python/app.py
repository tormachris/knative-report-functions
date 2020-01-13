import os

from flask import Flask

app = Flask(__name__)

def safe_cast(val, to_type, default=107107):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

@app.route('/')
def isprime():
    num = safe_cast(os.environ.get('TARGET', 107107),int)

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return str(i)
        else:
            return "not prime"

    else:
        print(num, "is not a prime number")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
