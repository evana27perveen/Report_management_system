from django.shortcuts import render, HttpResponseRedirect, reverse
import calendar

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
import datetime
from App_login.models import *
from App_main.forms import AssignForm
from App_main.models import ReportViewModel, ReportModel, AssignModel


def is_hod(user):
    return user.groups.filter(name='HOD').exists()


def is_officer(user):
    return user.groups.filter(name='OFFICER').exists()


def is_reporter(user):
    return user.groups.filter(name='REPORTER').exists()


# -------------------------------------------------------home-starts----------------------------------------------------


def home(request):
    date = datetime.datetime.now().strftime('%A %d. %B %Y')
    reports = ReportModel.objects.filter(status=True)
    top_posts = ReportModel.objects.filter(status=True).order_by('-counter')[:5]
    content = {
        'date': date,
        'reports': reports,
        'top_posts': top_posts,
    }
    return render(request, 'App_main/home.html', context=content)


def report_view(request, pk):
    report = ReportModel.objects.get(id=pk)
    if report.reporter != request.user:
        report.counter += 1
        report.save()
    content = {
        'report': report,
    }
    return render(request, 'App_main/report_view.html', context=content)


def categories(request):
    reports = ReportModel.objects.filter(status=True)
    cts = ReportModel.objects.filter(status=True).values_list('category')
    cts = list(set(cts))
    cats = []
    for i in cts:
        cats.append(i[0])
    content = {
        'cats': cats,
        'reports': reports,
    }
    return render(request, 'App_main/cats.html', context=content)


# -------------------------------------------------------home-ends------------------------------------------------------

# --------------------------------------------------------hod-starts----------------------------------------------------

@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def hod_dashboard(request):
    date = datetime.datetime.now().strftime('%A %d. %B %Y')
    profile = HeadOfDepartmentModel.objects.get(user=request.user)
    hods = HeadOfDepartmentModel.objects.all().count()
    officers = OfficerModel.objects.all().count()
    reporters = ReporterModel.objects.all().count()
    report_count = ReportModel.objects.filter(assigned=False).count()
    content = {
        'profile': profile,
        'date': date,
        'hods': hods,
        'officers': officers,
        'reporters': reporters,
        'report_count': report_count,
    }
    return render(request, 'hod/dashboard.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def all_hods(request):
    hods = HeadOfDepartmentModel.objects.all()
    content = {
        'hods': hods,
    }
    return render(request, 'hod/all_hods.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def all_officers(request):
    officers = OfficerModel.objects.all()
    content = {
        'officers': officers,
    }
    return render(request, 'hod/all_officers.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def all_reporters(request):
    reporters = ReporterModel.objects.all()
    content = {
        'reporters': reporters,
    }
    return render(request, 'hod/all_reporters.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def disable_hod(request, pk):
    hod = HeadOfDepartmentModel.objects.get(id=pk)
    hod.status = False
    hod.save()
    return HttpResponseRedirect(reverse('App_main:all-hods'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def activate_hod(request, pk):
    hod = HeadOfDepartmentModel.objects.get(id=pk)
    hod.status = True
    hod.save()
    return HttpResponseRedirect(reverse('App_main:all-hods'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def disable_officer(request, pk):
    officer = OfficerModel.objects.get(id=pk)
    officer.status = False
    officer.save()
    return HttpResponseRedirect(reverse('App_main:all-officers'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def activate_officer(request, pk):
    officer = OfficerModel.objects.get(id=pk)
    officer.status = True
    officer.save()
    return HttpResponseRedirect(reverse('App_main:all-officers'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def disable_reporter(request, pk):
    reporter = ReporterModel.objects.get(id=pk)
    reporter.status = False
    reporter.save()
    return HttpResponseRedirect(reverse('App_main:all-reporters'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def activate_reporter(request, pk):
    reporter = ReporterModel.objects.get(id=pk)
    reporter.status = True
    reporter.save()
    return HttpResponseRedirect(reverse('App_main:all-reporters'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def assign_report(request):
    reports = ReportModel.objects.filter(assigned=False).order_by('created_on')
    report_count = reports.count()
    form = AssignForm()
    content = {
        'reports': reports,
        'report_count': report_count,
        'form': form,
    }
    return render(request, 'hod/assign_report.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def assign(request, pk):
    report = ReportModel.objects.get(id=pk)
    if request.method == 'POST':
        officer_id = request.POST.get('assigned_to')
        officer = OfficerModel.objects.get(id=officer_id)
        hod = HeadOfDepartmentModel.objects.get(user=request.user)
        model = AssignModel(report=report, assigned_by=hod, assigned_to=officer, status=True)
        model.save()
        report.assigned = True
        report.save()
        return HttpResponseRedirect(reverse('App_main:assign-report'))
    return HttpResponseRedirect(reverse('App_main:assign-report'))


@login_required(login_url='App_login:login')
@user_passes_test(is_hod)
def assigned_reports(request):
    reports = AssignModel.objects.filter(assigned_by__user=request.user)
    content = {
        'reports': reports,
    }
    return render(request, 'hod/assigned_report.html', context=content)


# --------------------------------------------------------hod-ends------------------------------------------------------
# -----------------------------------------------------officer-starts---------------------------------------------------

@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def officer_dashboard(request):
    date = datetime.datetime.now().strftime('%A %d. %B %Y')
    profile = OfficerModel.objects.get(user=request.user)
    currently_assigned = AssignModel.objects.filter(assigned_to__user=request.user, report__status=False,
                                                    report__rejected=False).count()
    all_assigned = AssignModel.objects.filter(assigned_to__user=request.user).count()
    rejected_ones = AssignModel.objects.filter(assigned_to__user=request.user, report__status=False,
                                               report__rejected=True).count()
    content = {
        'profile': profile,
        'date': date,
        'currently_assigned': currently_assigned,
        'all_assigned': all_assigned,
        'rejected_ones': rejected_ones,
    }
    return render(request, 'officer/dashboard.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def reports_to_check(request):
    currently_assigned = AssignModel.objects.filter(assigned_to__user=request.user, report__status=False,
                                                    report__rejected=False)
    content = {
        'reports': currently_assigned,
    }
    return render(request, 'officer/reports_to_check.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def check_a_report(request, pk):
    report = ReportModel.objects.get(id=pk)
    profile = OfficerModel.objects.get(user=request.user)
    content = {
        'report': report,
        'profile': profile,
    }
    return render(request, 'officer/check_a_report.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def change_cat(request, pk):
    report = ReportModel.objects.get(id=pk)
    if request.method == 'POST':
        prev = report.category
        current = request.POST.get('new_cat')
        print(current)
        report.category = current
        report.pre_cat = prev
        report.save()
    return HttpResponseRedirect(reverse('App_main:check-a-report', kwargs={'pk': pk}))


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def approve(request, pk):
    publisher = OfficerModel.objects.get(user=request.user)
    report = ReportModel.objects.get(id=pk)
    report.status = True
    report.rejected = False
    report.published_by = publisher
    report.save()
    return HttpResponseRedirect(reverse('App_main:check-reports'))


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def reject(request, pk):
    report = ReportModel.objects.get(id=pk)
    report.status = False
    report.rejected = True
    report.save()
    return HttpResponseRedirect(reverse('App_main:check-reports'))


@login_required(login_url='App_login:login')
@user_passes_test(is_officer)
def all_assigned_reports(request):
    all_assigned = AssignModel.objects.filter(assigned_to__user=request.user)
    content = {
        'reports': all_assigned,
    }
    return render(request, 'officer/all_reports.html', context=content)


# ------------------------------------------------------officer-ends----------------------------------------------------
# -----------------------------------------------------reporter-starts--------------------------------------------------


@login_required(login_url='App_login:login')
@user_passes_test(is_reporter)
def reporter_dashboard(request):
    date = datetime.datetime.now().strftime('%A %d. %B %Y')
    profile = ReporterModel.objects.get(user=request.user)
    content = {
        'profile': profile,
        'date': date,
    }
    return render(request, 'reporter/dashboard.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_reporter)
def new_report(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        report_model = ReportModel(title=title, reporter=request.user, category=category, loc_of_occurrence=location,
                                   report_image1=image1, report_image2=image2, report_image3=image3,
                                   report_text=description)
        report_model.save()
        return HttpResponseRedirect(reverse('App_main:reporter-dashboard'))
    return render(request, 'reporter/new_report.html')


@login_required(login_url='App_login:login')
@user_passes_test(is_reporter)
def approved_reports(request):
    reports = AssignModel.objects.filter(report__status=True, report__reporter=request.user)
    content = {
        'reports': reports
    }
    return render(request, 'reporter/approved_report.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_reporter)
def pending_reports(request):
    reports = ReportModel.objects.filter(status=False, reporter=request.user, rejected=False)
    content = {
        'reports': reports
    }
    return render(request, 'reporter/pending_report.html', context=content)


@login_required(login_url='App_login:login')
@user_passes_test(is_reporter)
def rejected_reports(request):
    reports = ReportModel.objects.filter(reporter=request.user, rejected=True)
    content = {
        'reports': reports
    }
    return render(request, 'reporter/rejected_report.html', context=content)

# ------------------------------------------------------reporter-ends---------------------------------------------------
