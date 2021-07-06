from django.test import TestCase
from django.urls import resolve
from employees.models import Employee

class CreateAndListEmployees(TestCase):
    # check that deafault employees route lists all employees djangorestframework function
    def test_root_url_resolves_to_list_all_employees(self):
        found = resolve('/employees/')
        self.assertEqual(found.view_name, 'employee-list')

    def test_root_url_lists_all_employees_response_code(self):
        resp = self.client.get('/employees/', headers={'content-type': 'application/json'})        
        self.assertEqual(resp.status_code, 200)  # verify valid response code

    def test_root_url_lists_all_employees(self):
        Employee.objects.create(name='Alfredo Azevedo', email='alfredo@hotmail.com', hired='2019-10-12', salary=2000)
        Employee.objects.create(name='Anabela de Malhadas', email='anabela@hotmail.com', hired='2009-04-30', salary=600)
        
        #resp = self.client.get('/employees/', format='json')
        resp = self.client.get('/employees/', headers={'content-type': 'application/json'})
        self.assertEqual(len(resp.json()), 2)
        




