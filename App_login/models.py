from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
    "Enter a valid international mobile phone number starting with +(country code)"))

gender_choice = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Third Gender", "Third Gender"),
)

designation_choice = (
    ("Head of Department", "Head of Department"),
    ("Officer", "Officer"),
    ("Reporter", "Reporter"),
)


# Create your models here.

class HeadOfDepartmentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hod')
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Phone Number"), max_length=17,
                                    blank=False, null=False)
    gender = models.CharField(choices=gender_choice, max_length=15)
    nid = models.CharField(max_length=50, unique=True, blank=False, null=False)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(default='Head of Department', max_length=150)
    address = models.CharField(max_length=250, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='hod_picture', blank=False, null=False)
    joining_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.designation} - {self.user.first_name} {self.user.last_name}"


class OfficerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='officer')
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Phone Number"), max_length=17,
                                    blank=False, null=False)
    gender = models.CharField(choices=gender_choice, max_length=15)
    nid = models.CharField(max_length=50, unique=True, blank=False, null=False)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(default='Officer', max_length=150)
    address = models.CharField(max_length=250, blank=False, null=False)
    office_location = models.CharField(max_length=250, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='officer_picture')
    joining_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.designation} - {self.user.first_name} {self.user.last_name}"


class ReporterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Phone Number"), max_length=17,
                                    blank=False, null=False)
    designation = models.CharField(default='Reporter', max_length=150)
    gender = models.CharField(choices=gender_choice, max_length=15)
    address = models.CharField(max_length=150, blank=False, null=False)
    area = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=25, blank=False, null=False)
    zip_code = models.CharField(max_length=15, blank=False, null=False)
    country = CountryField(blank_label='(select country)', blank=False, null=False)
    profile_picture = models.ImageField(upload_to='reporter_picture')
    joining_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
