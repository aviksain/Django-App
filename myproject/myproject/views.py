from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  # return HttpResponse("<h1>This is our Home Page</h1>")
  return render(request, 'website/home.html')

def about(request):
  # return HttpResponse("<h1>This is our About Page</h1>")
  return render(request, 'website/about.html')

def contact(request):
  # return HttpResponse("<h1>This is our Contact Page</h1>")
  return render(request, 'website/contact.html')
