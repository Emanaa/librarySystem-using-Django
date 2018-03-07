from django.shortcuts import render
from .models import Writer,Book

# Create your views here.

def listWriters(request):
    writerList = Writer.objects.all()
    return render(request, 'writerList.html',{'writer_list': writerList})

def writerDetails(request,writer_id):
    writerDetails = Writer.objects.get(pk=writer_id)
    return render(request,'writerDetails.html',{'details':writerDetails})
