from django.shortcuts import render
from .models import Writer,Book

# Create your views here.

def listWriters(request):
    writerList = Writer.objects.all()
    return render(request, 'writerList.html',{'writer_list': writerList})
