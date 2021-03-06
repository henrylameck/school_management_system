from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDescipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('staff_name', models.CharField(max_length=200, verbose_name='Staff Name')),
                ('designation', models.CharField(max_length=200, verbose_name='Designation')),
                ('description', models.TextField()),
                ('description_date', models.DateField(verbose_name='Descripton Date')),
                ('action_taken', models.CharField(choices=[('', 'please select'), ('parental_involvement', 'Parental Involvement'), ('guadance_and_counselling', 'Guadance And Counselling'), ('suspension', 'Suspension'), ('dismissal', 'Dismissal'), ('others', 'Others')], max_length=50, verbose_name='Action Taken')),
                ('from_date', models.DateField(verbose_name='From Date')),
                ('to_date', models.DateField(verbose_name='To Date')),
                ('fine_amount', models.DecimalField(decimal_places=0, max_digits=6)),
                ('staff_in_charge', models.CharField(max_length=50, verbose_name='Staff In Charge')),
                ('paid_fine_amount', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
<<<<<<< HEAD
=======
            name='Teacher',
=======
>>>>>>> 9052dd70c6da001c44cbcdecfc191b215575636d
            name='TeacherAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(default=True, verbose_name='Date')),
                ('type', models.CharField(choices=[('', 'Please select'), ('all', 'All'), ('designations', 'Designations')], max_length=50, verbose_name='Attendance Type')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('attendance_hours', models.CharField(choices=[('', 'Please select'), ('am', 'AM'), ('pm', 'PM'), ('full_day', 'Full_Day')], max_length=10, verbose_name='Attendance Hours Type')),
                ('description', models.TextField()),
                ('leave_category', models.CharField(choices=[('', 'Please select'), ('first_half', 'First_Half'), ('second_half', 'Second_Half')], max_length=50, verbose_name='Leave Category')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRegistration',
<<<<<<< HEAD
=======
            name='Teacher',
>>>>>>> 558c88de9323bb2971b7dc80fe7a05abfd6f0701
=======
>>>>>>> 81d4e00e47cda4ae6df18e8008f9e8256e1b5a26
>>>>>>> 9052dd70c6da001c44cbcdecfc191b215575636d
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('employee_name', models.CharField(max_length=200, verbose_name='Employee Name')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('postal_code', models.CharField(max_length=50, verbose_name='Postal Code')),
                ('country', django_countries.fields.CountryField(default='TZ', max_length=2, verbose_name='Country')),
                ('nationality', django_countries.fields.CountryField(default='TZ', max_length=2, verbose_name='Nationality')),
                ('gender', models.CharField(choices=[('', 'Please select'), ('male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Gender')),
                ('joining_date', models.DateTimeField(default=True, verbose_name='Date')),
                ('mobile_number', models.CharField(max_length=20, verbose_name='Mobile Number')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('job_type', models.CharField(choices=[('', 'Please select'), ('permanent', 'Permanent'), ('temporary', 'Temporary'), ('contract_work', 'Contract Work'), ('guest', 'Guest')], max_length=50, verbose_name='Job Type')),
                ('emp_type', models.CharField(choices=[('', 'Please select'), ('teaching_staff', 'Teaching Staff'), ('non_teaching_staff', 'Non Teaching Staff')], max_length=50, verbose_name='Employee Type')),
                ('designations', models.CharField(max_length=50, verbose_name='Designations')),
                ('termination_date', models.DateField(verbose_name='Termination Date')),
            ],
        ),
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9052dd70c6da001c44cbcdecfc191b215575636d
        migrations.CreateModel(
            name='TeacherAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(default=True, verbose_name='Date')),
                ('type', models.CharField(choices=[('', 'Please select'), ('all', 'All'), ('designations', 'Designations')], max_length=50, verbose_name='Attendance Type')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('attendance_hours', models.CharField(choices=[('', 'Please select'), ('am', 'AM'), ('pm', 'PM'), ('full_day', 'Full_Day')], max_length=10, verbose_name='Attendance Hours Type')),
                ('description', models.TextField()),
                ('leave_category', models.CharField(choices=[('', 'Please select'), ('first_half', 'First_Half'), ('second_half', 'Second_Half')], max_length=50, verbose_name='Leave Category')),
            ],
        ),
<<<<<<< HEAD
>>>>>>> 558c88de9323bb2971b7dc80fe7a05abfd6f0701
=======
=======
>>>>>>> 81d4e00e47cda4ae6df18e8008f9e8256e1b5a26
>>>>>>> 9052dd70c6da001c44cbcdecfc191b215575636d
    ]
