from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='static')
            

@app.route('/', methods=['GET'])
def getallSongs():
    return "Hello World!!!"

if __name__ == "__main__":
    app.run(debug=True)
