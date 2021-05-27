from django.shortcuts import render
from .models import index,slider_images
# Create your views here.
def page(request):
    value=index.objects.all()
    img = slider_images.objects.all()
    context={
        'value':value,
        'img':img
    }
    return render(request,'base.html',context=context)

def banner(request):
    img = slider_images.objects.all()
    context = {
        'img':img
    }
    return render(request,'slider.html',context=context)