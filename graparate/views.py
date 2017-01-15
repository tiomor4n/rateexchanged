# -*- coding: utf8 -*-
from datetime import datetime
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from rateexchanged import settings
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from bs4 import BeautifulSoup as bs
import urllib.request, requests, sys, json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
#from urllib2 import urlopen, HTTPError, request
from graparate.crawer import DataPipe

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())

def index(request):
    txt=json.loads(DataPipe())
    print (len(txt))
    return render(request,'index.html',{'data':txt})
    #return render_to_response('index.html',locals())

def grsp(request):
    txt = DataPipe()
    return HttpResponse(txt)

def bankpack(request):
    #url = 'https://test-pro-tiomor4n.c9.io/here/'
    url = "http://127.0.0.1:8000/static/java/test.json"
    jsonparser = urllib.urlopen(url).read()
    #jsonparser = urlopen()
    getdata = jsonparser.read()
    pos_start = getdata.find('[')
    pos_end = getdata.find(']')
    usedata = getdata[(pos_start):pos_end]
    getjson = json.loads(usedata)
    for i in range(len(getjson)):
        print (getjson[i]['bankname'])

def test(requestion):
    '''
    request = urllib.request.Request("http://127.0.0.1:8000/static/java/currency_type.json")
    response = urllib.request.urlopen(request)
    
    #print (response.read().decode('utf-8'))
    
    cashholder = response.read().decode('utf-8')
    r = cashholder
    '''
    rArr=[]
    r = requests.get("http://127.0.0.1:8000/static/java/currency_type.json").json()
    print (type(r))
    rArr.append(r)
    rr = json.dumps(rArr)
    print ('rr type :' + str(type(rr)))
    print ('rr len:' + str(len(rr)))
    rrr = json.loads(rr)
    print ('rrr type :' + str(type(rrr)))
    print ('rrr len :' + str(len(rrr)))
    return render(requestion, 'test.html', {
           'r': rrr,
           })
    #return render_to_response('test.html',locals())
'''
class CType(object):
    def __init__(self, Nation, Language, Currency):
        self = self
        self.Nation = Nation
        self.Language = Language
        self.Currency = Currency

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'CType':
        return CType(obj,obj['Nation'], obj['Language'], obj['Currency'])
    return obj

json.loads('http://127.0.0.1:8000/static/java/currency_type.json', object_hook=object_decoder)

print (type(CType))
'''


def test2(request):
    return render_to_response('test2.html',locals())

base_dir = settings.BASEDIR()
filter = base_dir + "/templates/" + ""
