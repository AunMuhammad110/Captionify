from flask import Flask
from pydantic import BaseModel
app = Flask(__name__)

@app.route('/getHelloWorld')
def hello_world():
    return 'Hello,!'

if __name__ == '__main__':
    app.run(debug=True)
