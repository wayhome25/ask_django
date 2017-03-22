# dojo/views.py
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from mysite import settings

# def mysum(request, x, y=0, z=0):
#     return HttpResponse(int(x) + int(y) + int(z))

def mysum(request, numbers):
    return HttpResponse(sum(map(lambda s: int(s or 0),numbers.split('/'))))


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name,age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
                        <h1> hello, </h1>
                        <p>{name}</p>
                        <p>반가워요</p>
                        '''.format(name=name))


def post_list2(request):
    name = '홍철'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    }, json_dumps_params = {'ensure_ascii': True})

def excel_download(request):
    # filepath = '/Users/Leehyunjoo/GitHub/ask_django/scimagojr-3.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'scimagojr-3.xlsx')
    # 현재 프로젝트 최상위 (부모폴더) 밑에 있는 'scimagojr-3.xlsx' 파일
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
