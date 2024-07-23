import mysql.connector
import json


def login(name,email, password):
    try:
        with open("info.json", "r") as js:
            data = js.read()
            data = json.loads(data)

        mydb = mysql.connector.connect(
        host= data["server"]["host"],
        user= data["server"]["user"],
        password= data["server"]["password"]
        )
    except:
        print("Can't connect to server")

