from django.shortcuts import render

# Create your views here.
def now(request):
    return render(request,'now.html')