from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, Mail
from django.contrib.auth import get_user_model
from .issue_request import OrderForm, MailForm
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='users-login')
def index(request):
    users_count = get_user_model().objects.all().count()
    staff_count = get_user_model().objects.filter(is_staff=True).filter(is_superuser=False).count()
    all_count = Order.objects.all().count()
    order_count = Order.objects.filter(owner=request.user).count()

    context = {
        'all_count':all_count,
        'users_count': users_count-staff_count-1,
        'staff_count': staff_count,
        'order_count': order_count,
    }
    return render(request, 'gui/index.html', context)

@login_required(login_url='users-login')
def staff(request):
    users = get_user_model().objects.all()
    users_count = get_user_model().objects.all().count()
    staffs = get_user_model().objects.filter(is_staff=True).filter(is_superuser=False)
    staff_count = get_user_model().objects.filter(is_staff=True).filter(is_superuser=False).count()
    all_count = Order.objects.all().count()
    order_count = Order.objects.filter(owner=request.user).count()

    context = {
        'all_count':all_count,
        'users': users,
        'staffs': staffs,
        'users_count': users_count-staff_count-1,
        'staff_count': staff_count,
        'order_count': order_count,
    }
    return render(request, 'gui/staff.html', context)

@login_required(login_url='users-login')
def orders(request):
    order_requests = Order.objects.all()
    users_count = get_user_model().objects.all().count()
    staff_count = get_user_model().objects.filter(is_staff=True).filter(is_superuser=False).count()
    all_count = Order.objects.all().count()
    order_count = Order.objects.filter(owner=request.user).count()
    curr = order_requests.filter(owner=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            result = form.save()
            result.owner = request.user
            result.status = "Active"
            result.save()
            return redirect('gui-orders')
    else:
        form = OrderForm()

    context = {
        'all_count':all_count,
        'curr': curr,
        'order_requests': order_requests,
        'form': form,
        'users_count': users_count-staff_count-1,
        'staff_count': staff_count,
        'order_count': order_count,
    }
    return render(request, 'gui/orders.html', context)

@login_required(login_url='users-login')
def delete_order(request, key):
    deleted_order = Order.objects.get(id=key)
    if request.method == 'POST':
        deleted_order.delete()
        return redirect('gui-orders')
    return render(request, 'gui/delete_order.html')

@login_required(login_url='users-login')
def update_order(request, key):
    updated_order = Order.objects.get(id=key)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updated_order)
        form.save()
        return redirect('gui-orders')
    else:
        form = OrderForm(instance=updated_order)

    # form.fields['ownership'].disabled = True
    context = {
        'form': form,
    }
    return render(request, 'gui/update_order.html', context)

@login_required(login_url='users-login')
def mail_order(request, key):
    mailed_order = Order.objects.get(id=key)
    email_client = mailed_order.owner.email

    if request.method == 'POST':
        form = MailForm(request.POST)
        obj = Order.objects.get(pk=mailed_order.id)
        result = form.save()
        result.take_order_id = mailed_order.id
        result.save()
        obj.status = "Taken"
        obj.save()

        send_mail("Workman Management System", 
                  "Your order is taken by {}. The handyman will visit you on {}".format(request.user, result.date_time), 
                  "lilzpp17@gmail.com",
                    [email_client])
        
        return redirect('gui-orders')
    else:
        form = MailForm()
    
    context = {
        'form': form,
        'mailed_order':mailed_order,
        'email_client':email_client,
    }
    
    return render(request, 'gui/mail_order.html',context)
