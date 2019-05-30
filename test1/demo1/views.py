from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    banners=banner.objects.all()
    learns=learn.objects.all()
    for i in learns:
        i.width='385px'
        i.height='453px'
        i.save()
    newses=news.objects.all()
    return render(request, 'index.html',locals())
def about(request):
    us_teams=us_team.objects.all()
    chose_uss=chose_us.objects.all()
    return render(request, 'about.html', locals())
def services(request):
    services=service.objects.all()
    pro_services=pro_service.objects.all()
    us_suppots=us_suppot.objects.all()
    return render(request, 'services.html', locals())
def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    elif request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        subject=request.POST.get('Subject')
        message=request.POST.get('Message')
        print(name,email,subject,message)
        send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[email])
        # '1943158197@qq.com'
        return render(request,'contact.html')
    else:
        return HttpResponse("访问出错")
def wedding(request):
    imglists=imglist.objects.all()
    return render(request, 'wedding.html', locals())
