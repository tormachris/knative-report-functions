import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def isprime():
    num = os.environ.get('TARGET', '107107')
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "not prime"
        else:
            return "not prime"

    else:
        print(num, "is not a prime number")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
