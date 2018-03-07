from django.shortcuts import render
from .models import writer,book

# Create your views here.

def listWriters(request):
    writerList = writer.objects.all()
    return render(request, 'writerList.html',{'writer_list': writerList})

def writerDetails(request,writer_id):
    writerDetails = writer.objects.get(pk=writer_id)
    return render(request,'writerDetails.html',{'details':writerDetails})
