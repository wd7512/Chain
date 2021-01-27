from django.shortcuts import render, redirect
from .forms import init_form
from .models import user_form
from .models import *
from django.contrib import messages
from django.utils import timezone
from .forms import OrderForm


# Create your views here.
def signupform(request):
    if request.user.init_form_complete == 1:  # if form is complete, never go back, otherwise we keep making copies for the same user
        return redirect('promoter_dashboard')
    if request.user.type_client == 'C':
        return redirect('company_init_form')
    form = init_form(request.POST or None)
    if form.is_valid():
        email = request.user.email
        insta_id = form.cleaned_data.get("ig_name")
        sex = form.cleaned_data.get("sex")
        birthday = form.cleaned_data.get("birthday")
        submission_date = timezone.now()
        followers = form.cleaned_data.get("followers")
        dataline = user_form(email=email,
                             instagram_id=insta_id,
                             submission_date=submission_date,
                             sex=sex,
                             birthday=birthday,
                             followers=followers)
        request.user.init_form_complete = 1
        request.user.save()
        dataline.save()
        return redirect('promoter_dashboard')
    return render(request, "plain_form.html", {"form": form})


def dashboard(request):
    email = request.user.email
    row = user_form.objects.all().filter(email=email).values_list()
    id = row[0][0]  # id
    theemail = row[0][1]  # email
    instagram_id = row[0][2]  # instagram_id
    sex = row[0][3]  # sex
    submission_date = row[0][4]  # submission_date
    birthday = row[0][5]  # birthday
    followers = row[0][6]  # followers
    return render(request, "dashboardpromoter.html", {'email': theemail,
                                                      'all': list(row),
                                                      'instagram_id': instagram_id,
                                                      'sex': sex,
                                                      'submission_date': submission_date,
                                                      'birthday': birthday,
                                                      'followers': followers})



def home(request):
    b = Product(name='Product2',
                price=50,
                category='Indoor',
                description='---',
                date_created=models.DateTimeField(auto_now_add=True, null=True),
                )
    c = Customer(name='Name',
                 phone='+44 7493417301',
                 email='joao@gmail',
                 date_created=models.DateTimeField(auto_now_add=True, null=True))
    # b.save()
    # c.save()
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
