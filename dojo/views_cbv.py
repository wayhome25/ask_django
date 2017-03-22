from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

# CBV 사용시에 View를 상속받아서 사용하는 일을 거의 없다
class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
                <h1> hello, </h1>
                <p>{name}</p>
                <p>반가워요</p>
                '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()


class PostListView3(View):
    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': True})

    def get_data(self):
        return{
            'message' : '안녕 파이썬 장고',
            'items' : ['파이썬', '장고', 'AWS', 'Azure'],
        }

post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    #TODO : 직접 구성해 보세요
    pass
