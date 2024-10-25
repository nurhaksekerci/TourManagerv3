from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime, date

class Job(models.Model):
    JOB_CHOICES = [
        ('software_engineer', 'Software Engineer'),
        ('frontend_developer', 'Frontend Developer'),
        ('backend_developer', 'Backend Developer'),
        ('full_stack_developer', 'Full Stack Developer'),
        ('test_engineer', 'Test Engineer'),
        ('data_analyst', 'Data Analyst'),
        ('data_scientist', 'Data Scientist'),
        ('system_administrator', 'System Administrator'),
        ('product_manager', 'Product Manager'),
        ('project_manager', 'Project Manager'),
        ('ux_designer', 'UX Designer'),
        ('ui_designer', 'UI Designer'),
        ('devops_engineer', 'DevOps Engineer'),
        ('solutions_architect', 'Solutions Architect'),
        ('cybersecurity_specialist', 'Cybersecurity Specialist'),
        ('technical_support', 'Technical Support'),
        ('customer_representative', 'Customer Representative'),
    ]

    title = models.CharField(max_length=50, choices=JOB_CHOICES)

    def __str__(self):
        return self.get_title_display()

class Daphne(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    jobs = models.ManyToManyField(Job, verbose_name=("Job Titles"))
    phone = models.CharField(verbose_name=("Phone"), max_length=50)

    def __str__(self):
        return f"{self.user.username} - {', '.join(job.title for job in self.jobs.all())}"

class Shift(models.Model):
    daphne = models.ForeignKey(Daphne, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def duration(self):
        return timedelta(hours=self.end_time.hour, minutes=self.end_time.minute) - timedelta(hours=self.start_time.hour, minutes=self.start_time.minute)

    def __str__(self):
        return f"{self.daphne.user.username} - {self.date} {self.start_time} - {self.end_time}"


