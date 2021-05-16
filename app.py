from flask import Flask
from flask import request
from flask import jsonify

import preprocessing
import model

app = Flask(__name__)

app.id_count = 1
app.users = {}

app.problem = {}

@app.route('/')
def user_juso():
    temp = request.args.get('name', "user01")
    temp1 = request.args.get('juso', "df")

    return temp + "-" + temp1

@app.route("/post_test", methods=['POST'])
def post_test():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count = app.id_count + 1

    return jsonify(new_user)

@app.route("/get_problem", methods=['POST'])
def get_problem():
    new_problem = request.json
    new_problem["id"] = app.id_count
    app.problem[app.id_count] = new_problem
    app.id_count = app.id_count + 1
    return jsonify(new_problem)




if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
