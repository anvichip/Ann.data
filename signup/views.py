from django.shortcuts import render
import mysql.connector as mysql
fn=''
em=''
pwd=''
area = ''
# Create your views here.
def signaction(request):
    global fn,ln,g,em,pwd
    if request.method=="POST":
        m=mysql.connect(host="localhost",user="root",passwd="root",database='fms')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="farmer_name":
                fn=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key =="area":
                area=value
        c="insert into user_details values('{}','{}','{}','{}','{}')".format(fn,em,pwd, area)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')