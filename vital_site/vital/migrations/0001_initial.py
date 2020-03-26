<<<<<<< HEAD
# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-06-27 02:57
from __future__ import unicode_literals
=======
# Generated by Django 2.2.2 on 2019-06-23 23:38
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('auth', '0007_alter_validators_add_error_messages'),
=======
        ('auth', '0011_update_proxy_permissions'),
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
    ]

    operations = [
        migrations.CreateModel(
            name='VLAB_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('is_active', models.BooleanField(default=False)),
<<<<<<< HEAD
                ('activation_code', models.IntegerField(null=True)),
=======
                ('activation_code', models.CharField(max_length=50, null=True)),
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_faculty', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sftp_account', models.CharField(max_length=200, unique=True)),
                ('sftp_pass', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Allowed_Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email_suffix', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_by', models.IntegerField()),
                ('done_at', models.DateTimeField(default=datetime.datetime.now)),
                ('action', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Auto_Start_Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
            name='Available_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course_number', models.CharField(max_length=200, unique=True)),
                ('registration_code', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=10)),
                ('auto_shutdown_after', models.IntegerField(default=3)),
                ('allow_long_running_vms', models.BooleanField(default=False)),
                ('no_of_students', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PR', 'Professor'), ('TA', 'TeachingAssistant'), ('OW', 'Owner')], default='PR', max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intake_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local_Network_MAC_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_id', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Network_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('is_course_net', models.BooleanField(default=False)),
                ('has_internet_access', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Registered_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('registered_date', models.DateTimeField(default=datetime.datetime.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User_Bridge',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('created', models.BooleanField(default=False)),
=======
            name='Intake_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Bridge',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('created', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, unique=True)),
                ('session_key', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Virtual_Machine_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon_location', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Xen_Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('total_memory', models.IntegerField(default=0)),
                ('used_memory', models.IntegerField(default=0)),
                ('utilization', models.DecimalField(decimal_places=4, max_digits=5)),
                ('no_of_vms', models.IntegerField(default=0)),
                ('no_of_students', models.IntegerField(default=0)),
                ('no_of_courses', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Virtual_Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vital.Virtual_Machine_Type')),
            ],
        ),
        migrations.CreateModel(
            name='User_VM_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xen_server', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(default=0)),
                ('vnc_port', models.CharField(max_length=10)),
                ('terminal_port', models.CharField(max_length=10)),
                ('no_vnc_pid', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=50, null=True)),
                ('vm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Virtual_Machine')),
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
            ],
        ),
        migrations.CreateModel(
            name='User_Network_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('mac_id', models.CharField(max_length=50)),
                ('is_course_net', models.BooleanField(default=False)),
<<<<<<< HEAD
                ('bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.User_Bridge')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, unique=True)),
                ('session_key', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User_VM_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xen_server', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(default=0)),
                ('vnc_port', models.CharField(max_length=10)),
                ('terminal_port', models.CharField(max_length=10)),
                ('no_vnc_pid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Virtual_Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Virtual_Machine_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon_location', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Xen_Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('total_memory', models.IntegerField(default=0)),
                ('used_memory', models.IntegerField(default=0)),
                ('utilization', models.DecimalField(decimal_places=4, max_digits=5)),
                ('no_of_vms', models.IntegerField(default=0)),
                ('no_of_students', models.IntegerField(default=0)),
                ('no_of_courses', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='virtual_machine',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machine_Type'),
        ),
        migrations.AddField(
            model_name='user_vm_config',
            name='vm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machine'),
        ),
        migrations.AddField(
            model_name='user_network_configuration',
            name='vm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machine'),
        ),
        migrations.AddField(
            model_name='network_configuration',
            name='virtual_machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machine'),
        ),
        migrations.AddField(
            model_name='local_network_mac_address',
            name='network_configuration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Network_Configuration'),
        ),
        migrations.AddField(
            model_name='auto_start_resources',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Course'),
        ),
        migrations.AddField(
            model_name='vlab_user',
            name='admitted_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vital.Intake_Period'),
=======
                ('bridge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.User_Bridge')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
                ('vm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Virtual_Machine')),
            ],
        ),
        migrations.CreateModel(
            name='Registered_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('registered_date', models.DateTimeField(default=datetime.datetime.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Network_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('is_course_net', models.BooleanField(default=False)),
                ('has_internet_access', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
                ('virtual_machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Virtual_Machine')),
            ],
        ),
        migrations.CreateModel(
            name='Local_Network_MAC_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_id', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
                ('network_configuration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Network_Configuration')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PR', 'Professor'), ('TA', 'TeachingAssistant'), ('OW', 'Owner')], default='PR', max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Auto_Start_Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('type', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vital.Course')),
            ],
        ),
        migrations.AddField(
            model_name='vlab_user',
            name='admitted_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vital.Intake_Period'),
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
        ),
        migrations.AddField(
            model_name='vlab_user',
            name='department',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vital.Department'),
=======
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vital.Department'),
>>>>>>> 7f2f8b96592d27ff0fed41e387b55cef37452a96
        ),
        migrations.AddField(
            model_name='vlab_user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='vlab_user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
