import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy


def Insert_Image(idPost,path):
    query = "INSERT INTO Images (idPost,'path') VALUES ('{}','{}')".format(idPost,path)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Image(path,idImage):
    query = "UPDATE Images SET path='{}' WHERE idImage={}".format(path,idImage)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Image(idImage):
    query = "DELETE FROM Images WHERE idImage={}".format(idImage)
    msg = Provider.ExecuteNonQuery(query)
    return msg


def Get_Image():
    query = "SELECT * FROM Images"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

# Test 
# Insert_Image(1,'dsadsaweqwsad')
Update_Image('sdas',1)
# Delete_Image(1)
# Get_Comment()








