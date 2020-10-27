import json

from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .models import *
from .serializers import *
from django.test import Client


from rest_framework.test import APIRequestFactory, URLPatternsTestCase
from rest_framework.test import force_authenticate

from rest_framework.test import APIClient

from django.contrib.auth.models import User
from django.test.client import Client

class UserTest(APITestCase):
    def setUp(self):
        password = 'mypassword' 
        my_admin = User.objects.create_superuser('myuser12df',
            'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

    def test_get_all_users(self):
        url = reverse('user:user-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_new_users(self):
        #Add User 1 - Looking for CREATED
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
            'ssn' : '123456789', 'age' : 99}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        #Get user 1 - Looking for OK
        url = reverse('user:user-api-detail', kwargs={"pk" : 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Get User 2 - Looking for NOT_FOUND
        url = reverse('user:user-api-detail', kwargs={"pk" : 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 

        #Add User 2 - invalid ssn
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
            'ssn' : '12345689', 'age' : 99}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        #Add User 2 - invalid ssn
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
        'ssn' : '1234568449', 'age' : 99}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        #Add User 2 - invalid age
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
        'ssn' : '1234568449', 'age' : 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        #Add User 2 - invalid age
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
        'ssn' : '1234568449', 'age' : 1033}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        #Get User 2 - Looking for NOT_FOUND
        url = reverse('user:user-api-detail', kwargs={"pk" : 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        #Add User 2 - Looking for CREATED
        url = reverse('user:user-api-list')
        data = {'firstName' : 'testFirst', 'lastName' : 'testLast',
        'ssn' : '987654321', 'age' : 30}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #Get User 2 - Looking for OK
        url = reverse('user:user-api-detail', kwargs={"pk" : 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        #Assert data is stored correctly
        url = reverse('user:user-api-detail', kwargs={"pk" : 1})
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), {'firstName' : 'testFirst', 'lastName' : 'testLast',
            'ssn' : '123456789', 'age' : 99})

        url = reverse('user:user-api-detail', kwargs={"pk" : 2})
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), {'firstName' : 'testFirst', 'lastName' : 'testLast',
        'ssn' : '987654321', 'age' : 30})
