from my_app.models import students
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    students_list = students.objects.order_by('name')
    diction= {'students': students_list}
    return render(request, 'my_app/index.html', context=diction)
'''
def home(request):
    return HttpResponse("trying first, then Antu gonna help!")

def friend(request):
    return HttpResponse("I may be done by myself!")'''
