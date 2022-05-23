import sqlite3 as sql


# function to execute query and return result
def ExecuteQuery(query):
    try:
        #open connection
        connection = sql.connect('project.db')

        # create a cursor object to execute all queries
        cur = connection.cursor()

        # execute query
        cur.execute(query)
        return cur.fetchall()
    except:
        print(" Error : Can not execute to database !!!")
        return -1
    finally:
        #close connection
        connection.close()

# This using for insert update
def ExecuteNonQuery(query):
    try:
        connection = sql.connect("project.db")

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











