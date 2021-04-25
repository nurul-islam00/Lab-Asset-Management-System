

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import student
from .models import instrument
from django.contrib import messages
from .models import assign
from django.db.models import Q
from .models import *

def firstpage(request):

    return  render(request,"firstpage.html")

def student_profile(request):

    return  render(request,"student_profile.html")
def student_profile_search(request):
    id=request.POST.get('id1')
    item=student.objects.filter(id=id)

    if(len(item)==1):
        c=1
        item2=student.objects.get(id=id)
        item3=assign.objects.filter(regi_id=id)
        if(len(item3)==0):
            c=0
            return render(request,"student_profile_search.html",{'c':c,'item2':item2})
        else:

           return render(request,"student_profile_search.html",{'c':c,'item2':item2,'item3':item3})
    else:
        messages.error(request,"No such student found")
        return render(request,"student_profile_search.html")




    return  render(request,"student_profile.html")

def home2(request):
    return  render(request,"homepage2.html")
def student_login(request):
    return  render(request,"student_login.html")
def instrument_list_s(request):
    list = instrument.objects.all()
    return render(request, "instrument_list2.html", {'list': list})
def profile(request):
    id=request.session.get('id')
    item=student.objects.get(id=id)
    item2=assign.objects.filter(regi_id=id)
    c=int(1)
    if(len(item2)==0):
      c=0
      return render(request,"profile.html",{'c':c,'item2':item})
    else:
       item3=assign.objects.filter(regi_id=id)
       #item3=assign.objects.get(regi_id=id)
       return render(request,"profile.html",{'c':c,'item3':item3,'item2':item})


def student_login2(request):
    id = request.POST.get('id')
    code = request.POST.get('pwd')
    item=student.objects.filter(id=id)
    item2=student.objects.filter(code=code)

    if(len(item)==1 and len(item2)>=1):
         item3=student.objects.get(id=id)
         if(item3.id==id and item3.code==code):
           request.session['id'] = id
           return render(request,"homepage2.html")
         else:
            messages.error(request,"Enter Correct Information")
            return render(request,"student_login.html")
    else:
        messages.error(request, "Enter Correct Information")
        return render(request, "student_login.html")


    return  render(request,"student_login.html")
def home(request):
    return  render(request,"homepage.html")
def student_list(request):
    list=student.objects.all()
    return  render(request,"student_list.html",{'list':list})

def instrument_list(request):
    list=instrument.objects.all()
    return  render(request,"instrument_list.html",{'list':list})
def student_search(request):
        qur = request.POST.get('search')
        match = student.objects.filter(Q(id__icontains=qur) | Q(email__icontains=qur) | Q(name__icontains=qur) | Q(batch__icontains=qur)| Q(hall__icontains=qur)).distinct()
        # match=user.objects.filter(email__contains=qur)
        c=1
        if(len(match)==0):
            c=0
        return render(request, "student_list2.html", {'ab': match,'c':c})


def delete(request,id):
    item=assign.objects.filter(regi_id=id)
    for x in item:
        y=x.regi_id
        item2=assign.objects.filter(regi_id=y)
        z=x.ins_id
        item4=instrument.objects.get(id=z)
        item4.status="Available"
        item4.save()
        item2.delete()
    item3=student.objects.get(id=id)
    item3.delete()
    list=student.objects.all()

    return render(request,"student_list.html",{'list':list})


def instrument_search_admin(request):
    qur = request.POST.get('search')
    match = instrument.objects.filter(Q(id__icontains=qur) | Q(price__icontains=qur) | Q(name__icontains=qur) | Q(ins_type__icontains=qur) | Q(status__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    c = 1
    if (len(match) == 0):
        c = 0
    return render(request, "instrument_list2_admin.html", {'ab': match, 'c': c})


def collect_instrument(request):
    return  render(request,"collect_instrument.html")
def confirm_ins_collect(request):
    if(request.method=='POST'):
        id1=request.POST.get('id1')
        id2=request.POST.get('id2')

        item = assign.objects.filter(ins_id=id1)
        item2=assign.objects.filter(regi_id=id2)
        if(len(item)>=1 and len(item2)>=1):
            check=assign.objects.get(ins_id=id1)
            if(check.ins_id==id1 and check.regi_id==id2):
                item3=instrument.objects.get(id=id1)
                item3.status="Available"
                item3.save()
                dlt = assign.objects.get(ins_id=id1)
                dlt.delete()
                messages.success(request,"The Instrument is collected successfully")
            else:
                messages.error(request,"Please Enter correct Information")

        else:
                 messages.error(request,"Please Enter correct Information")
    return render(request,"collect_instrument.html")

def confirm_ins_assign(request):
    if(request.method=='POST'):
        id1 = request.POST.get('id1')
        id2 = request.POST.get('id2')
        item=instrument.objects.filter(id=id1)
        item2=student.objects.filter(id=id2)
        if(len(item)==0):
            messages.error(request,"The instrument doesn't exist")
        elif(len(item2)==0):
            messages.success(request,"The registration number is incorrect")
        else:
           item3=instrument.objects.get(id=id1)
           if(item3.status=="Unavailable"):
               messages.error(request,"The instrument is not available")

           else:
               item3.status="Unavailable"
               assign_details=assign(ins_id=id1,regi_id=id2)
               assign_details.save()
               item3.save()
               messages.success(request,"The instrument is assigned successfully")




    return render(request,"assign_instrument.html")







    return  render(request,"firstpage.html")
def assign_instrument(request):
    return  render(request,"assign_instrument.html")
def student_registration(request):
    return  render(request,"student_registration.html")
def instrument_registration(request):
    return  render(request,"instrument_registration.html")
def confirm_ins_registration(request):
    if (request.method == 'POST'):
         id = request.POST.get('id')
         name = request.POST.get('name')
         price = request.POST.get('price')
         ins_type = request.POST.get('ins_type')
         price=int(price)

    
         a = int(1)
         if (instrument.objects.filter(pk=id).exists()):
            a = 0
            messages.error(request, "The ID Number is already registered.Try with another ID")
         if (price<0):
            a = 0
            messages.error(request, "The Price must be a positive number")

         if(ins_type=="" or ins_type=="Choose Instrument Type"):
             a=0
             messages.error(request,"Choose Instrument Type")
         if (a == 0):
           return render(request, "instrument_registration.html")
         else:
            instrument_details = instrument(id=id,name=name, price=price,ins_type=ins_type,status="Available")
            instrument_details.save()

            messages.success(request, "Instrument is added successfully")
            # return  render(request,"firstpage.html")
            return render(request, "Instrument_registration.html")

    return  render(request,"instrument_registration.html")
def confirm_registration(request):
    if (request.method == 'POST'):
        id = request.POST.get('id')
        email = request.POST.get('email')
        name=request.POST.get('name')
        batch = request.POST.get('batch')
        code = request.POST.get('code')
        hall = request.POST.get('hall')
        a = int(1)
        if (student.objects.filter(pk=id).exists()):
            a = 0
            messages.error(request, "The Registration Number is already registered.")
        if (len(code) < 5):
            a = 0
            messages.error(request, "The Secret Code must be at least 5 character long")
        if (a == 0):
            return render(request, "student_registration.html")

        else:
            student_details = student(id=id, email=email, name=name, batch=batch, code=code, hall=hall)
            student_details.save()

            messages.success(request, "Student registration is successfully completed")
            # return  render(request,"firstpage.html")
            return render(request, "student_registration.html")

def admin_login(request):
    if (request.method == 'POST'):
        p = request.POST.get('admin')
        q=request.POST.get('pwd')
        if(p=="admin"  and q=="admin"):
          return render(request,"homepage.html")
        else:
            return redirect('/')