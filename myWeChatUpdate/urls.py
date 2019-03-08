from django.conf.urls import url,include
#format_suffix_patterns使用户可以自行定义返回的数据类型
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    url(r'^upfile/$', views.UpfileList.as_view()),
    url(r'^upfile/(?P<pk>\d+)/$', views.UpfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)