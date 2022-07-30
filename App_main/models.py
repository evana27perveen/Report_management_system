from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from App_login.models import HeadOfDepartmentModel, OfficerModel


class ReportModel(models.Model):
    title = models.CharField(max_length=500)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='this_reporter')
    published_by = models.ForeignKey(OfficerModel, on_delete=models.CASCADE, related_name='this_officer', blank=True,
                                     null=True)
    category = models.CharField(max_length=200)
    pre_cat = models.CharField(max_length=200, default='Same')
    loc_of_occurrence = models.CharField(max_length=300)
    report_image1 = models.ImageField(upload_to='report_images', blank=True, null=True)
    report_image2 = models.ImageField(upload_to='report_images', blank=True, null=True)
    report_image3 = models.ImageField(upload_to='report_images', blank=True, null=True)
    report_text = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    counter = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def str(self):
        return f"{self.title}-{self.status}"


class ReportViewModel(models.Model):
    report = models.ForeignKey(ReportModel, on_delete=models.CASCADE, related_name='viewed_report')
    counter = models.PositiveIntegerField(default=0)

    def str(self):
        return f"{self.report.title}-{self.counter}"


class AssignModel(models.Model):
    report = models.ForeignKey(ReportModel, on_delete=models.CASCADE, related_name='report_to_check')
    assigned_by = models.ForeignKey(HeadOfDepartmentModel, on_delete=models.CASCADE, related_name='assigner_hod')
    assigned_to = models.ForeignKey(OfficerModel, on_delete=models.CASCADE, related_name='assigned_officer')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
