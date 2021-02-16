# from django.http import HttpResponse
#
#
# def about(request):
#     return HttpResponse('Hi bro')
#
# def index(request):
#     return HttpResponse('салам э брат!!!')

from django.shortcuts import render
def view_dishes(request):
    return render(request, 'index.html',{'numbers':[123,1,2,3],'letters':1})