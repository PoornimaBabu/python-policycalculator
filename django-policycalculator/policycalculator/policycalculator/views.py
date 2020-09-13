from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    #To return the HTML page
    return render(request, 'home.html')

def external(request):
    #Data from the webpage is passed to py script using POST method
    policynum = request.POST.get('policyno')
    policyStartDate = request.POST.get('policystartdate')
    premium = request.POST.get('premium')
    membership = request.POST.get('type')
    print(policynum, policyStartDate, premium, membership)
    #Sys.executable runs the external python script from the mentioned path
    out= run([sys.executable, 'D://calculatematurity.py', policynum, policyStartDate, premium, membership],shell=False,stdout=PIPE)
    #print(out.stdout)
    return render(request, 'home.html', {'data1':out.stdout.decode('utf-8')})