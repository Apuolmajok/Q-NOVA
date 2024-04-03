from django.shortcuts import render

# Create your views here.
def Quick(request):
    return render(request, 'Quick.html',{})