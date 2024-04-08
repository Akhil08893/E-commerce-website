from django.shortcuts import render

# Create your views here.
def check_out(request):
    return render(request,'check_out.html',{})

def payment_success(request):
    return render(request,'payment_success.html',{})