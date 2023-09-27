from django.shortcuts import render,redirect,HttpResponse ,get_object_or_404
from rest_framework.response import Response  
from rest_framework import status  
from .models import knowledge_base  
from rest_framework.views import APIView
from .serializers import knowledge_base_Serializer  
from django.views import View
from rest_framework.views import APIView
from django.views import *

class knowledge_base_view(APIView):
    def get(self, request):
        students = knowledge_base.objects.all()
        serializer = knowledge_base_Serializer(students, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
  
    def post(self, request):
        serializer = knowledge_base_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        data = request.data
        student_id = data.get('id')

        try:
            student = knowledge_base.objects.get(id=student_id)
        except knowledge_base.DoesNotExist:
            return Response({"status": "error", "message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = knowledge_base_Serializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):   
        data = request.data
        student_id = data.get('id')
        # student_id = data.get(id=id)

        try:
            student = knowledge_base.objects.get(id=student_id)
            student.delete()
            return Response({"status": "success", "message": "Student deleted successfully"}, status=status.HTTP_200_OK)
        except knowledge_base.DoesNotExist:
            return Response({"status": "error", "message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)




class knowledge_base_view_templates(APIView):
    def get(self, request):
        students = knowledge_base.objects.all()
        return render(request, 'home.html', {'students1': students})


class addview(APIView):
    def get(self, request):
        return render(request, "add.html")

    def post(self, request):
        ufname = request.POST.get('first_name')
        ulname = request.POST.get('last_name')
        uaddress = request.POST.get('address')
        uroll_number = request.POST.get('roll_number')
        umobile = request.POST.get('mobile')
        knowledge_base(first_name=ufname, last_name=ulname, address=uaddress, roll_number=uroll_number,
                       mobile=umobile).save()
        return redirect('knowledge_templates')


class update(View):
    def get(self, request, id):
        try:
            student = knowledge_base.objects.get(pk=id)
            return render(request, 'update.html', {'student': student})
        except student.DoesNotExist:
            return render(request, 'error_404.html')

    def post(self, request, id):
        data = request.POST
        try:
            student = knowledge_base.objects.get(pk=id)
        except student.DoesNotExist:
            # return render(request, '.html')/
            return HttpResponse("Not Exist")

        # Manually update the fields
        student.first_name = data.get('first_name')
        student.last_name = data.get('last_name')
        student.address = data.get('address')
        student.roll_number = data.get('roll_number')
        student.mobile = data.get('mobile')

        student.save()

        return redirect('knowledge_templates') 

class deleteView(View):
    def get(self, request, id):
        try:
            student = knowledge_base.objects.get(pk=id)
        except student.DoesNotExist:
            return render(request, 'error_404.html')

        student.delete()
        return redirect('knowledge_templates')
