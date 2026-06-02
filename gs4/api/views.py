from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from . import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class student_api(View):
    def get(self,request,*args,**kwargs):
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get("id", None)
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = serializers.StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type="application/json")
            stu = Student.objects.all()
            serializer = serializers.StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")

    def post(self,request,*args,**kwargs):
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = serializers.StudentSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type="application/json")

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")

    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        # for partial update
        serializer = serializers.StudentSerializer(stu, data=pythondata, partial=True)
        # for full update
        # serializer = serializers.StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(res, safe=False)
