import pymongo
client=pymongo.MongoClient('localhost',27017)
walden=client['walden']
#sheet_line=walden['sheet_line']
sheet_tab = walden['sheet_tab']
# path='walden.txt'
# with open(path ,'r') as f:
#     lines=f.readlines()
#     for index, line in enumerate(lines):
#          data = {
#              'index':index,
#              'line' :line,
#              'words':len(line.split())
#          }
#     sheet_tab.insert_one(data)
# #
for item in sheet_tab.find():
    print(item)
        #sheet_tab.insert_one(data)