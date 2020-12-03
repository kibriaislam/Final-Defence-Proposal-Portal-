from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import defenceInfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import xlwt
from django.core.mail import send_mail
from django.conf import settings

#home page view
def home_view(request):
    return render(request,'Home.html')



#login view
def login_view(request):
    return render(request,'login.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request,'Home.html')



#show student list in the front-end and authenticate user to view the list
def student_list(request):
    if request.method=="POST":
        username = request.POST.get('uname')
        password=request.POST.get('psw')
        user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request, user)
        data=[]
        data=defenceInfo.objects.all()
        return render(request,'studentlist.html',{'data': data})
    else:
        messages.info(request,'Your username or password is incorrect!!')
        return render(request,'login.html')




#getting all the reponse value and saved it in the database
def get_value(request):
    sId = request.POST["sId"]
    sName = request.POST["sName"]
    batch = request.POST["batch"]
    semester = request.POST["semester"]
    email = request.POST["email"]
    pNumber = request.POST["pNumber"]
    year=request.POST["year"]
    defence=request.POST["defence"]
    title = request.POST["title"]
    description = request.POST["description"]

    data = defenceInfo(sId=sId,sName=sName,batch=batch,semester=semester,email=email,year=year,defence=defence,pNumber=pNumber,title=title,description=description)
    data.save()
    
    return render(request,'Home.html')



#generating excell sheet 
@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Proposal_Report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('defenceInfo')

    # Sheet header,first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Student Name', 'Student ID', 'Batch', 'Semester','Email','Year','Phone','Type','Title','Description' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    #Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = defenceInfo.objects.all().values_list('sName', 'sId', 'batch','semester' ,'email','year','pNumber','defence','title','description')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required
def emailPage(request):

    return render(request,'email.html')
@login_required
def email_send(request):
    #query with semester and year
    data=[]
    semester1=request.POST['semester1']
    year1=request.POST['year1']

    data=defenceInfo.objects.filter(

        semester=semester1,
        year=year1,


        )
    print(data)

    subject = request.POST['subject']
    message = request.POST['message']
    email_from = settings.EMAIL_HOST_USER
    recipient_list=[]
    for data in data:
        recipient_list.append(data.email)
        
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'email.html')

