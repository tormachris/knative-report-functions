import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def isprime():
  n = os.environ.get('TARGET', '42069')
  if n == 2 or n == 3: return "Prime"
  if n < 2 or n%2 == 0: return "Not Prime"
  if n < 9: return "Prime"
  if n%3 == 0: return "Not Prime"
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return "Not Prime"
    if n%(f+2) == 0: return "Not Prime"
    f +=6
  return "Prime"

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
