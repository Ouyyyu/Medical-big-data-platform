from .models import *
from django.http import JsonResponse

robot_handler = ChatBotGraph()


def robot(request):
    user_question = request.POST.get("question")
    answer = robot_handler.chat_main(user_question)
    return JsonResponse({'result': 1, 'answer': answer}, json_dumps_params={"ensure_ascii": False})
    # while 1:
    #     question = input('用户:')
    #     answer = handler.chat_main(question)
    #     print('小妤:', answer)
