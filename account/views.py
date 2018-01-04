from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.admin.views.decorators import user_passes_test
from django.views.generic import UpdateView

from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm


User = get_user_model()

def check_admin(user):
    print(user.is_superuser)
    return user.is_superuser


def home_view(request):
    return render(request,'home.html',{})


def login_view(request):
    title="login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/")
    return render(request, "form.html", {"form":form, "title":title})


def logout_view(request):
    logout(request)
    return redirect("/")


def register_view(request):
    print("register")
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        return redirect("/")
    context ={
        "form":form,
        "title": title,
    }
    return render(request, "form.html", context)


def member_leave_view(request,pk):
    instance = get_object_or_404(User, pk=pk)
    instance.delete()
    return redirect("/")


@user_passes_test(check_admin)
def admin_member_list_view(request):
    qs = User.objects.all()
    print(qs)
    return render(request,"home.html",{"member_list":qs})


def member_list_view(request):
    qs = User.objects.all()
    print(qs)
    return render(request,"home.html",{"member_list":qs})


class UserUpdateView(UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'form.html'
    success_url="/"


def member_detail_view(request, pk):
    instance = get_object_or_404(User, pk=pk)
    return render (request, "detail.html",{'instance':instance})


class OnlyAdminUserUpdateView(UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'form.html'
    success_url="/"

    def get(self, request, *args, **kwargs):
        print(type(self.request.user))
        if str(self.request.user) != 'admin':
            return render (request, "error.html",{})
        else:
            return HttpResponse("<h1>hello<h1>")