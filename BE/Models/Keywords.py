import Models.Provider as Provider
from flask_sqlalchemy import SQLAlchemy
import json


#Insert Keywords
def Insert_Keywords(category,content,score):
    query = "INSERT INTO Keywords ('category','content',score) VALUES ('{}','{}',{}) ".format(category,content,score)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Keywords(category,content,score,idKeyword):
    query = "UPDATE Keywords SET category ='{}', content='{}', score={} WHERE idKeyword={}".format(category,content,score,idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Keywords(idKeyword):
    query = "DELETE FROM Keywords WHERE idKeyword={}".format(idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg


def GetKeyword():
    query = "SELECT * FROM Keywords"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None







# def data_entry(content,score):
#     query = "INSERT INTO Keywords ('content','score') VALUES ('{}',{})",format(content,score)
#     msg = Provider.ExecuteNonQuery(query)
#     return msg


# def Get_Sentiment(content,score):
#     query = "SELECT * FROM Users WHERE content = '{}' AND score = {}".format(content,score)
    
#     try:
#         record = Provider.ExecuteQuery(query)

#         if len(record) > 0:
#             return True
        
#         return False
#     except:
#         return False
    
# Insert Sentiment List to Keyword Table

# def Insert_Sentiment_List(content,score):

#     with open('labels.json') as file:
#         sentiment_dict = json.load(file)
#     # print(sentiment_dict)

#     for record in sentiment_dict:
#         query = ('INSERT INTO Keywords (content,score) VALUES (?,?)', (record['content'], record['score'])).format(content,score)
#         msg = Provider.ExecuteNonQuery(query)
#         return msg



#Test
# Insert_Keywords('Positive','Good',1)
# Update_Keywords('Nev','Goo',-1,1)
# Delete_Keywords(1)
# Insert_Sentiment_List('zxc',-1)

#
# def SentimentAnalysisProcess(self,tweet,positivelist,negativelist):
#     ps = PorterStemmer()
#     # PorterStemmer using for look up words have 1 root word
#     # For example : Root Word : Like include Likes Liking Liked Likely
#
#     tweet = word_tokenize(tweet)
#     tweet_list = []
#     score = 0
#
#     for word in tweet:
#         word = ps.stem(word)
#         if word in positivelist:
#             score += score
#
#         elif word in negativelist:
#             score -= score
#
#         else:
#             pass
#     return score
#
# def checkRank(self,score,rank):
#     query = "SELECT ranked FROM Comments"
#     rank = Provider.ExecuteQuery(query)
#     if (score > 0):
#         rank = "Good"
#     elif (score == 0):
#         rank = "Neutral"
#     else:
#         rank = "Bad"
#     return rank
#
#
#
#
#
#




