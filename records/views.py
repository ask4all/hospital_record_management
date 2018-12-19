from django.shortcuts import render

# Create your views here.

def home (requests):
	return render(requests, 'login.html')
''' def login(requests):
	return render(requests, 'accounts/validation.html')
'''
