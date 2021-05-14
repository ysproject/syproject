from django.shortcuts import render, redirect

# Create your views here.
def classhome(request):
    return render(request, 'class/classhome.html')