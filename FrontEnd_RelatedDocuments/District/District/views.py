from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.db import connection
from District.models import *

def homepage(request):
    return render(request,'Homepage.html')

def adminloginportal(request):
    return render(request,'AdminLoginPortal.html')

def adminportal(request):
    return render(request,'AdminPortal.html')

def citizenloginportal(request):
    return render(request,'CitizenLoginPortal.html')

def citizenportal(request):
    return render(request,'CitizenPortal.html')

def citizencomplaintportal(request):
    return render(request,'CitizenComplaintPortal.html')

def tehsildarloginportal(request):
    return render(request,'TehsildarLoginPortal.html')

def tehsildarportal(request):
    return render(request,'TehsildarPortal.html')

def tehsildarcomplaintsportal(request):
    return render(request,'TehsildarComplaintsPortal.html')

def sdologinportal(request):
    return render(request,'SDOLoginPortal.html')

def sdoportal(request):
    return render(request,'SDOPortal.html')

def aboutus(request):
    return render(request,'AboutUs.html')

def showallcitizen(request):
    showall = Citizens.objects.all()
    return render(request, 'CitizenDetails.html', {"data":showall})

def InsertCitizen(request):
    if request.method=="POST":
        saverecord=Citizens()
        saverecord.c_id=request.POST.get('c_id')
        saverecord.c_name=request.POST.get('c_name')
        saverecord.c_email=request.POST.get('c_email')
        saverecord.c_contact_no=request.POST.get('c_contact_no')
        saverecord.c_dob=request.POST.get('c_dob')
        saverecord.c_address=request.POST.get('c_address')
        saverecord.save()
        
        messages.success(request,'Citizens '+saverecord.c_id+' is saved successfully!') 
        return render(request,'InsertCitizen.html')
    else:
            return render(request,'InsertCitizen.html')

def runQuerySolvedComplaints(request):
    raw_query = "select cp1.cp_id, cp1.cp_issue, cp1.cp_location, ts1.ts_status, ts1.ts_duration from public.complaints cp1 join public.status ts1 on cp1.cp_id = ts1.cp_id where ts1.ts_status='Resolved' order by cp_id asc;"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'SolvedComplaints.html',{'data':alldata})

def runQueryStatusComplaints(request):
    raw_query = "select cp1.cp_id, cp1.cp_issue, cp1.cp_location, ts1.ts_status, ts1.ts_duration from public.complaints cp1 join public.status ts1 on ts1.cp_id = cp1.cp_id where cp1.cp_id='1010'"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'StatusComplaints.html',{'data':alldata})

def runQueryTehsilTehsildar(request):
    raw_query = "select t1.t_id, t1.t_name, t1.t_office_address, t1.s_zone, td1.td_id, td1.td_name, td1.td_email, td1.td_contact_no, td1.td_salary from public.tehsil t1 join public.tehsildars td1 on td1.td_id = t1.td_id;"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'TehsilTehsildarDetails.html',{'data':alldata})