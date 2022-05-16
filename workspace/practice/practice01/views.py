from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index( request );
    #return render('연결이 완료되었습니다')
return HttpResponse('연결 완료')
