from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def recipies(request):
    if request.method == "POST":
        data = request.POST
       
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

    
        print(recipe_description)
        print(recipe_name)
        print(recipe_image)

        Recipe.objects.create(
        recipe_image = recipe_image,
        recipe_name = recipe_name,
        recipe_description= recipe_description,
        )

        return redirect('/recipies/')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipies': queryset}
    return render(request,'recipies.html', context)

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipies/')

    context = {'recipe': queryset}
    
    return render(request,'update_recipies.html', context)    


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipies/')


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/recipies/')

    return render(request, 'login.html')

def logout_page(request):
    return('/login/')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
      
        if user.exists():
            messages.info(request, 'Username Already Taken.')
            return redirect('/register/')

        user = User.objects.create(
           first_name = first_name,
           last_name = last_name,
           username = username 
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully.')

        return redirect('/register/')


    return render(request, 'register.html')