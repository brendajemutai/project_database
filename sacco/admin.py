from django.contrib import admin

from sacco.models import Deposit, Customer

# Register your models here.

admin.site.site_header = 'Umoja Sacco Administration'
admin.site.site_title = 'Sacco Administration'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','gender','dob']
    search_fields = ['first_name','last_name','email']
    list_filter = ['gender']
    list_per_page = 25

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer','created_at','status','amount']
    search_fields = ['customer','status','amount']
    list_per_page = 25
    list_filter = ['status']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)

#python manage.py --help
#python manage.py createsuperuser
#admin@gmail.com
#Brenda123456

#p@1humanr,hr@gmail.com-hr_user

#localhost:8000/admin