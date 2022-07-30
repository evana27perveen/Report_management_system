# Generated by Django 3.2.14 on 2022-07-25 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0002_auto_20220725_1039'),
        ('App_main', '0002_alter_reportmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='this_officer', to='App_login.officermodel'),
        ),
        migrations.CreateModel(
            name='AssignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigner_hod', to='App_login.headofdepartmentmodel')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_officer', to='App_login.officermodel')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_to_check', to='App_main.reportmodel')),
            ],
        ),
    ]
