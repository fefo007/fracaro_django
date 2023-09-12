from django.shortcuts import render
from django.http import HttpResponse 
from .models import Staff,Users,Orders,Travel
from .forms import OrdersForm,TravelForm

def login(req):
    if req.method == 'POST':
        return render(req,'login.html')
    else:
        return render(req,'login.html')

def home(req):
    return render(req,'home.html')

def travels(req):
    if req.method == 'POST':
        form = TravelForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            travel = Travel(
                name = data['name'],
                image = data['image'],
                price = data['price'],
                time = data['time'],
                description = data['description']
                )
            travel.save()
            return render(req,'home.html')
    else:
        form = TravelForm()
        return render(req,'travels.html',{'travels_form':form})

def contact(req):
    return render(req,'contact.html')

def search(req):
    if req.GET['searchTravel']:
        search = req.GET['searchTravel']
        travel = Travel.objects.filter(name = search)
        return render(req,'search.html',{'search':travel})
    else:
        return HttpResponse(f'No se busco nada aun...')

def aboutUs(req):
    return render(req,'aboutUs.html')

def orders(req):
    if req.method == 'POST':
        form = OrdersForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Orders(
                client = data['client'],
                travel = data['travel'],
                price = data['price'],
                departure = data['departure'],
                arrival = data['arrival']
                )
            order.save()
            return render(req,'home.html')
    else:
        form = OrdersForm()
        return render(req,'orders.html',{'orders_form':form})

def user(req):
    if req.method == 'POST':
        user = Users(
            name=req.POST['name'],
            lastname=req.POST['lastname'],
            email=req.POST['email'],
            birthday=req.POST['birthday'],
            phone=req.POST['phone'],
            address=req.POST['address']
        )
        user.save()
        return render (req, 'home.html')
    else:
        return render (req, 'user.html')



