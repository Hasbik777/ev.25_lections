from django.http import Http404
from rest_framework.views import APIView

from .models import Task
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from . import serializers
from rest_framework import generics
#
#
# # function based-view
#
# # Class-based views
# # 3 вида:
# # Api View, Generics, ViewSet


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.TaskListSerializer
        return serializers.TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer



# class TaskListCreateApiView(APIView):
#     def get(self, request):
#         queryset = Task.objects.all()
#         serializer = serializers.TaskSerializer(instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = serializers.TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
#
# class TaskDetailApiView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         queryset = self.get_object(pk)
#         try:
#             serializer = serializers.TaskSerializer(queryset)
#             return Response(serializer.data, status=200)
#         except:
#             return Response(f'Does not exist this task with {pk} id!', status=404)
#
#     def put(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = serializers.TaskSerializer(instance=queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#
#     def delete(self, request, pk):
#         queryset = self.get_object(pk)
#         queryset.delete()
#         return Response({'msg':'Successfully deleted!'}, status=204)




##############################################################################################



# from django.shortcuts import render
#
# # from django.http import HttpResponse
# from .models import Task
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from . import serializers
# # Create your views here.
# # def hello_world(request):
# #     return HttpResponse('<h1>Hello_world</h1>')
#
#
# # 'GET',    'POST',     'PUT',     'PATCH',            'DELETE'
# # list       create     update     partial_update       destroy
# # retrieve
#
# # function based-view
#
#
# @api_view(['GET'])
# def tasks_list(request):
#     queryset = Task.objects.all()
#     serializer = serializers.TaskListSerializer(queryset, many=True)
#     return Response(serializer.data, status=200)
#
#
# @api_view(['GET'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         serializer = serializers.TaskSerializer(task)
#         return Response(serializer.data, status=200)
#     except Task.DoesNotExist:
#         return Response(f'This task with {id} id, does not exist!', status=404)
#
#
# @api_view(['POST'])
# def task_create(request):
#     # print(request.data, '!!!!!!!!!!')
#     serializer = serializers.TaskSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)
#
#
# @api_view(['PUTT', 'PATCH'])
# def task_update(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         if request.method == 'PUT':
#             serializer = serializers.TaskSerializer(instance=task, data=request.data)
#         else:
#             serializer = serializers.TaskSerializer(instance=task, data=request.data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=206)
#     except Task.DoesNotExist:
#         return Response(f'This task with {id} id, does not exist!', status=404)
#
#
# @api_view(['DELETE'])
# def task_delete(request, pk):
#     queryset = Task.objects.get(id=pk)
#     queryset.delete()
#     return Response({'msg': 'Successful delete'})