from rest_framework import serializers, viewsets
from employees.models import Employee

# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'email', 'hired']

# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer