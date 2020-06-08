from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import smtplib
from .models import Register
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
c=0

def index(request):
    return render(request, 'admin/login.html')

def register(request):
    return render(request,'admin/register.html')
def fetch(request):
    r = Register()
    if request.method =='POST':
        r.fname = request.POST.get('fName')
        r.lname = request.POST.get('lName')
        r.email = request.POST.get('Name')
        r.password = request.POST.get('Password')
        cpassword = request.POST.get('CPassword')
        if r.password == cpassword:
            r.save()
        else:
            return render(request,'admin/register.html')
        return render(request,'admin/login.html')
# Create your views here.
def home(request):
    return render(request,'admin/index.html')
def checkUser(request):
    r = Register.objects.all().values('email','password')
    count =0
    if request.method =='POST':
        if request.POST.get('Name') and request.POST.get('Password'):
            for i in range(len(r)):
                if r[i]['email'] == request.POST.get('Name') and r[i]['password'] == request.POST.get('Password'):
                   count = 1
                   return render(request,'admin/index.html')
            if(count == 0):
                return render(request,'admin/login.html')

def index1(request):
    context = 'hello world'
    return render(request, 'admin/webpage.html', {'context': context})

def prediction(request):
    # -*- coding: utf-8 -*-


    # import libraries


    # import dataset
    # dataset = pd.read_csv('AhmDataSet_new_test.csv')
    # x = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:, 5].values
    global c
    if(request.method=='POST'):
        rooms = request.POST['rooms']
        area = request.POST['area']
        square_foot=request.POST.get('square_foot')
        construction = request.POST['construction_status']
        bathroom=request.POST['bathroom']

        rooms=int(rooms)
        square_foot=int(square_foot)
        bathroom = int(bathroom)


    x_dummy = [rooms, area, square_foot, construction, bathroom]
    x_dummy_df = pd.DataFrame([x_dummy])
    x_dummy_test = np.array(x_dummy_df)

    x_test = x_dummy_test

    # Load and perform encoding
    labelencoder_x_1 = joblib.load('LE_1.sav')
    labelencoder_x_3 = joblib.load('LE_3.sav')
    onehotencoder = joblib.load('OHE.sav')

    x_test[:, 1] = labelencoder_x_1.transform(x_test[:, 1])
    x_test[:, 3] = labelencoder_x_3.transform(x_test[:, 3])

    x_test = onehotencoder.transform(x_test).toarray()

    # Decison Tree
    regressor_dt = joblib.load('predict_decision_tree.sav')
    y_pred_dt = regressor_dt.predict(x_test)
    if y_pred_dt >= 100:
        c= y_pred_dt/100
        c = float(c)
        a = 'cr'
    else:
        c= y_pred_dt
        c = float(c)
        a = 'lakhs'

    c =str(c)+' '+a
    # Random Forest
    #regressor_rf = joblib.load('predict_random_forest.sav')
    #y_pred_rf = regressor_rf.predict(x_test)

    # Gradient Boosting
    #regressor_gb = joblib.load('predict_gradient_boosting.sav')
    #y_pred_gb = regressor_gb.predict(x_test)

    return render(request,'admin/property.html',{'context':c,'rooms':rooms,'square_foot':square_foot,'area':area,'construction':construction,'bathroom':bathroom})

def page(request):
    return render(request,'admin/property.html')
def contact(request):
    return render(request,'admin/contact.html')
def about (request):
    return render(request,'admin/about.html')
def mail(request):
    if request.method =='POST':
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(message)
    # content = message + name + email + subject




    msg = 'Name :- '+name+'<br>Email :- '+email+'<br>Message :- '+message
    # mail.sendmail('5995.stkabirdin@gmail.com','jash2531998@gmail.com','')
    the_message = MIMEMultipart("alternative")
    the_message['FROM'] = '5995.stkabirdin@gmail.com'
    the_message['TO'] = 'jash2531998@gmail.com'
    the_message['SUBJECT'] = subject
    the_message.attach(MIMEText(msg,'html'))
    content = the_message.as_string()
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    # mail.ehlo()
    mail.starttls()
    mail.login('5995.stkabirdin@gmail.com', 'yash5995@')

    mail.sendmail('5995.stkabirdin@gmail.com','shimolishah1@gmail.com',content)
    mail.quit()
    return render(request,'admin/contact.html')
def property(request):
    return render(request,'admin/best_property.html')
def ganesh(request):
    return render(request,'admin/ganesh_maple_tree.html')
def goyal(request):
    return render(request,'admin/goyal.html')
def keshar(request):
    return render(request,'admin/keshar.html')
def sobha(request):
    return render(request,'admin/sobha.html')
def parshwa(request):
    return render(request,'admin/parshwa.html')
def setu(request):
    return render(request,'admin/setu.html')
def shree(request):
    return render(request,'admin/balaji.html')
def saanvi(request):
    return render(request,'admin/saanvi.html')