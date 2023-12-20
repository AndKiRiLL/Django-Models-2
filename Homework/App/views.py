from django.shortcuts import render
from .forms import FormAdd, UserEditForm
from .models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def add(request):

    if request.method == "POST":
        email = request.POST.get('email', 'Undefined')
        password = request.POST.get('password', 'Undefined')
        login = request.POST.get('login', 'Undefined')

        User.objects.create(email=email, password=password, login=login)

        return HttpResponseRedirect('/')

    else:
        form_add = FormAdd()
        return render(request, 'add.html', {'form_add': form_add})

def delete(request):
    users = User.objects.all()
    return render(request, 'delete.html', {'users': users})

def delete_choose(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        users = User.objects.all()
        return render(request, 'delete.html', {'users': users})

    except User.DoesNotExist:
        users = User.objects.all()
        return render(request, 'delete.html', {'users': users})

def edit(request):
    users = User.objects.all()
    return render(request, 'edit.html', {'users': users})

def edit_choose(request, id):
    try:
        if request.method == "POST":
            user = User.objects.get(id=id)

            user.email = request.POST.get('email', 'Undefined')
            user.password = request.POST.get('password', 'Undefined')
            user.login = request.POST.get('login', 'Undefined')

            user.save()

            users = User.objects.all()
            return render(request, 'edit.html', context={'users': users})

        else:
            user = User.objects.get(id=id)
            form_edit = UserEditForm(instance=user)
            return render(request, 'edit_choose.html', context={'form_edit': form_edit})

    except User.DoesNotExist:
        return HttpResponseRedirect('/')