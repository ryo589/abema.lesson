from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<html><body><h1>sample by Abema System　ryo</h1></body></html>'
if __name__ == '__main__':
    app.run()