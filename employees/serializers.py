from rest_framework import serializers
from .models import ManagePlacement, Employee


class ManagePlacementSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=40)
    department = serializers.IntegerField()

    def create(self, validated_data):
        manage = ManagePlacement.objects.create(
            position=validated_data['position'],
            department=validated_data['department']
        )
        return manage

    def update(self, instance, validated_data):
        instance.position = validated_data['position']
        instance.department = validated_data['department']
        return instance


class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=35)
    date_birth = serializers.DateField()
    position = serializers.IntegerField()
    salary = serializers.CharField()

    def create(self, validated_data):
        employee = Employee.objects.create(
            fullname=validated_data['fullname'],
            date_birth=validated_data['date_birth'],
            position=validated_data['position'],
            salary=validated_data['salary']
        )
        return employee

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.date_birth = validated_data['date_birth']
        instance.position = validated_data['position']
        instance.salary = validated_data['salary']
        return instance