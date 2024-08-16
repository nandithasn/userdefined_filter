from django.shortcuts import render
# Create your views here.
def usd(request):
    d={'data':'virat loves his family'}
    return render(request,'usd.html',d)
