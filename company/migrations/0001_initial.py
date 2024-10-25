# Generated by Django 5.1.2 on 2024-10-25 10:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='City Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='District Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='company.city', verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Company Name')),
                ('tax_number', models.CharField(max_length=50, unique=True, verbose_name='Tax Number')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('payment_plan', models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, verbose_name='Payment Plan')),
                ('subscription_end_date', models.DateField(verbose_name='Subscription End Date')),
                ('address', models.TextField(verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.city', verbose_name='City')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.district', verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Branch Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.city', verbose_name='City')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='company.company', verbose_name='Company')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.district', verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('tax_certificate', 'Tax Certificate'), ('registration_certificate', 'Registration Certificate'), ('tax_id_certificate', 'Tax ID Certificate'), ('trade_license', 'Trade License'), ('insurance_certificate', 'Insurance Certificate'), ('bank_account_document', 'Bank Account Document'), ('company_article_of_association', 'Company Article of Association'), ('business_permit', 'Business Permit'), ('environmental_license', 'Environmental License'), ('health_inspection_certificate', 'Health Inspection Certificate'), ('audit_report', 'Audit Report'), ('other', 'Other')], max_length=30, verbose_name='Document Type')),
                ('file', models.FileField(upload_to='documents/', verbose_name='File')),
                ('upload_date', models.DateField(auto_now_add=True, verbose_name='Upload Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='company.company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('is_company_authority', models.BooleanField(default=False, verbose_name='Is Company Authority')),
                ('is_branch_authority', models.BooleanField(default=False, verbose_name='Is Branch Authority')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Phone Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.branch', verbose_name='Branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('pending', 'Pending')], max_length=20, verbose_name='Status')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='company.company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Neighborhood Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='company.district', verbose_name='District')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.neighborhood', verbose_name='Neighborhood'),
        ),
        migrations.AddField(
            model_name='branch',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.neighborhood', verbose_name='Neighborhood'),
        ),
    ]
