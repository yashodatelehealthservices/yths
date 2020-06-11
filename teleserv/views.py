from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, "home.html")
def TeleEducation(request):
	return render(request, "TeleEducation.html")
def TeleDietics(request):
	return render(request, "TeleDietics.html")
def index(request):
	return render(request, "home.html")
def Pathology(request):
	return render(request, "Pathology.html")
def Online(request):
	return render(request, "Online.html")