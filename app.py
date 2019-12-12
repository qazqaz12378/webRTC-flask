from flask import Flask, request, abort,jsonify

app = Flask(__name__)

_dataStore = {}

@app.route('/data/<username>',methods=['GET'])
def GetPos(username):
    if not username is None:
        if _dataStore.get(username) == None:
            return abort(404)
        else:
            if len(_dataStore[username]) > 0:
                return _dataStore[username].pop(0)
            else:
                return abort(404)
    else:
        return abort(404)

@app.route('/data/<username>',methods=['POST'])
def POSTPos(username):
    if not username is None:
        if _dataStore.get(username) == None:
            _dataStore[username] = []
        _dataStore[username].append(request.data)
        return '1'
    else:
        return abort(404)
# @app.route('/data/<username>')
# def Postid(username):
#     return username



if __name__ == '__main__':
    app.run(host='0.0.0.0')