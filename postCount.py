import pymongo

client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")

db =client['darkweb-UrgentData']
col =db['mainData']

count =0
for i in col.find({}):
    for j in i['posts']:
        count+=1
        
print(count)        