from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "mahi mashal sarwar"

if __name__ =="__main__":
    app.run()#debug mode my run ho