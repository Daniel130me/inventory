from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order
from django.contrib.auth.models import User
from .forms import ProductForm, OrderForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def index(request):
    order_data = Order.objects.all()
    product_data = Product.objects.all()
    product_no = product_data.count()
    staff_no = User.objects.all().count()
    my_order_list_name = []
    my_order_list_quantity = []
    for data in product_data:
        order_ch = sum(list(Order.objects.filter(product_id=data.id).values_list('quantity', flat=True)))
        if order_ch != 0:
            my_order_list_quantity.append(order_ch)
            my_order_list_name.append(data.name)
            print(f'{data.name}-{order_ch}')
    print(my_order_list_quantity,my_order_list_name)
    
    order_no = order_data.count()
    staff_no  = User.objects.all().count()
    # product_data____  = Product.objects.raw("SELECT * FROM dashboard_product WHERE category='Electronic'")
    electronic_data  = sum(list(Product.objects.filter(category='Electronic').values_list('quantity', flat=True)))
    stationary_data  = sum(list(Product.objects.filter(category='stationary').values_list('quantity', flat=True)))
    food_data  = sum(list(Product.objects.filter(category='food').values_list('quantity', flat=True)))
    product_chart = [electronic_data,stationary_data,food_data]
   
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if  form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return JsonResponse({'message':'success'})
    context = {
        'form':form,
        'order_data':order_data,
        'order_no':order_no,
        'staff_no':staff_no,
        'product_no':product_no,
        'product_chart':product_chart,
        'my_order_list_quantity':my_order_list_quantity,
        'my_order_list_name':my_order_list_name,
    }
    return render(request, 'dashboard/index.html', context)
# Create your views here.

@login_required(login_url='user-login')
def staff(request):
    staff_data = User.objects.all()
    staff_no = staff_data.count()
    product_no = Product.objects.all().count()
    order_no = Order.objects.all().count()
    context = {
        'staff_no':staff_no,
        'product_no':product_no,
        'order_no':order_no,
        'staff_data':staff_data,
    }
    return render(request, 'dashboard/staff.html', context)
# Create your views here.

@login_required(login_url='user-login')
def product(request):
    product_no = Product.objects.all().count()
    staff_no = User.objects.all().count()
    order_no = Order.objects.all().count()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
        
    context = {
        'staff_no':staff_no,
        'product_no':product_no,
        'order_no':order_no,
        'form':form
    }
    return render(request, 'dashboard/product.html', context)

def product_update(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pid = request.POST['id']
            product = Product.objects.get(id=pid)
            product.name = request.POST['name']
            product.category = request.POST['category']
            product.quantity = request.POST['quantity']
            product.save()
            return JsonResponse({'message':'success'})

def product_delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return JsonResponse({'message':'success'})

def product_details(request):
    data = Product.objects.all()
    return render(request, 'dashboard/product_details.html',{'data':data})
# Create your views here.

@login_required(login_url='user-login')
def order(request):
    order_data = Order.objects.all()
    order_no = order_data.count()
    staff_no = User.objects.all().count()
    product_no = Product.objects.all().count()
    context = {
        'staff_no':staff_no,
        'product_no':product_no,
        'order_no':order_no,
        'order_data':order_data,
    }
    return render(request, 'dashboard/order.html', context)

def staff_order_details(request):
    order_data = Order.objects.all()
    return render(request, 'dashboard/staff_order_details.html',{'order_data':order_data})
# Create your views here.

