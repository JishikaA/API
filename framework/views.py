from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from framework.models import Employee, Student
from framework.serializers import SnippetSerialize, StudentSerialize


# Create your views here.

def test(request):
    return render(request,'test.html')


class Snippet:
    pass


class SnippetSerializer:
    pass


@api_view(['GET','POST'])
def snippet_list(request):

    if request.method == 'GET':
        snippets = Employee.objects.all()
        serializer = SnippetSerialize(snippets,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = SnippetSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','PATCH','DELETE'])
def crud_employee(request,id):
    try:
        employee =Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer =SnippetSerialize(employee)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer =SnippetSerialize(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = SnippetSerialize(employee, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def student_mark(request):

    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerialize(snippets,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','PATCH','DELETE'])
def crud(request,id):
    try:
        student =Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer =StudentSerialize(student)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer =StudentSerialize(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentSerialize(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

