from django.shortcuts import render,get_list_or_404,get_object_or_404
from garments.models import Formalshirt,Casualshirt,Tshirt,Trouser,Jean,Trackpant
from garments.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here. 

def index(request,):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def formal_shirts(request):
    #lst=Formalshirt.objects.all()
    lst=get_list_or_404(Formalshirt)
    return render(request,'formal_shirts.html',{'lst':lst})

def casual_shirts(request):
    #lst=Casualshirt.objects.all()
     lst=get_list_or_404(Casualshirt)
     return render(request,'casual_shirts.html',{'lst':lst})

def t_shirts(request):
    #lst=Tshirt.objects.all()
     lst=get_list_or_404(Tshirt)
     return render(request,'t_shirts.html',{'lst':lst})



def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        subject='Hello from garments.com'
        message='This is what you typed:'+request.POST.get('content')
        from_email=settings.EMAIL_HOST_USER
        user_email=request.POST.get('contact_email')
        to_list=[user_email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})

def trouser(request):
    #lst=Trouser.objects.all()
     lst=get_list_or_404(Trouser)
     return render(request,'trousers.html',{'lst':lst})

def jean(request):
    #lst=Jean.objects.all()
     lst=get_list_or_404(Jean)
     return render(request,'jeans.html',{'lst':lst})

def trackpant(request):
    #lst=Track_pant.objects.all()
     lst=get_list_or_404(Trackpant)
     return render(request,'track_pants.html',{'lst':lst})

def thankyou(request):
    res=HttpResponse()
    res.write("<h1>Thanks for visiting our site</h1>")
    res.write("<h1>we just sent a mail to you</h1>")
    res.write("<h1>please go through it</h1>")
    return res

lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(Formalshirt,id=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'tot_price':sum(price)})