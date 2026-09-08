from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import register, ReportForm


# Create your views here.
def register(request):

    if request.method == 'POST':
        form  = register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
            login(request,user)
            messages.success(
                request,
                "Registation Successful"
            )
            return redirect ('home')
    else:
        form = register()
    return render(
        request,
        'reports/register.html',
        {'form':form}

    )

def home(request):
    return render(
                request, 
                'reports/home.html'
                )

def user_login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
            messages.success(
                request,
                "Login Successful"
            )
            return redirect(home)
        else:
            messages.error(
                request,
                "Invalid Username or Password."
            )
    return render(
        request,
        'reports/login.html'
    )


def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfull.")

    return redirect('home')

@login_required
def create_report(request):
    if request.method == "POST":
        report_form = ReportForm(request.POST,request.FILES)
        if report_form.is_valid():
            report = report_form.save(commit = False)
            report.owner = request.user
            report.save()
            messages.success(request,
                             "Report Created Successfully")
            return redirect('home')
    else:
        report_form = ReportForm()

    return render(request,'reports/report_form.html',{'form': report_form})
        



        



