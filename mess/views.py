from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Menupdf,Feedback
from . import classify
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def index(request):
    if request.method =='POST':
        
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        flag = 0
        if email=='' or password1=='' or password2=='' :
            
            messages.info(request,'Blank Value Passed') 
        elif User.objects.filter(email = email).exists():
            flag = 1 
            messages.info(request,'Email already exists')
            
        elif password1 != password2:
            messages.info(request,'Password Dont Match')
            return render(request ,'index.html')
                    
        if ( flag==0 and email != '' and password1 != '' and password2 != '' and (password1 == password2)):
            user = User.objects.create_user(username = email, email = email , password= password1)
            user.save()
            messages.info(request,'Successfully Registered Now you can Log in')
            print("user created")
    flag = 1
    storage = messages.get_messages(request)
    #print(len(storage))
    #del storage._loaded_messages[0]
    storage.used = True 
    storage = messages.get_messages(request)
    for message in storage:
        pass
              
    return render(request ,'index.html')


def student(request):
    if request.method=='POST' and 'fromstudent' in request.POST:
        name = request.POST.get('name')
        entry = request.POST.get('entry')
        date = request.POST.get('date')
        meal = request.POST.get('meal')
        message = request.POST.get('message')
        y = classify.prediction(str(message))
        data = y[0]
        data = int(data)
        print(data)
        dicts = {1:' High Negative' , 2:'Negative', 3:'Neutral', 4:'Positive', 5:'High Positive'}
        review = dicts[data]
        print("I am  kk here")
        feed = Feedback()
        feed.name = name
        feed.entry = entry
        feed.meal = meal
        feed.date = date
        feed.text = message
        feed.review = review
        print("User Created")
        feed.save()
        return render(request ,'student.html')
        
        
    elif request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("I am here")
        print(email)
        print(password)
        print("Here")
        val = Menupdf.objects.all()
        data = val[len(val) -1]
        
        
        passed = data.filepdf.url
        fix = data
        param = {'data':fix}
        print(passed)
        user = auth.authenticate(username = email , email = email , password = password)
        
        if email=="sugandhiaayush0203@gmail.com" and password=="123456":
            
            feed = Feedback.objects.all()
            print(feed)
            params = {'feed':feed}
            return render(request ,'adminpanel.html',params)
        
        elif user is not None:
            auth.login(request,user)
            messages.info(request,'Correct credentials')
            return render(request ,'student.html',param)
        else:
            messages.info(request,'wrong credentials')
            return render(request,'index.html')
        
    else:
        return render(request,'index.html')
def adminpanel(request):
    context ={}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('myfile')
        print(uploaded_file)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        
        context['url'] = fs.url(name)
        print('here')
        data = Menupdf()
        data.title = uploaded_file.name
        data.filepdf = uploaded_file
        data.save()
        return render(request ,'adminpanel.html')
    else:
        return render(request ,'index.html')