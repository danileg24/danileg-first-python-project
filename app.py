from flask import Flask, app

app = Flask(__name__) 

@app.route("/")
def hello_world():
    return 'Hello, DaniLeg'


if __name__ == "__main__":
  print("I'm inside if now")
  app.run(host='0.0.0.0', debug=True)