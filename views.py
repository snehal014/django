from django.shortcuts import render
from .MyForm import InputForm
from django.http import HttpResponse


import mysql.connector as m

# database connectivity

mydatabase = m.connect(host="localhost", user="root", password="Dnyanesh@2326", database="netbanking_project")
query = "insert into Bank(Account_No,First_Name,Last_Name,Address,City,State,Phone_Number,Email,Customer_ID,Ac_Opening_Date,IFSC,FD,Balance) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # must be "s"
# query1 = "update Bank set Balance = Balance + 500 where Account_No=1"
# query2 = "update Bank set Balance = Balance - 500 where Account_No=2"
cursor = mydatabase.cursor()


# deposit="update Bank set Balance= Balance + "

# Create your views here.


def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)

def CRUD(request):
    return render(request,'CRUD.html')

def login(request):
    return render(request,'Login.html')

def transaction(request):
    return HttpResponse(request,'Welcome to transaction page')


def result(request):
    form = InputForm(request.POST)
    cursor.execute(query, [form['Account_No'].value(), form['First_Name'].value(), form['Last_Name'].value(), form['Address'].value(), form['City'].value(), form['State'].value(), form['Phone_Number'].value(), form['Email'].value(), form['Customer_ID'].value(), form['Ac_Opening_Date'].value(), form['IFSC'].value(), form['FD'].value(), form['Balance'].value()])
    mydatabase.commit()
    return HttpResponse("Data Inserted Successfully")
























# def Login(request):


#
# #Data base Deposite or widraw
# def Transaction(request,acnt,process,num):
#     form= InputForm(request.PUT)
#     cursor.execute(query1,[form['Account_No'].value(),form['Amount']])
#
#
# def myview(request,Bank):
#     res = Bank.object.all()