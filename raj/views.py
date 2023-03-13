from django.shortcuts import render

# Create your views here.
def friends(request):
    dic={'name':'Rajesh_Goriparthi','name1':'Ramesh_Sagar'}
    return render(request,'friends.html',context=dic)
