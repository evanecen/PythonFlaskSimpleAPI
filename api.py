import flask

app = flask.Flask(__name__)

def readjson(filename):
    with open(filename) as file:
        data = flask.json.load(file)
    return data

@app.route("/api/<name>")
def data(name):
    return flask.jsonify(readjson("data/"+name+".json"))
