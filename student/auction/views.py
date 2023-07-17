from django.shortcuts import render

def first(request):
    if request.method=='POST':
        return render(request,'home.html')
    else:
        return render(request,'home.html')
    
def login(request):
    if request.method=='POST':
        return render(request,'login.html')
    else:
        return render(request,'login.html')    
    
def upload(request):
    if request.method=='POST':
        return render(request,'upload.html')
    else:
        return render(request,'upload.html')  
    
def welcome(request):
    if request.method=='POST':
        return render(request,'welcome.html')
    else:
        return render(request,'welcome.html')     
    
def welcome1(request):
    if request.method=='POST':
        return render(request,'welcome1.html')
    else:
        return render(request,'welcome1.html')  
    
def choice(request):
    if request.method=='POST':
        return render(request,'choice.html')
    else:
        return render(request,'choice.html')             
      
