from django.shortcuts import render,redirect,HttpResponse


from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout


# Create your views here.

def login_(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # user = authenticate(username=username,password=password)
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('username is invalid')
        if user.password == password:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('wrong credentials')



    return render(request,'login_.html')



def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        u = User.objects.create(username=username,email=email,password=password)
        return redirect('login_')

    return render(request,'register.html')


def logout_(request):
    logout(request)
    return redirect('login_')