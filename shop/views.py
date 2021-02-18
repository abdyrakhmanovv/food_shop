# from django.http import HttpResponse
#
#
# def about(request):
#     return HttpResponse('Hi')
#
# def index(request):
#     return HttpResponse('салам !!!')

from django.shortcuts import render
def view_dishes(request):
    return render(request, 'index.html',{'numbers':[123,1,2,3],'letters':1})