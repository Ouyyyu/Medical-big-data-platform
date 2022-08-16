from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def information(request):
    disease = request.GET.get("disease")
    return disease


def baike(request):
    disease = request.GET.get("disease")
    if not disease:
        return JsonResponse({"result": "应返回百科主页面"}, json_dumps_params={"ensure_ascii": False})
    # baike = Baike.objects.filter(disease=disease).first()
    return JsonResponse({"result": "应返回词条"}, json_dumps_params={"ensure_ascii": False})
