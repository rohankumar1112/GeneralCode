import pymongo

client = pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
# client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["darkweb-UrgentData"]
collection = db["HackForum"]
dump_db = client["darkweb-UrgentData"]
dump_collection = dump_db["Filter"]
# print(dump_collection.find().count())
keywords = ['7-eleven global, (7 11 Global)', 'AEON ', 'Bank BTPN ', 'AWS ', 'BHP ', 'Bareksa Fintech', 'boat', 'Japan Railway ', 'Chubu Electric Power Co. Inc.', 'Chugai Pharmacuetical Co. Ltd. ', 'Daiwa Securities ', 'Deloitte ', 'Demir BT', 'Deutsche Post DHL', 'Digital Hearts ', 'DITO Telecoms ', 'Electric Power Development Co. Ltd.', 'Electricity ISAC ', 'Ernst & Young ', 'ETEK', 'Expedia ', 'Fincombank ', 'First Citizen Bank', 'FoxNews ', 'FreeDivision s.r.o', 'Globant', 'Goldman Sachs ', 'HDFC Bank ', 'Hoist Finance', 'Hokkaido Electric Power Co. Ltd. ', 'Hon Hai Precision Co. Ltd.', 'Hue Central Hospital', 'IDEX', 'IDFC First Bank ', 'IHI Corporation', 'Indorama', 'ION Management', 'ISUZU Motors Limited ', 'Izena Company', 'Japan Broadcasting Corporation', 'Japan Post ', 'JERA Co. Inc.', 'Jewelex', 'Kerry Group Plc', 'Logitech', 'Masaki Corp.', 'Maxam Corp.', 'Medi Assist ', 'Mega International Commercial Bank', 'Ministerual Afacerilor Interne Moldova ', 'Ministry of Defense Moldova ', 'Mitsubishi', 'Mitsubishi Corporation ', 'Mitsubishi Motors Corporation ', 'Moldindconbank', 'Moneta Money Bank','Morgan Stanley & Co. LLC ', 'MPTC', 'National Hospital of Obstetrics and Gynecology (NHOG)', 'NEC Corporation ', 'NForce Secure', 'NGK Spark Plug', 'Neiderrhein Energie and Wasser GmbH', 'Nikkentes', 'Nippon Care Supply Co. Ltd. ', 'NTT Communications ', 'NTT Data ', 'Odakyu Electric Railway Co. Ltd.', 'Orica Global ', 'Panasonic Holdings Corporation', 'Pepperfry ', 'Philippine Airlines ', 'RICOH Company', 'Seibu Holdings ', 'SHIFT Inc. ', 'Shin Kong Bank Co. Ltd.', 'Snowflake', 'Source Code Control Ltd. ', 'Subaru Corporation ', 'Sumitomo Rubber ', 'Suntory Holdings Limited ', 'SuperChoice', 'Tateno Corporation ', 'The Bank of Yokohama ', 'The Kansai Electric Power Company inc. ', 'Thai Nguyen Nartional Hospital', 'Thong Nhat Hospital', 'Tokyo Gas Co. Ltd. ', 'Toppan Printing ', 'Toshiba Corporation ', 'Transcosmos ', 'Travelers', 'TVS Motors', 'Vietnam International Commercial Joint Stock Bank (VIB)', 'Vietnam Ministry of Health', 'Vietnam', 'Vietnam National Childrens Hospital', 'Vin Tech', 'Xeon Motors', 'XONTECH Systems', 'Zscaler Global', 'Zuellig Pharma']

for keyword in keywords:
    query = {
        "$or": [
            {"title": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"link": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"posts": {"$elemMatch": {"$regex": f".*{keyword}.*", "$options": "i"}}}
        ]
    }
    results = collection.find(query)
    for result in results:
        if dump_collection.find_one({"_id": result["_id"]}):
            print("Document already exists: ", keyword, result["_id"])
        else:
            dump_collection.insert_one(result)
            print(keyword, result["_id"])
# print(dump_collection.find().count())