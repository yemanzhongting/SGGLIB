from django.db import models
from mongoengine import *
connect('wbsite',host='127.0.0.1',port=27017)#声明了或许数据库展示静态
# Create your models here.
#如何引用 post与mysql
#属于document类，什么样的key
#pymongo操作比较底层，ORM,django中利用Mongoengine以对象的方式来进行操作。
class ArtiInfo(Document):

    des=StringField()#属性的定义
    title=StringField()
    scores=StringField()
    tags=ListField(StringField())

    #不同的sheet
    meta={
        'collection':'arti_info'
    }
class ItemInfo(Document):
    title = StringField()
    url = StringField()
    pub_date = StringField()
    area = ListField(StringField())
    cates = ListField(StringField())
    look = StringField()
    time = StringField()
    price = IntField()
    meta = {'collection':'item_infoS'}

for i in ArtiInfo.objects:
    print(i.title,i.des)#find函数来进行操作