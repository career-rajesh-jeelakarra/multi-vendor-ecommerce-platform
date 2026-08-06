from django.shortcuts import render
from .models import User

def register(request):

    if request.method == "POST":
        print("POST Request Received")

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            user = User.objects.create_user(
                username=email,
                first_name=fullname,
                email=email,
                password=password,
                role=User.CUSTOMER
            )

            print("User Registered Successfully")

        else:
            print("Passwords do not match")

    return render(request, "accounts/register.html")