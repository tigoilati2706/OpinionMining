import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy

# Admin - User
def Insert_Users(dateOfBirth,address,userName,password,email,gender):
    query = "INSERT INTO Users ('dateOfBirth','address','userName','password','email',gender) VALUES ('{}','{}','{}','{}','{}','{}')".format(dateOfBirth,address,userName,password,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Insert_Users(dateOfBirth,address,userName,password,email,gender):
    query = "INSERT INTO Users ('dateOfBirth','address','userName','password','email',gender) VALUES ('{}','{}','{}','{}','{}','{}')".format(dateOfBirth,address,userName,password,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg



def Update_User(idUser,dateOfBirth,address,userName,password,email,gender,phoneNumber):
    query = "UPDATE Users SET dateOfBirth='{}', address='{}', userName='{}', password='{}',email='{}',gender={},phoneNumber={} WHERE idUser={}".format(idUser,dateOfBirth,address,userName,password,email,gender,phoneNumber)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_User(idUser):
    query = "DELETE FROM Users WHERE idUser={}".format(idUser)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def User_Login(email, password):
    query = "SELECT * FROM Users WHERE email = '{}' AND password = '{}'".format(email, password)
    
    try:
        record = Provider.ExecuteQuery(query)

        if len(record) > 0:
            return True
        
        return False
    except:
        return False

def GetAllUser():
    query = "SELECT * FROM Users"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None  


def GetUserById(idUser):
    query = "SELECT * FROM Users WHERE idUser={}".format(idUser)

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None  



# Test
# Insert_Users('01-08-2000','dsa','dsa','dsa','dsa','dssa',1)
# Update_User('01-08-2000','dsa','dsa','dsa','dsa','dssa',1,1)
# Delete_User(1)
# User_Login("dnsa",'sdsa123')