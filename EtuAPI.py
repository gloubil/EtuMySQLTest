from flask import Flask, request
from MySQLInstance import MySQLInstance

app = Flask("EtuAPI")

@app.route("/heartbeat")
def heartbeat():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    host = request.args.get("host", "")

    try:
        sql = MySQLInstance(host=host, username=username, password=password)
    except:
        return {"success" : False}
    return {"success" : True}
    


