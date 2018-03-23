from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(BaseModel, AbstractUser):
    class Meta:
        db_table = 'df_user'


class AreaInfo(models.Model):
    # title charField字符串
    title = models.CharField(max_length=20)
    # 父集 自关联
    aParent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'df_area'


class Address(BaseModel):
    receiver = models.CharField(max_length=10)
    province = models.ForeignKey(AreaInfo, related_name='province')
    city = models.ForeignKey(AreaInfo, related_name='city')
    district = models.ForeignKey(AreaInfo, related_name='district')
    address = models.CharField(max_length=100)
    # 6位邮编号
    Postal_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
    # 是否默认,默认不默认
    isDefault = models.BooleanField(default=False)

    class Meta:
        db_table = 'df_address'

