from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import ManagePlacement, Employee
# from rest_framework import generics
# from .serializers import ManagePlacementSerializer, EmployeeSerializer
# from rest_framework import viewsets


@csrf_exempt
def create_position(request):
    if request.method == 'POST':
        data = json.loads(request.position)
        new_position = ManagePlacement.objects.create(**data)
        json_data = {
            'position': new_position.position,
            'department': new_position.department,
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        positions = ManagePlacement.objects.all()
        data = []
        for position in positions:
            data.append(
                {
                    'position': position.position,
                    'department': position.department,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.fullname)
        new_employee = Employee.objects.create(**data)
        json_data = {
            'fullname': new_employee.fullname,
            'date_birth': new_employee.date_birth,
            'position': new_employee.position,
            'salary': new_employee.salary
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = []
        for employee in employees:
            data.append(
                {
                    'fullname': employee.fullname,
                    'date_birth': employee.department,
                    'department': employee.position,
                    'salary': employee.salary
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)



