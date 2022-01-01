from os import replace
from sys import excepthook
from django.http import request
from django.shortcuts import render, redirect
from datetime import date, datetime
import speech_recognition as sr
import re

from app.models import Customer, SuperUser

# Create your views here.


def IndexPage(request):
    return render(request, 'app/index.html')


def InsertUser(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            user = SuperUser.objects.create(
                UserName=username, Email=email, Password=password)
            message = 'Sign Up successfully'

            return render(request, "app/login.html", {'mssg': message})

        else:
            message = 'Password Not matched'

            return render(request, "app/index.html", {'mssg': message})


def ShowLoginPage(request):
    return render(request, 'app/login.html')


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        user = SuperUser.objects.get(UserName=username)

        if user:
            if user.Password == password:
                message = "Login successfully"
                all_customer = Customer.objects.all()
                return render(request, "app/home.html", {'all_data': all_customer})

            else:
                message = "Incorrect Password"
                return render(request, "app/login.html", {'mssg': message})

        else:
            message = "User not exist,Please Sign up first"
            return render(request, "app/login.html", {'mssg': message})


def InsertCustomer(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            contact = request.POST['phone']
            amount = request.POST['amount']
            weight = request.POST['weight']
            rate = request.POST['rate']
            description = request.POST['description']
            
            today_date = date.today().strftime("%d/%m/%y")

           

            if name=="" and contact=="" and amount=="" and weight=="" and rate=="":
                message = "Fields Cannot be empty"
                all_customer = Customer.objects.all()
                return render(request, 'app/home.html',{'mssgAlert':message,'all_data': all_customer})
            else:
                message = f"Customer {name} is Successfully Added" 
                customer = Customer.objects.create(Name=name, Contact=contact, Amount=amount, Date=today_date, Weight=weight, Rate=rate, Description=description)
                all_customer = Customer.objects.all()
                return render(request, 'app/home.html',{'mssgSuccess':message,'all_data': all_customer})

        except Exception:
            message = "Fields Cannot be empty or Something went wrong"
            print(message)

    # we write this because if Super user not make post request then also he will
    # able to see database
    all_customer = Customer.objects.all()
    return render(request, 'app/home.html', {'all_data': all_customer})


def Delete(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        name = customer.Name
        id = customer.id
        message = f"Customer Id:{id} with Name:{name} is Successfully Deleted"
        customer.delete()


        all_customer = Customer.objects.all()
        return render(request, 'app/home.html',{'mssgSuccess':message,'all_data': all_customer})

    except Exception:
        return redirect('insertpage')


def Editpage(request, pk):
    customer = Customer.objects.get(id=pk)

    return render(request, "app/edit.html", {'customer': customer})


def EditUser(request, pk):
    if request.method == 'POST':
        customer = Customer.objects.get(id=pk)
        
        # new date
        newName = request.POST['name']
        newContact = request.POST['phone']
        newAmount = request.POST['amount']

        newWeight = request.POST['weight']
        newRate = request.POST['rate']
        newDescription = request.POST['description']
        #here we take old date form database and concatenate with new date 
        #as if user change data in same field then it might chance to lost same data as user backspace long
        newDate = request.POST['newdate']

        if newDate!="":
            old=customer.Date
            combine_date = old+","+newDate
            # we use replace to show data in formated form in data column
            # ",\n" we automattically place , in every date
            ndate = combine_date.replace(",", ",\n")

        else:
            ndate = request.POST['olddate']

    
        customer.Name = newName
        customer.Contact = newContact
        customer.Amount = newAmount
        customer.Date = ndate
        customer.Weight = newWeight
        customer.Rate = newRate
        customer.Description = newDescription

        customer.save()
        return redirect('insertpage')


def DetailPage(request, pk):
    customer = Customer.objects.get(id=pk)

    return render(request, "app/detail.html", {'customer': customer})


def SearchCustomer(request):
    if request.method == 'POST':
        search = request.POST['searchtv']

        # Here we are checking if text input is string then search that in Name
        # and if it return false then check in Contact
        # checking using regex expresion
        matched = re.match(
            "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$", search)
        # if typed input match with regex then return true else false
        is_match = bool(matched)

        if is_match == True:
            # __conatins:-used to filter every row whose conatin same name
            customer = Customer.objects.filter(Name__contains=search)
            message = 'Customer Found'
            return render(request, 'app/search.html', {'mssg': message, 'customer': customer})

        else:
            customer = Customer.objects.filter(Contact__contains=search)
            message = 'Customer Found'
            return render(request, 'app/search.html', {'mssg': message, 'customer': customer})

    else:
        message = 'Customer Not found'
        return render(request, 'app/search.html', {'mssg': message})


def SuperuserOp(request):
    user = SuperUser.objects.all()
    return render(request, "app/op_superUser.html", {'all_user': user})


def DeleteSuper(request, sn):
    user = SuperUser.objects.get(id=sn)
    user.delete()
    return redirect('SuperuserOp')


def ShowCal(request):
    return render(request, "app/calculate.html")


def Calculator(request):
    if request.method == 'POST':
        try:
            pri_amount = request.POST['principle_amount']
            rate = request.POST['rate']
            old_date = request.POST['olddate']
            new_date = request.POST['newdate']

            a = float(pri_amount)
            r = float(rate)

            d0 = datetime.strptime(str(old_date), "%d/%m/%y")
            d1 = datetime.strptime(str(new_date), "%d/%m/%y")
            delta = d1 - d0
            no_days = delta.days

            interest_per_month = a*r/100
            interest_per_day = interest_per_month/30
            total_interest = no_days*interest_per_day

            if no_days < 30:
                interest = interest_per_month
            else:
                interest = total_interest

            return render(request, 'app/calculate.html', {'inte': interest, 'no': no_days})

        except Exception:
            message = "Fields Cannot be empty or Something went wrong"
            return render(request, 'app/calculate.html', {'mssg':message})

    #we not want to show error to user so if they press 
    return render(request, 'app/calculate.html')


def command1(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            q = query.lower()
            return render(request, 'app/home.html', {'key1': q})

        except:

            return "None"

        return query
