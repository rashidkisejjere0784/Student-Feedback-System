from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def index(request):

    # Page from the theme 
    if request.user.is_authenticated:
        return render(request, 'pages/index.html')
    
    else:
        return redirect("login")
