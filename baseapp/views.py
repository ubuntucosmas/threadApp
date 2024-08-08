from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Thread, Post,Topic
from .forms import ThreadForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login-page')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    context={'page':page}
    return render(request, './baseapp/login_register.html', context)
#===================================================================================================================

def logoutUser(request):
    logout(request)
    return redirect('home')

#===================================================================================================================
def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    context = {'page':page, 'form':form}
    return render(request, './baseapp/login_register.html', context)

#===================================================================================================================

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q)) # topic__name queries up to the parent(Topic Model)
    topics = Topic.objects.all()
    thread_count = threads.count()
    context = {'threads':threads,'topics':topics, 'thread_count':thread_count}
    return render(request, './baseapp/home.html',context)

#===================================================================================================================

def thread(request, pk): #pk=means we have to the value passed dynamically on the url /<str:pk>/
    threads = Thread.objects.get(id=pk)
    context = {'threads':threads}
    return render(request, './baseapp/thread.html',context)

#===================================================================================================================
@login_required       # this decorator restrict unauthenticated users from creating a thread
def createThread(request):
    form = ThreadForm()
    if request.method == 'POST':
      form = ThreadForm(request.POST, request.FILES)  # request.FILES for images
      if form.is_valid():
          form.save()
          return redirect('home')
      
    else:
        form = ThreadForm()
        context={'form':form}
    return render(request, './baseapp/thread-form.html', context)
#===================================================================================================================

@login_required
def updateThread(request,pk):
    updates = Thread.objects.get(id=pk)
    form = ThreadForm(instance=updates) #instance prefill the form with the room(updates) values
    if request.user != updates.host:
        return HttpResponse('You do not have permission to update this thread')
    if request.method == 'POST':
        form = ThreadForm(request.POST,instance=updates) #instance is specifying which room to update
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, './baseapp/thread-form.html', context)


@login_required
def delete(request,pk):
    updates = Thread.objects.get(id=pk)
    if request.user != updates.host:
        return HttpResponse('You do not have permission to update this thread')
    if request.method == 'POST':
        updates.delete()
    return redirect('home')


     
