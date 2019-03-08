from django.db import models

# Create your models here.
from rest_framework.pagination import LimitOffsetPagination
import datetime
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25)
    gender = models.BooleanField(default=1)

    class Meta:
        db_table = "user"
    def __str__(self):
        return self.username


class WechatUpdate(models.Model):
    text = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to=str('static\img\{time}'.format(time=str(datetime.date.today().strftime("%Y%m/%d")))))
    username = models.CharField(max_length=25)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wechatupdate"
        ordering = ["-create_time"]
    def __str__(self):
        return self.username



class Pagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = None
