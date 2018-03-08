from django.shortcuts import render,redirect
from .models import writer,book
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def listWriters(request):
    writerList = writer.objects.all()
    return render(request, 'writerList.html',{'writer_list': writerList})

def writerDetails(request,writer_id):
    writerDetails = writer.objects.get(pk=writer_id)
    return render(request,'writerDetails.html',{'details':writerDetails})


def bookDetails(request,book_name):
    bookDetails = Book.objects.get(title=book_name)
    return render(request,'bookDetails.html',{'bookDetails':bookDetails})


    #signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('users_uname')
            raw_password = form.cleaned_data.get('users_password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'writerList.html',{'userName':username})#redirect('writerList')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
