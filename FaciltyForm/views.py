from django.shortcuts import render

# Create your views here.

def facility(request):
    return render(request, 'pages/facility.html')