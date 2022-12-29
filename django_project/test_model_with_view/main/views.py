from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):

    def get(self, request):
        students = Student.objects.all() # ORM requests DJANGO_ORM CLASS.objects.all()
        # data = {
        #     'result': [1, 2, 3, 4, 5],
        #     'status_code': 200
        # }
        sertializer = StudentSerializer(instance=students, many=True)
        return Response(sertializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id=None):
        student = Student.objects.get(pk=id)
        print(student.first_name)
        student.delete()
        return Response('Successfulle delete object')