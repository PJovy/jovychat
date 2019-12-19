from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            next = request.POST.get('next', '')
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return redirect('blog:articles')
            else:
                return HttpResponse('You made a mistake about login info, please input again.')
        else:
            return HttpResponse('Username or password is invalid.')
    elif request.method == 'GET':
        next = request.GET.get('next', '')
        user_login_form = UserLoginForm()
        context = {'form': user_login_form, 'next': next}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('Please use GET or POST to request.')


@login_required(login_url='userprofile:login')
def user_logout(request):
    logout(request)
    return redirect('blog:articles')


@login_required(login_url='userprofile:login')
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('blog:home')
        else:
            return HttpResponse('Register form info occured errors.')
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse('Please use POST or GET method.')


@login_required(login_url='/userprofile/login')
def user_delete(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('blog:articles')
        else:
            return HttpResponse("You don't have the permission.")
    else:
        return HttpResponse("Only receive POST method.")
