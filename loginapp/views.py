from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import asdf
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        check = asdf.objects.filter(yourid=request.POST['yourid'])
        if len(check)>0:
            return render(request, 'signup.html', {'message':'이미 아이디가 존재합니다.'})
        
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['yourid'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            a = asdf(yourid=request.POST['yourid'], name = request.POST['username'],school=request.POST['school'], gender=request.POST['gender'], birth=request.POST['birth'], 
            hobby=request.POST['hobby'], mbti=request.POST['mbti'], img = request.FILES['img'], kakao = request.POST['kakao'])
            a.save()
            return redirect('home')

    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            request.session['islogin'] = True
            return redirect('home')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    request.session.clear()
    return redirect('home')
    
def home(request):
    return render(request, 'home.html')

def userlist(request):
    ulist = asdf.objects.all()
    print(ulist)
    ulist = str(ulist)
    ulist = ulist.split()
    arr = []
    check = 0
    for ary in ulist:
        if check == 1:
            arr.append(ary)
        for char in ary:
            if char == ':':
                check = 1
            elif char == '>':
                tmp = ""
                for x in ary:
                    if x == '>':
                        break
                    tmp += x
                check = 0
                arr.pop()
                arr.append(tmp)
                break

    useridarr = []
    namearr = []
    schoolarr = []
    genderarr = []
    birtharr = []
    hobbyarr = []
    mbtiarr = []
    imgarr = []
    kakaoarr = []
    

    kk = []
    for i in range(len(arr)):
        if i%9 == 0:
            useridarr.append(arr[i])
        if i%9 == 1:
            namearr.append(arr[i])
        if i%9 == 2:
            schoolarr.append(arr[i])
        if i%9 == 3:
            genderarr.append(arr[i])
        if i%9 == 4:
            birtharr.append(arr[i])
        if i%9 == 5:
            hobbyarr.append(arr[i])
        if i%9 == 6:
            mbtiarr.append(arr[i])
        if i%9 == 7:
            imgarr.append(arr[i])
        if i%9 == 8:
            kakaoarr.append(arr[i])
            
    for i in range(int(len(arr)/9)):
        data = dict(id = useridarr[i], name = namearr[i], school = schoolarr[i], gender = genderarr[i], birth = birtharr[i], 
        hobby = hobbyarr[i], mbti = mbtiarr[i], img=imgarr[i], kakao = kakaoarr[i])
        kk.append(data)
        
        
    print(kk)

    return render(request, 'ulist.html',{'data':kk})

def search(request):
    aaa = asdf.objects.all()

    q = request.POST.get('q', "") 

    if q:
        aaa = aaa.filter(school__icontains=q)
        return render(request, 'search.html', {'aaa' : aaa, 'q' : q})
    
    else:
        return render(request, 'search.html')