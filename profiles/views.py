from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def view_profile(request):
    #retrieve the currently logged in user
    user = request.user
    #passing the user object to the profile template/page
    return render(request,'profile.html',{'user':user})