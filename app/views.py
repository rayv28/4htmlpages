from django.shortcuts import render

# Create your views here.
def fun1(request):
  return render(request,'one.html')

def fun2(request):
  return render(request,'two.html')

def fun3(request):
  return render(request,'three.html')

def fun4(request):
  return render(request,'four.html')
