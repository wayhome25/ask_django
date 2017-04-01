# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at' ]
    list_display_links = ['id', 'title']
    actions = ['make_published', 'make_draft']

    # 글자수 컬럼 추가
    def content_size(self, post):
        return mark_safe('<u>{}</u>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    # admin action 추가
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #queryset.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count)) #django message framework 활용
    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') #queryset.update
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count)) #django message framework 활용
    make_draft.short_description = '지정 포스팅을 draft 상태로 변경'



    # list_display_links = ['id', 'title']
    # list_editable = ['author']
    # list_per_page = 3
    # list_filter = ['author', 'created_at']

#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#   list_display = ['id','title', 'content_size', 'status', 'created_at', 'updated_at']
#   actions = ['make_published', 'make_draft']
#   def content_size(self, post):
#       return mark_safe('<u>{}</u>글자'.format(len(post.content)))
#   content_size.short_description = '글자수'
#
#   def make_published(self, request, queryset):
#       updated_count = queryset.update(status='p')
#       self.message_user(request, '{}건의 포스팅을 published 상태로 변경'.format(updated_count))
#   make_published.short_description = '지정 포스팅을 Published 상태로 변경합니다'
#
#   def make_draft(self, request, queryset):
#       updated_count = queryset.update(status='d')
#       self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count))
#   make_draft.short_description = '지정 포스팅을 draft 상태로 변경합니다'
#
# # admin.site.register(Post, PostAdmin)
