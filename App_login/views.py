from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from App_login.forms import *


def hod_signup(request):
    form1 = HODUserForm()
    form2 = HODForm()
    if request.method == 'POST':
        form1 = HODUserForm(data=request.POST)
        form2 = HODForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            editor_grp = Group.objects.get_or_create(name='HOD')
            editor_grp[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_main:hod-dashboard'))
    return render(request, 'App_login/hod_signup.html', context={'form1': form1, 'form2': form2})


def officer_signup(request):
    form1 = OfficerUserForm()
    form2 = OfficerForm()
    if request.method == 'POST':
        form1 = OfficerUserForm(data=request.POST)
        form2 = OfficerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            publisher_grp = Group.objects.get_or_create(name='OFFICER')
            publisher_grp[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_main:hod-dashboard'))
    return render(request, 'App_login/officer_signup.html', context={'form1': form1, 'form2': form2})


def reporter_signup(request):
    form1 = ReporterUserForm()
    form2 = ReporterForm()
    if request.method == 'POST':
        form1 = ReporterUserForm(data=request.POST)
        form2 = ReporterForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            reporter_grp = Group.objects.get_or_create(name='REPORTER')
            reporter_grp[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_main:hod-dashboard'))
    return render(request, 'App_login/reporter_signup.html', context={'form1': form1, 'form2': form2})


def hod_officer_login(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        designation = request.POST.get('designation')
        password = request.POST.get('password')
        try:
            try:
                this_user = HeadOfDepartmentModel.objects.get(employee_id=emp_id, designation=designation, status=True)
                username = this_user.user.username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if request.user.groups.filter(name__in=['HOD']).exists():
                        return HttpResponseRedirect(reverse('App_main:hod-dashboard'))
                    else:
                        return HttpResponseRedirect(reverse('App_login:hod-login'))
            except ObjectDoesNotExist:
                this_user = OfficerModel.objects.get(employee_id=emp_id, designation=designation, status=True)
                username = this_user.user.username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if request.user.groups.filter(name__in=['OFFICER']).exists():
                        return HttpResponseRedirect(reverse('App_main:officer-dashboard'))
                    else:
                        return HttpResponseRedirect(reverse('App_login:hod-login'))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('App_login:hod-login'))
    return render(request, 'App_login/hod_login.html')


def reporter_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            this_user = ReporterModel.objects.get(user__email=email, status=True)
            username = this_user.user.username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.groups.filter(name__in=['REPORTER']).exists():
                    return HttpResponseRedirect(reverse('App_main:reporter-dashboard'))
                else:
                    return HttpResponseRedirect(reverse('App_login:reporter-login'))

        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('App_login:reporter-login'))
    return render(request, 'App_login/reporter_login.html')


def logout_system(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_main:home'))
