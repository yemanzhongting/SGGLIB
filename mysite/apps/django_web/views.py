from apps.django_web.models import ItemInfo
from django.core.paginator import Paginator


#============================================== <<<< DATA GENS >>>> ====================================================

# 不同区域发帖量前三名
def topx(date1,date2,area,limit):

    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':date1,'$lte':date2}},{'area':{'$all':area}}]}},
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
        {'$limit':limit},
        {'$sort':{'counts':-1}}
    ]

    for i in ItemInfo._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'][0],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data

series_CY = [i for i in topx('2015.12.25','2015.12.27',['朝阳'],3)]
series_TZ = [i for i in topx('2015.12.25','2015.12.27',['通州'],3)]
series_HD = [i for i in topx('2015.12.25','2015.12.27',['海淀'],3)]
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 数据中发帖总量柱状图
def total_post():
    pipeline = [
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    ]

    for i in ItemInfo._get_collection().aggregate(pipeline):
        print(i)
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

series_post = [i for i in total_post()]


#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def one_day_deal_cate():
    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':'2015.12.25','$lte':'2016.01.11'}},{'time':1}]}},
        {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]

    for i in ItemInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

def one_day_deal_area():
    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$gte':'2015.12.25','$lte':'2016.01.11'}},{'time':1}]}},
        {'$group':{'_id':{'$slice':['$area',1]},'counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]

    for i in ItemInfo._get_collection().aggregate(pipeline):
        data = {
            'name':i['_id'][0],
            'y':i['counts']
        }
        yield data

pie1_data = [i for i in one_day_deal_cate()]
pie2_data = [i for i in one_day_deal_area()]



#============================================== <<<< PAGE VIEWS >>>> ===================================================

# Create your views here.
def BSweb(request):
    return render(request, 'BSweb.html')
'''def index(request):
    arti_info=ArtiInfo.objects[:1]

    context={
        # 'title':'Just a title',
        # 'des':'Just a description',
        # 'score':'1.0'
        'title': arti_info[0].title,
        'des':arti_info[0].des,
        'score':arti_info[0].scores,
    }
    return render(request,'index.html',context)'''
#context数据库替换,字典，替换具体内容。
#model作为代理取出来数据

def chart(request):
    context = {
        'chart_CY':series_CY,
        'chart_TZ':series_TZ,
        'chart_HD':series_HD,
        'series_post':series_post,
        'pie1_data':pie1_data,
        'pie2_data':pie2_data
    }
    return render(request, 'chart2.html', context)
def index(request):
    limit = 15
    arti_info = ItemInfo.objects
    paginatior = Paginator(arti_info,limit)
    page = request.GET.get('page',1)
    print(request)
    print(request.GET)
    loaded = paginatior.page(page)

    context = {
        'ItemInfo':loaded,
        'counts':arti_info.count(),
        'last_time':arti_info.order_by('-pub_date').limit(1),

    }

    return render(request, 'index_data.html', context)


from django.shortcuts import render
from django.http import HttpResponse


# import os

# Create your views here.
def file(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            # 打开特定的文件进行二进制的写操作
            # print(os.path.exists('/temp_file/'))
            with open("./temp_file/%s" % File.name, 'wb+') as f:
                # 分块写入文件
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("UPload over!")
    else:
        return render(request, "fileupload.html")
