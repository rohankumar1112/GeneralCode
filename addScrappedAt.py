import  pymongo
import datetime

myclient=pymongo.MongoClient()
db =myclient['ForumScrapping']  #change database 
col =db['allData'] #change collection
print(col.count_documents({}))

time_format ="%Y-%m-%dT%H:%M:%S"
currentDate =datetime.datetime.now().strftime(time_format)
print(currentDate)

date_time = {"$set": {"ScrappedAt":currentDate }}
col.update_many({},date_time)

print("scrappedAt field added!!")

