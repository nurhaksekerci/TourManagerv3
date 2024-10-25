from django.contrib import admin
from .models import City, District, Neighborhood, SalesAgent, SalesAgentDoc, SalesAgentUser, Company, SalesAgentCustomer, CompanyDoc, Branch, Employee

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('city', 'is_deleted')
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('district', 'is_deleted')
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(SalesAgent)
class SalesAgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'district', 'neighborhood', 'number_of_sales', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('city', 'district', 'neighborhood', 'number_of_sales', 'is_deleted')
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(SalesAgentDoc)
class SalesAgentDocAdmin(admin.ModelAdmin):
    list_display = ('sales_agent', 'doc_name', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('doc_name',)
    list_filter = ('sales_agent', 'is_deleted')
    ordering = ['doc_name']
    list_editable = ('is_deleted',)


@admin.register(SalesAgentUser)
class SalesAgentUserAdmin(admin.ModelAdmin):
    list_display = ('sales_agent', 'user', 'phone', 'is_manager', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('user__username', 'phone')
    list_filter = ('sales_agent', 'is_manager', 'is_deleted')
    ordering = ['user']
    list_editable = ('is_deleted',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'district', 'neighborhood', 'branch', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('city', 'district', 'neighborhood', 'is_deleted')
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(SalesAgentCustomer)
class SalesAgentCustomerAdmin(admin.ModelAdmin):
    list_display = ('sales_agent', 'company', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('sales_agent__name', 'company__name')
    list_filter = ('sales_agent', 'company', 'is_deleted')
    ordering = ['sales_agent']
    list_editable = ('is_deleted',)


@admin.register(CompanyDoc)
class CompanyDocAdmin(admin.ModelAdmin):
    list_display = ('company', 'doc_name', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('doc_name',)
    list_filter = ('company', 'is_deleted')
    ordering = ['doc_name']
    list_editable = ('is_deleted',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'city', 'district', 'neighborhood', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('company', 'city', 'district', 'neighborhood', 'is_deleted')
    ordering = ['name']
    list_editable = ('is_deleted',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'phone', 'is_manager', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('user__username', 'phone')
    list_filter = ('branch', 'is_manager', 'is_deleted')
    ordering = ['user']
    list_editable = ('is_deleted',)
