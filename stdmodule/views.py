from django.shortcuts import render
from stdmodule.models import Register, Feedback
import sqlite3
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

# Create your views here.
def menu(request):
    return render(request, "menu.html")
def index(request):
    return render(request, "index.html")
def login(request):
    if request.method=='POST':
        username = request.POST.get("myname")
        password = request.POST.get("mypassword")
        role = request.POST.get("role")
        if role=='Teacher':
            if username == "N20531" and password == "Itsday31":
                return render(request,"ahome.html")
            else:
                return render(request,"login.html")
        elif role =='Student':
            mark = 0
            conn = sqlite3.connect("/home/nikilbalaji/stdproject/db.sqlite3")
            c = conn.cursor()
            c.execute("select sid, password from stdmodule_Register where sid = ? and password = ?", (username, password))
            if c.fetchone() is not None:
                print("Welcome user")
                c.execute("select mark from stdmodule_Register where sid = '" + username + "'")
                for m in c.fetchone():
                    print(m)
                    if m == "0":
                        print("Till mark is not updated ")
                        return render(request,"login.html")
                    else:
                        request.session['sid']=username
                        c.execute("select * from stdmodule_Register where sid ='" + username + "'")
                        for d in c.fetchone():
                            print(d)
                    return render(request, "shome.html",{'sid':request.session['sid']})
            else:
                return render(request,"login.html")
            return render(request,"shome.html")
        else:
            return render(request,"login.html")
    return render(request, "login.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")


def menu2(request):
    return render(request, "menu2.html")
def ahome(request):
    return render(request, "ahome.html")
def studentregister(request):
    if request.method=='POST':
        sname1 = request.POST.get("sname")
        mobile1 = request.POST.get("mobile")
        email1 = request.POST.get("email")
        password1 = request.POST.get("password")
        course1 = request.POST.get("course")
        p = Register(sname=sname1,mobile=mobile1,email=email1,password=password1,course=course1)
        p.save();
        cdata = Register.objects.all()
        return render(request,"studentview.html",{'data':cdata})
    return render(request, "studentregister.html")
def studentview(request):
    cdata = Register.objects.all()
    return render(request, "studentview.html",{'data':cdata})
def markupdate(request):
    if request.method=='POST':
        sid1 = request.POST.get("myid")
        mark1 = request.POST.get("mymark")
        conn = sqlite3.connect('/home/nikilbalaji/stdproject/db.sqlite3')
        c = conn.cursor()
        c.execute("update stdmodule_Register set mark =? where sid = ?", (mark1, sid1))
        conn.commit()
        cdata = Register.objects.all()
        return render(request,"studentview.html",{'data':cdata})
    return render(request, "markupdate.html")
def sendemail(request):
    if request.method == 'POST':
        EmailId1 = request.POST.get("stemail")
        Subject1 = request.POST.get("stsubject")
        Message1 = request.POST.get("stmessage")
        email = EmailMessage(Subject1, Message1, to=[EmailId1])
        email.send()
        return render(request,"sendemail.html")
    return render(request,"sendemail.html")
def feedbackview(request):
    cdata = Feedback.objects.all()
    return render(request, "feedbackview.html",{'data':cdata})



def menu3(request):
    return render(request, "menu3.html", {'sid':request.session['sid']})
def shome(request):
    return render(request, "shome.html", {'sid':request.session['sid']})
def studentviewdetails(request):
    p = Register.objects.all()
    return render(request, "studentviewdetails.html",{'data':p})
def feedbackupload(request):
    if request.method=='POST':
        sid1 = request.POST.get("myid")
        sname1 = request.POST.get("myname")
        remarks1 = request.POST.get("myremarks")
        rating1 = request.POST.get("rating")
        p = Feedback(sid=sid1,sname=sname1,remarks=remarks1,rating=rating1)
        p.save();
        cdata = Feedback.objects.all()
        return render(request,"feedbackupload.html",{'data':cdata})
    return render(request, "feedbackupload.html",{'sid':request.session['sid']})


def upload(request):
    if request.method == 'POST' and 'document' in request.FILES:
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, "upload.html")

def display(request):
    return render(request, "display.html")