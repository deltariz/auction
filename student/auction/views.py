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
        
