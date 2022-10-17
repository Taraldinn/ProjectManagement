from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from accounts.forms import RegisterForm

from django.contrib.auth import authenticate, login, logout

User = get_user_model() # get user models

# Leader user registration view 
class LeaderRegisterTemplateView(TemplateView):
    # get method to view the page
    def get(self, request, *args, **kwargs):
        # check user authenticated
        if request.user.is_authenticated:
            # redirect to user dashboard
            return HttpResponse("Redirect to user dashboard coz user authenticated")
        else:
            form  = RegisterForm()
            # send context to template 
            context = {
                'form': form
            }
            # render template
            return render(request, 'accounts/register.html', context) # render a template with context

    # post method to handle user submited data and create user object
    def post(self, request, *args, **kwargs):
        # check if user is authenticate == True or False
        if request.user.is_authenticated:
            # if user is authenticated then user will be redirect to dashboard
            return HttpResponse("Redirect to user dashboard")
        else:
            # check again is it post method or not, (to more secure)
            if request.method == 'post' or request.method == 'POST':
                form = RegisterForm(request.POST) # pass user submited data to RegisterForm 
                if form.is_valid(): # check the submited data is valid
                    try: # inside try we gonna check user is exist == True or False
                        email = form.cleaned_data['email'] # get submited user email
                        if User.objects.get(email=email).count() > 0: # check user submited email is exist == True or False
                            messages.warning(request, "This email address already exist!") # send message to user
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
                        else:
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
                    except: # here we gonna create user object
                        instance = form.save(commit=False)# commit false given access to reasign value
                        instance.user_type = 'leader' # reaign the value
                        instance.is_active = True # now direct active user account (when verify user we gonna change it)
                        instance.save() # save those data to database
                        return redirect('accounts:login') # redirect to login page after created account
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon


# Worker user registration view 
class WorkerRegisterTemplateView(TemplateView):
    # get method to view the page
    def get(self, request, *args, **kwargs):
        # check user authenticated
        if request.user.is_authenticated:
            # redirect to user dashboard
            return HttpResponse("Redirect to user dashboard coz user authenticated")
        else:
            form  = RegisterForm()
            # send context to template 
            context = {
                'form': form
            }
            # render template
            return render(request, 'accounts/register.html', context) # render a template with context

    # post method to handle user submited data and create user object
    def post(self, request, *args, **kwargs):
        # check if user is authenticate == True or False
        if request.user.is_authenticated:
            # if user is authenticated then user will be redirect to dashboard
            return HttpResponse("Redirect to user dashboard")
        else:
            # check again is it post method or not, (to more secure)
            if request.method == 'post' or request.method == 'POST':
                form = RegisterForm(request.POST) # pass user submited data to RegisterForm 
                if form.is_valid(): # check the submited data is valid
                    try: # inside try we gonna check user is exist == True or False
                        email = form.cleaned_data['email'] # get submited user email
                        if User.objects.get(email=email).count() > 0: # check user submited email is exist == True or False
                            messages.warning(request, "This email address already exist!") # send message to user
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
                        else:
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
                    except: # here we gonna create user object
                        instance = form.save(commit=False) # commit false given access to reasign value
                        instance.user_type = 'worker'# reaign the value
                        instance.is_active = True # now direct active user account (when verify user we gonna change it)
                        instance.save()# save those data to database
                        return redirect('accounts:login') # redirect to login page after created account
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon

  
# user login template view
class LoginTemplateView(TemplateView):
    # get method to render templates
    def get(self, request, *args, **kwargs):
        # check user authentication
        if request.user.is_authenticated:
            return HttpResponse('Redirect to dashboad coz user is authenticated')
        else:
            context = {
                
            }
            return render(request, 'accounts/login.html', context)
    # post method to login users
    def post(self, request, *args, **kwargs):
        # check user authentication
        if request.user.is_authenticated:
            # redirect to user dashboard
            return HttpResponse('Redirect to dashboad coz user is authenticated')
        else:
            # check request method
            if request.method == 'post' or request.method == 'POST':
                email = request.POST.get('email') # get submited email
                password = request.POST.get('password') # get submited password
                user = authenticate(request, username=email, password=password) # authentication a user
                # check user is not none == True or False
                if user is not None:
                    login(request, user) # now login user
                    # given access by user type
                    if request.user.user_type == 'admin':
                        return HttpResponse("redirect ADMIN dashboard after login ")
                    elif request.user.user_type == 'leader':
                        return HttpResponse("redirect LEADER dashboard after login ")
                    elif request.user.user_type == 'worker':
                        return HttpResponse("redirect WORKER dashboard after login ")
                    else:
                        return HttpResponse("redirect 404 page  ")
                    return HttpResponse("redirect after login ")
                else:
                    # send a message to user
                    messages.info(request, "username or password is incorrect!")
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon
