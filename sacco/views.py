from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sacco.app_forms import CustomerForm
from sacco.models import Customer, Deposit


# Create your views here.
def test(request):
    #save a customer
    # c1=Customer(first_name='John', last_name='Smith',email='smith@gmail.com',
    #             dob='2001-11-28',gender="male",weight=62)
    # c1.save()
    #
    # c2 = Customer(first_name='Mary', last_name='Juma', email='maria@gmail.com',
    #               dob='2005-11-30', gender="female", weight=52)
    # c2.save()
    customer_count = Customer.objects.count()

    #fetching one customer
    c1=Customer.objects.get(id=1) # select * from customer where id=1
    print(c1)
    d1=Deposit(amount=10000,status=True, customer=c1)
    d1.save()

    deposit_count=Deposit.objects.count()
    return HttpResponse(f"Ok, Done,We have {customer_count} customers and {deposit_count} deposits")


def customers(request):
    data=Customer.objects.all() # ORM select * from customers
    return render(request,'customers.html',{'customers':data})


def delete_customer(request,customer_id):
    customer=Customer.objects.get(id=customer_id) #select * from customers where id=7
    customer.delete() #delete from customers where id=7
    return redirect(customers)


def add_customer(request):
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form=CustomerForm()
    return render(request,'customer_form.html',{'form':form})


#pip install django-crispy-forms
#pip install crispy-bootstrap5