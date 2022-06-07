from django.shortcuts import render
import library.models
from library.models import *
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
import pyodbc
import platform
import socket
import os

def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'add_book_info.html',{'Book':Book})

def AddBookSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            bookid = request.POST["bookid"]
            bookname = request.POST["bookname"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            add = AddBook(user = user1,bookid=bookid,bookname=bookname,subject=subject,category=category)
            add.save()
            Book = AddBook.objects.all()
            return render(request,'BookAdd.html',{'Book':Book})
    return redirect('/')

def deletebook(request,id):
    if request.session.has_key('is_logged'):
        AddBook_info = AddBook.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("Login")

def bookinfo(request):
    return render(request,'bookinfo.html')


def editbookdetails(request, id):
    if request.session.has_key('is_logged'):
        Book = AddBook.objects.get(id=id)
        return render(request, 'editdetails.html', {'Book': Book})
    return redirect('login')


def updatedetails(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            add = AddBook.objects.get(id=id)
            add.bookid = request.POST["bookid"]
            add.bookname = request.POST["bookname"]
            add.subject = request.POST["subject"]
            add.ContactNumber = request.POST['category']
            add.save()
            return redirect("dashboard")
    return redirect('login')

def SignupBackend(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        phone = request.POST['phone']
        password = request.POST['password']
        userprofile = UserExtend(phone=phone)
        if request.method == 'POST':
            try:
                UserExists = User.objects.get(username=request.POST['uname'])
                messages.error(request, " Username already taken, Try something else!!!")
                return redirect("staffsignup")
            except User.DoesNotExist:
                if len(uname) > 10:
                    messages.error(request, " Username must be max 15 characters, Please try again")
                    return redirect("staffsignup")

                if not uname.isalnum():
                    messages.error(request, " Username should only contain letters and numbers, Please try again")
                    return redirect("staffsignup")

        # create the user
        user = User.objects.create_user(uname, email, password)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        userprofile.user = user
        userprofile.save()
        messages.success(request, " Your account has been successfully created")
        return redirect("stafflogin")
    else:
        return HttpResponse('404 - NOT FOUND ')


def LoginBackend(request):
    if request.method == 'POST':
        loginuname = request.POST["loginuname"]
        loginpassword = request.POST["loginpassword"]
        RegisteredUser = authenticate(username=loginuname, password=loginpassword)
        if RegisteredUser is not None:
            dj_login(request, RegisteredUser)
            request.session['is_logged'] = True
            RegisteredUser = request.user.id
            request.session["user_id"] = RegisteredUser
            messages.success(request, " Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404-not found')


 def Logout(request):
        del request.session['is_logged']
        del request.session["user_id"]
        logout(request)
        messages.success(request, " Successfully logged out")
        return redirect('dashboard')


