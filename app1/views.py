from django.shortcuts import render,redirect

from .models import Products,Cart,Checkout,Contact

from django.contrib.auth.models import User

from .forms import CheckoutForm,ContactForm



from django.db.models import Q

# Create your views here.


def count_(request):
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.filter(host=request.user).count()
    return count


def home(request):

    categorylinks = []

    c = Products.objects.all()
    for i in c:
        if i.category not in categorylinks:
            categorylinks+=[i.category]

    all = []
    off = ''
    norec = ''

    if request.method == 'GET':
        if 'cat' in request.GET:
            print(request.GET['cat'])
            cat = request.GET['cat']
            all = Products.objects.filter(category=cat)

        elif 'trending' in request.GET:
            all = Products.objects.filter(trending=1)

        elif 'offer' in request.GET:
            off = 'OFFER - flat 50% off -'
            all = Products.objects.filter(offer=1)

        elif 'q' in request.GET:
            q = request.GET['q']
            all = Products.objects.filter(Q(category__icontains=q)|Q(name__icontains=q)|Q(desc__icontains=q))
            if len(all) == 0:
                norec = 'no record found'

        else:
            all = Products.objects.all()

        context = {
            'all':all,'categorylinks':categorylinks,'off':off,'norec':norec,'count':count_(request)
        }


    return render(request,'home.html',context)


def cart(request):

    c = Cart.objects.filter(host=request.user)


    totalamount = 0

    for i in c:
        totalamount+=i.totalprice



    noitem = False
    if len(c) == 0:
        noitem=True

    context = {
        'c':c,'noitem':noitem,'totalamount':totalamount,'count':count_(request)
    }


    return render(request,'cart.html',context)


def addcart(request,id):

    if request.user.is_authenticated:

        p = Products.objects.get(id=id)

        try:
            c = Cart.objects.get(name=p.name,host=request.user)
            c.quantity+=1
            c.totalprice+=p.price
            c.save()

        except:
            Cart.objects.create(
            category=p.category,
            name = p.name,
            desc = p.desc,
            price = p.price,
            quantity = 1,
            totalprice = p.price,
            host = request.user
            )
        return redirect('home')
    else:
        return redirect('login_')

def remove(request,id):
    c = Cart.objects.get(id=id)
    c.delete()
    return redirect('cart')


def checkout(request):
    if request.method == 'POST':
        c = CheckoutForm(data=request.POST)
        if c.is_valid():
            c.save()
            return render(request,'placeorder.html')
    return render(request,'checkout.html',{'CheckoutForm':CheckoutForm})




def profile(request):
    return render(request,'profile.html')


def eprofile(request,id):

    u = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        print(username,email)
        u.username = username
        u.email = email
        u.save()
        return redirect('login_')

    return render(request,'eprofile.html')



def upassword(request,id):
    u = User.objects.get(id=id)
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        print(old_password,new_password)
        u.password=new_password
        u.save()
        return render(request,'updatedpass.html')

    return render(request,'upassword.html')



def dprofile(request):
    return render(request,'dprofile.html')


def ddelete(request,id):
    d = User.objects.get(id=id)
    d.delete()
    print('profile deleted')
    return redirect('home')


def aboutus(request):
    return render(request,'aboutus.html')


def contactus(request):

    if request.method == 'POST':
        c = ContactForm(data=request.POST)
        if c.is_valid():
            c.save()
            return render(request,'contactr.html')

    return render(request,'contactus.html',{'ContactForm':ContactForm})
