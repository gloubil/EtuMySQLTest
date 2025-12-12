from flask import Flask, request
from MySQLInstance import MySQLInstance
import os

app = Flask("EtuAPI")

@app.route("/heartbeat")
def heartbeat():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    host = request.args.get("host", f"{os.getenv("DB_IP")}")

    try:
        sql = MySQLInstance(host=host, username=username, password=password)
    except:
        return {"success" : False}
    return {"success" : True}
    



