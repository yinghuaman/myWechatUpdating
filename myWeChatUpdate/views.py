from django.shortcuts import render,redirect
#from django.http import HttpResponse,JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from rest_framework import generics
from .models import WechatUpdate,Pagination
from .serializers import WechatUpdateSerializer
# Create your views here.

class UpfileList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = WechatUpdate.objects.all()
    serializer_class = WechatUpdateSerializer
    #pagination_class = Pagination

    # 列出已有的动态或者创建新的动态
    def get(self,request):
        obj = Pagination()
        page_list = obj.paginate_queryset(self.queryset, request)
        serial = self.serializer_class(instance=page_list, many=True)
        response = obj.get_paginated_response(serial.data)
        return response

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class UpfileDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    #查询、更新或者删除某条动态
    queryset = WechatUpdate.objects.all()
    serializer_class = WechatUpdateSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)







