from django.shortcuts import render
from .models import writer,book

# Create your views here.

def listWriters(request):
    writerList = writer.objects.all()
    return render(request, 'writerList.html',{'writer_list': writerList})

def writerDetails(request,writer_id):
    writerDetails = writer.objects.get(pk=writer_id)
    return render(request,'writerDetails.html',{'details':writerDetails})

    #signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
