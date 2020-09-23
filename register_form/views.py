from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubmissionFormModel
from .forms import FormSubmissionModel, NewUserCreation
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse


@login_required(login_url='login')
@staff_member_required(login_url='view_data')
def register_page(request):
    form = NewUserCreation()
    if request.method == 'POST':
        form = NewUserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'successfully created a new user' + ' ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('view_data')
            else:
                messages.info(request, 'Failed to login. Check Name and Password and try again')
        context = {}
        return render(request, 'authentication/login.html', context)


def logout_page(request):
    logout(request)
    messages.success(request, 'Your data is secure and save ')
    return redirect('login')


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        phone = request.POST['phone']

        subject = name
        message = birthday + '' + email + '' + phone
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ndipdesmond247@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        form = FormSubmissionModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your form was submitted successfully')
            return redirect('home')
        else:
            # name = request.POST['name']
            # birthday = request.POST['birthday']
            # email = request.POST['email']
            # phone = request.POST['phone']

            messages.info(request, 'form was not submitted, there was an error try again ')
            # context = {
            #     name: 'name',  birthday: ' birthday',
            #     email: 'email', phone: 'phone'
            #
            # }
            return render(request, 'index.html', {})
    return render(request, 'index.html', {})


@login_required(login_url='login')
def view_data(request):
    data = SubmissionFormModel.objects.all().order_by('-id')
    count = SubmissionFormModel.objects.all().count
    return render(request, 'view_data.html', {'data': data, 'count': count})


@login_required(login_url='login')
def detail_view(request, data_id):
    get_singe_data = SubmissionFormModel.objects.get(id=data_id)
    return render(request, 'detail_view.html', {'get_singe_data': get_singe_data})


def update_data(request, up_id):
    data = SubmissionFormModel.objects.get(id=up_id)
    form = FormSubmissionModel(instance=data)
    if request.method == 'POST':
        form = FormSubmissionModel(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_data.html')
    return render(request, 'index.html', {'form': form})

# def delete_data(request, del_id):
#     data = SubmissionFormModel.objects.get(id=del_id)
#     if request.method == 'POST':
#         data.delete()
#         return redirect('view_data')
#     return render(request, 'delete.html', {})


def delete_data(request, del_id):
    data = SubmissionFormModel.objects.get(id=del_id)
    data.delete()
    return redirect('view_data')






