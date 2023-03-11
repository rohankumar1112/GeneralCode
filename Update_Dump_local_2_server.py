import pymongo

local_client =pymongo.MongoClient()
local_db =local_client['Tesing']   # Add your local database 
local_collection =local_db['tesing']  #Add your local collection

server_client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
server_db =server_client['darkweb-UrgentData']
server_collection =server_db['mainData1']

print("Currently your local data yet to dump is: ", local_collection.count_documents({}))
print("Total dumped data on server Mongo have right now is : ",server_collection.count_documents({}))



server_data =server_collection.find({})
local_data =local_collection.find({})


local_data = local_collection.find({})
serer_data = server_collection.find({})

for local_doc in local_data :

    l_url = local_doc['url']
    if server_collection.find_one({'url': f'{l_url}'}):
        print("Data already exist!!")
    else :
        server_collection.insert_one(local_doc)     
        
for i in local_data:
    server_collection.insert_one(i)
    print("Data Inserted!!")           
            
            
print("Now total dumped data on server Mongo have right now is :", server_collection.count_documents({}))            
print("Done!!")  
              