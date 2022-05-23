import json
import sqlite3 as sql

# This using for insert update
def ExecuteNonQuery(query):
    try:
        connection = sql.connect("./project.db")

        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
        msg = "Successfully"
    except Exception as e:
        print(e)
        connection.rollback()
        msg = "Error in Insert or Update Operation"
    finally:
        return msg
        connection.close()

#Insert Keywords
def Insert_Keywords(category,content,score):
    query = "INSERT INTO Keywords ('category','content','score') VALUES ('{}','{}',{}) ".format(category,content,score)
    msg = ExecuteNonQuery(query)
    return msg

name = "labels.json"

# JSON file
f = open (name, "r")
 
# Reading from file
data = json.loads(f.read())

#key: tên keyword; value: score của keyword
#{'abandon': -2} => key: abandon; value: -2
for key, value in data.items():
    try:
        result = Insert_Keywords("Positive" if value >= 0 else "Negative", key, value)            
        print(key + " " + str(value) + " " + result)
    
    except Exception as e:
        print(e)
        print(key + " passed")

        
    
