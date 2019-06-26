from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Bitly
from django.http import HttpResponse,HttpResponseRedirect

from .forms import  BitlyForm,editBitly

def index (request):
    objects = Bitly.objects.all()
    context = {'objs':objects}
    return render(request,'index.html',context)

def create(request):
    from .utlis import create_shortcode
    form=BitlyForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit = False)
        instance.Shortcode= create_shortcode()
        instance.datewise=""
        instance.save()

        return HttpResponseRedirect("http://127.0.0.1:8000/home/")

    context = {"urlform":form}
    return render(request,"create.html",context)    

def goto(request,Shortcode= None):
    qs=get_object_or_404(Bitly,Shortcode__iexact=Shortcode) 
    return HttpResponseRedirect(qs.long_url)

def update (request, pk=None):
    qs=get_object_or_404(Bitly,id=pk)
    form=editBitly(request.POST or None, instance=qs)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home")
    context={'urlform':form}
    return render(request,"create.html",context)    