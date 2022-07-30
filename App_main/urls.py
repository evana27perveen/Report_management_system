from django.urls import path
from . import views

app_name = 'App_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('report-view/<int:pk>/', views.report_view, name='report-view'),
    path('categories/', views.categories, name='categories'),

    # -------------------------------------------------- public --------------------------------------------------------
    # ---------------------------------------------------- HOD ---------------------------------------------------------

    path('hod-dashboard/', views.hod_dashboard, name='hod-dashboard'),
    path('all-hods/', views.all_hods, name='all-hods'),
    path('all-officers/', views.all_officers, name='all-officers'),
    path('all-reporters/', views.all_reporters, name='all-reporters'),
    path('activate-hod/<int:pk>', views.activate_hod, name='activate-hod'),
    path('disable-hod/<int:pk>', views.disable_hod, name='disable-hod'),
    path('activate-officer/<int:pk>', views.activate_officer, name='activate-officer'),
    path('disable-officer/<int:pk>', views.disable_officer, name='disable-officer'),
    path('activate-reporter/<int:pk>', views.activate_reporter, name='activate-reporter'),
    path('disable-reporter/<int:pk>/', views.disable_reporter, name='disable-reporter'),
    path('assign-report/', views.assign_report, name='assign-report'),
    path('assign/<int:pk>/', views.assign, name='assign'),
    path('assigned-report/', views.assigned_reports, name='assigned-report'),

    # ------------------------------------------------ reporter --------------------------------------------------------

    path('reporter-dashboard/', views.reporter_dashboard, name='reporter-dashboard'),
    path('new-report/', views.new_report, name='new-report'),
    path('approved-report/', views.approved_reports, name='approved-report'),
    path('pending-report/', views.pending_reports, name='pending-report'),
    path('rejected-report/', views.rejected_reports, name='rejected-report'),

    # ------------------------------------------------ officer ---------------------------------------------------------
    path('officer-dashboard/', views.officer_dashboard, name='officer-dashboard'),
    path('all-assigned-reports/', views.all_assigned_reports, name='all-assigned-reports'),
    path('check-reports/', views.reports_to_check, name='check-reports'),
    path('check-a-report/<int:pk>/', views.check_a_report, name='check-a-report'),
    path('change-cat/<int:pk>/', views.change_cat, name='change-cat'),
    path('approve/<int:pk>/', views.approve, name='approve'),
    path('reject/<int:pk>/', views.reject, name='reject'),

]
