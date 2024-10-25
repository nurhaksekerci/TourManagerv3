from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='City Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']


class District(models.Model):
    name = models.CharField(max_length=100, verbose_name='District Name')
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.city.name}"

    class Meta:
        ordering = ['name']


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, verbose_name='Neighborhood Name')
    district = models.ForeignKey(District, related_name='neighborhoods', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.district.name}"

    class Meta:
        ordering = ['name']


class SalesAgent(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=126)
    city = models.ForeignKey(City, verbose_name=("City"), related_name='sales_agents', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name=("District"), related_name='sales_agents', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), related_name='sales_agents', on_delete=models.CASCADE)
    address = models.TextField(verbose_name=("Address"))
    number_of_sales = models.PositiveIntegerField(verbose_name=("Number of Sales"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.neighborhood.name}, {self.district.name}, {self.city.name}"


class SalesAgentDoc(models.Model):
    sales_agent = models.ForeignKey(SalesAgent, verbose_name=("Sales Agent"), related_name='documents', on_delete=models.CASCADE)
    doc_name = models.CharField(verbose_name=("Doc Name"), max_length=255)
    file = models.FileField(verbose_name=("File"), upload_to="agents/", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doc_name} (Agent: {self.sales_agent.name})"


class SalesAgentUser(models.Model):
    sales_agent = models.ForeignKey(SalesAgent, verbose_name=("Sales Agent"), related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("User"), related_name='sales_agent_users', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name=("Phone"), max_length=50)
    is_manager = models.BooleanField(default=False)
    terms_read = models.BooleanField(default=False)
    kvkk_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} (Agent: {self.sales_agent.name})"


class Company(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=126)
    city = models.ForeignKey(City, verbose_name=("City"), related_name='companies', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name=("District"), related_name='companies', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), related_name='companies', on_delete=models.CASCADE)
    address = models.TextField(verbose_name=("Address"))
    complete_at = models.DateField(verbose_name=("Complete Date"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    branch = models.PositiveIntegerField(verbose_name=("Branch"), default=1)

    def __str__(self):
        return f"{self.name}, {self.neighborhood.name}, {self.district.name}, {self.city.name}"


class SalesAgentCustomer(models.Model):
    sales_agent = models.ForeignKey(SalesAgent, verbose_name=("Sales Agent"), related_name='customers', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name=("Company"), related_name='sales_agent_customers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sales_agent.name} - {self.company.name}"


class CompanyDoc(models.Model):
    company = models.ForeignKey(Company, verbose_name=("Company"), related_name='documents', on_delete=models.CASCADE)
    doc_name = models.CharField(verbose_name=("Doc Name"), max_length=255)
    file = models.FileField(verbose_name=("File"), upload_to="companies/", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doc_name} (Company: {self.company.name})"


class Branch(models.Model):
    company = models.ForeignKey(Company, verbose_name=("Company"), related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Name"), max_length=126)
    city = models.ForeignKey(City, verbose_name=("City"), related_name='branches', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name=("District"), related_name='branches', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), related_name='branches', on_delete=models.CASCADE)
    address = models.TextField(verbose_name=("Address"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.company.name}"


class Employee(models.Model):
    branch = models.ForeignKey(Branch, verbose_name=("Branch"), related_name='employees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("User"), related_name='employees', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name=("Phone"), max_length=50)
    is_manager = models.BooleanField(default=False)
    terms_read = models.BooleanField(default=False)
    kvkk_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} (Branch: {self.branch.name})"
