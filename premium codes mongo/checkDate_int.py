## Test date formate (int type) and dump in another collection

from datetime import datetime, timedelta
import re
import pymongo


client=pymongo.MongoClient('mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority')
db=client['Final_Filtered_Data']
collection=db['cyber_data']
error_col =db['error']

for i in collection.find({}):

  try:
    for j in i['posts']:
      int(j['date'])
  except:
    print(i["_id"])
    if(error_col.find({'_id':('i[_id]')})):
      pass
    else:  
      error_col.insert_one(i)

  try:
    int(i['lastModifiedDate'])  
  except:
    print(i['_id'])
    if(error_col.find({'_id':('i[_id]')})):
      pass
    else:  
      error_col.insert_one(i)

  try:
    int(i['ScrappedAt'])  
  except:
    # print(i['_id'])  
    if(error_col.find({'_id':('i[_id]')})):
      pass
    else:  
      error_col.insert_one(i)



