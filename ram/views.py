from django.shortcuts import render

# Create your views here.
def best_friends(request):
    d={'name2':'Ramesh','name3':'Rajesh'}
    return render(request,'friends.html',context=d)
