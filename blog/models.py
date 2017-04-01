# blog/model.py
import re
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    author = models.CharField(max_length=50)
    title = models.CharField(verbose_name='제목이다!' ,max_length=100, help_text='최대 100자 내로 입력가능합니다.')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                                validators = [lnglat_validator],
                                help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장

    def __str__(self):
        return self.title
