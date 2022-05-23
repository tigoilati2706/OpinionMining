import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy


def Insert_Post(content,dateCreate,idUser):
    query = "INSERT INTO Posts ('content','dateCreate','idUser') VALUES ('{}','{}','{}')".format(content,dateCreate,idUser)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Post(idPost,content):
    query = "UPDATE Posts SET content='{}' WHERE idPost={}".format(content,idPost)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Post(idPost):
    query = "DELETE FROM Posts WHERE idPost={}".format(idPost)
    msg = Provider.ExecuteNonQuery(query)
    return msg


def GetPost():
    query = "SELECT * FROM Posts"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

def GetPostById(idPost):
    query = "SELECT * FROM Posts WHERE idPost={}".format(idPost)

    try : 
        record = Provider.ExecuteQuery(query)
        return record
    except:
        return None  
   

# Test 
# Insert_Post('Good','2010-10-10')
Update_Post(1,'Yeh')
# Delete_Post(1)