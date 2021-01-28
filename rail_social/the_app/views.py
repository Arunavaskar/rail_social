from django.http.response import HttpResponse
from django.shortcuts import render
# from django.views import View

# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         return HttpResponse('Hello World')

#functions based views

def HomeView(request):
    return HttpResponse("Hello World")