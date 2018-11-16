import pymongo

client=pymongo.MongoClient('localhost',27017)
wbsite=client['wbsite']

#第一列
arti_info=wbsite['arti_info']

data = {
             'des':str("zhangyan"),
             'title' :"whu",
             'scores':'5',
             #'tags':list[str("good"),str("happy"),str("sunny")]   #2:"sunny"
         }
arti_info.insert_one(data)