from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #            add message
            return redirect("login")
    form = UserRegisterForm
    return render(
        request, "users/register.html", context={"form": form, "title": "Register"}
    )
