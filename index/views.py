from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    return render(request, 'index/index.html')