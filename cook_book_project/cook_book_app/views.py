from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Recipe_add
from django.shortcuts import render,HttpResponse,redirect

def add_recipe(request):
    if request.method == 'POST':
        obj = Recipe_add(Item_name=request.POST.get('Item_name'), Recipe=request.POST.get('Recipe'))
        obj.save()
        messages.success(request, 'Recipe added successfully!')
        return redirect('cook_book_app:view_recipes')
    return render(request, 'recipes_add.html')

def view_recipes(request):
    recipes = Recipe_add.objects.all()
    return render(request, 'recipes_view.html', {'recipes': recipes})


# def HomePage(request):
#     return render (request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('view_recipes')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

# def LogoutPage(request):
#     logout(request)
#     return redirect('login')

