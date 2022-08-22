from django.http import JsonResponse
from .models import User
from django.shortcuts import render


# login时读取url携带信息
def information(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    return username, password


# 注册功能
def register(request):
    username = request.POST.get("username")
    sex = request.POST.get("sex")
    password = request.POST.get("password")
    age = request.POST.get("age")
    province = request.POST.get("province")
    user = User.objects.filter(username=username).first()
    if user:
        return JsonResponse({'result': 0, 'message': '此用户名已注册过'}, json_dumps_params={"ensure_ascii": False})

    User.objects.create_user(username=username, sex=sex, password=password,
                             province=province, age=age)
    return JsonResponse({'result': 1, 'message': '注册成功'}, json_dumps_params={"ensure_ascii": False})


# 登录功能
def login(request):
    username, password = information(request)
    user = User.objects.filter(username=username).first()
    # 信息有误，直接返回
    # if not user:
    #     return JsonResponse({'result': 0, 'message': '用户不存在'}, json_dumps_params={"ensure_ascii": False})
    # elif not user.check_password(password):
    #     return JsonResponse({'result': 0, 'message': '密码错误'}, json_dumps_params={"ensure_ascii": False})
    if not user or not user.check_password(password):
        return JsonResponse({'result': 0, 'message': '用户名或密码错误'}, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({"result": 1, "massage": '登陆成功'}, json_dumps_params={"ensure_ascii": False})


def delete(request):
    username, password = information(request)
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        user.delete()
        return JsonResponse({"result": "删除成功"}, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({"result": "用户名或密码错误"}, json_dumps_params={"ensure_ascii": False})
