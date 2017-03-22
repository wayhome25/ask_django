# blog/model.py
import re
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100, help_text='최대 100자 내로 입력가능합니다.'
    # choices = (
    #     ('제목1', '제목 1 레이블'),
    #     ('제목2', '제목 2 레이블'),
    #     ('제목3', '제목 3 레이블'),
    # )
    ) # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')             # 길이 제한이 없는 문자열
    # DB에서는 길이제한 유무에 따라서 문자열 필드타입이 다른다.
    # 길이 제한이 없는 문자열을 많이 쓰면 성능이 좋지 않다.
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators = [lnglat_validator], # 함수를 넘겨서 유효성 검사 실행
        help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장
