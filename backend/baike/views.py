import json
import csv
from django.shortcuts import render
from django.http import JsonResponse
# from .models import Baike
import pandas as pd


# Create your views here.

# 获取url携带参数
def information(request):
    disease = request.POST.get("disease")
    return disease


# 返回百科数据
def baike(request):
    # 获取url后缀的信息
    disease = request.GET.get("disease")
    # 若值为空，返回医疗百科分类页面
    if not disease:
        data_all = disease_all()
        return JsonResponse({'result': 1, 'data': data_all}, json_dumps_params={"ensure_ascii": False})
        # return JsonResponse({'result': 1, 'data': 'aaaaaa'}, json_dumps_params={"ensure_ascii": False})
    # 若有值，返回此疾病详情
    elif disease:
        data_one = disease_one(disease)
        return JsonResponse({'result': 1, 'data': data_one}, json_dumps_params={"ensure_ascii": False})
    # 无效请求
    else:
        return JsonResponse({'result': 0, 'data': '无效请求'}, json_dumps_params={"ensure_ascii": False})


# 返回医疗百科分类页面
# 获取csv文件内所有分类信息以及相应疾病信息
def disease_all():
    # 创建新数组以字典格式接受读取内容
    disease_data = []
    # 打开文件
    # with open(".\static\\classify.csv", 'r', encoding='gb18030', errors='ignore') as csvfile:
    with open(".\static\\test.csv", 'r', encoding='gb18030', errors='ignore') as csvfile:
        # 以字典格式读取
        reader = csv.DictReader(csvfile)
        # reader.replace('\0', '')
        # 逐行存入
        for row in reader:
            disease_data.append(dict(row))

        # print(json.dumps(disease_data, sort_keys=True, indent=2, ensure_ascii=False))

    # print(disease_data)
    # print(type(disease_data))
    # name = []
    # department = []
    # for index, row in disease_data.iterrows():
    #     name.append(row[0])
    #     department.append(row[1])
    # disease_data = disease_data.to_json()
    # print(department)
    # print(type(disease_data), type(name), type(department))
    # for index, row in disease_data.iterrows():
    #     res = []
    #     for i in disease_data:
    #         res.append(row[i])
    #         ls.append(res)
    #
    # for i in range(len(ls)):
    #     try:
    #         XXX.objects.create(title=ls[i][0], rating=ls[i][1])
    #     except Exception as e:
    #         print(e)
    # return HttpResponse('数据存储成功')
    # return disease_data
    return disease_data


# 返回疾病详情页面
# 获取csv文件内此疾病信息
def disease_one(disease):
    # 大部分代码逻辑同上
    disease_data = []
    with open(".\static\\disease.csv", 'r', encoding='gb18030', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 判断，选取出此疾病相关数据行
            if row['disease'] == disease:
                disease_data.append(dict(row))
                return disease_data
