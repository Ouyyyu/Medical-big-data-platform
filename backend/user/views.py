from django.http import JsonResponse
from .models import User


def information(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    return username,password


def register(request):
    username=request.GET.get("username")
    sex=request.GET.get("sex")
    password=request.GET.get("password")
    province=request.GET.get("province")
    old=request.GET.get("old")
    user = User.objects.filter(username=username).first()
    if user:
        return JsonResponse({"result": "用户已存在"},json_dumps_params={"ensure_ascii":False})

    User.objects.create_user(username=username,sex=sex,password=password,
                             province=province,old=old)
    return JsonResponse({"result": "注册成功"},json_dumps_params={"ensure_ascii":False})


def login(request):
    username,password = information(request)
    user=User.objects.filter(username=username).first()
    if not user:
        return JsonResponse({"result": "用户不存在"},json_dumps_params={"ensure_ascii":False})
    if not user.check_password(password):
        return JsonResponse({"result": "密码错误"},json_dumps_params={"ensure_ascii":False})
    return JsonResponse({"result":"登录成功","username":username},json_dumps_params={"ensure_ascii":False})


def delete(request):
    username,password=information(request)
    user=User.objects.filter(username=username).first()
    if user and user.check_password(password):
        user.delete()
        return JsonResponse({"result":"删除成功"},json_dumps_params={"ensure_ascii":False})
    return JsonResponse({"result":"用户名或密码错误"},json_dumps_params={"ensure_ascii":False})
