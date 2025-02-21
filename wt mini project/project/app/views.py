from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
# Create your views here.


@csrf_exempt
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        user = authenticate(
            username=request.POST['userName'], password=request.POST['password'])
        if user:
            login(request,user)
            # print('alskdfddddddddddddddddddddddddddddddddd',User.objects.get(username=request.POST['userName']).username)
            return render(request, 'index.html',{"name": str(User.objects.get(username=request.POST['userName']).username)})
        return render(request, 'login.html', {'message': 'user not registered'})


def logout_user(request):
    logout(request)
    return render(request, 'login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'], password=request.POST['password'], is_staff=True)
        return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'register.html')


def product(request):
    return render(request,'product.html')
def about(request):
    return render(request,'about.html')
def index(request):
    current_user=request.user
    user_id=current_user.id
    user_name=current_user.username
    # print(user_id)
    print('ddddddddddddddddddddddddddddd',request.user.username)
    context={'user_id':user_id,
             'user_name':user_name,
             'name': str(request.user.username)}
    return render(request,'index.html',context)
def login1(request):
    return render(request,'login.html')
def msg(request):
    return render(request,'msg.html')
def laptop(request):
    return render(request,'laptop.html')
def shirts(request):
    return render(request,'shirts.html')
def pants(request):
    return render(request,'pants.html')
def watches(request):
    return render(request,'watches.html')
def mobile(request):
    return render(request,'mobile.html')
def cart(request):
    return render(request,'cart.html')