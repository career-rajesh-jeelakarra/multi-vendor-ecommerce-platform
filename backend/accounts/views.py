from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login as auth_login

def register(request):

    if request.method == "POST":
        print("POST Request Received")

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # check email already exists

        if User.objects.filter(username=email).exists():
            return render(request, "accounts/register.html", {
        "error": "Email already registered. Please use another email."
    })
        # Password length
        if len(password) < 8:
            return render(request, "accounts/register.html", {
        "error": "Password must be at least 8 characters."
    })
        # Uppercase check
        if not any(char.isupper() for char in password):
            return render(request, "accounts/register.html", {
        "error": "Password must contain at least one uppercase letter."
    })
         # Lowercase check
        if not any(char.islower() for char in password):
            return render(request, "accounts/register.html", {
                "error": "Password must contain at least one lowercase letter."
            })
         # Number check
        if not any(char.isdigit() for char in password):
                    return render(request, "accounts/register.html", {
                        "error": "Password must contain at least one number."
                    })
         # Special character check
        if not any(not char.isalnum() for char in password):
                    return render(request, "accounts/register.html", {
                        "error": "Password must contain at least one special character."
                    })
        # Confirm password
        if password != confirm_password:
            return render(request,"accounts/register.html",{
                  "error":"Passwords do not match."
            })
            # Create user
            user = User.objects.create_user(
                username=email,
                first_name=fullname,
                email=email,
                password=password,
                phone=phone,
                role=User.CUSTOMER
            )

        print("User Registered Successfully")
            # Go to login page
        return redirect("login")
    return render(request,"accounts/register.html")


def login(request):
      if request.method == "POST":
            print("LOGIN POST Request Recieved")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request,username=email,password=password)
            if user is not None:
                  print("Customer Authentication is Successful")
                  # Actually log the user in
                  auth_login(request,user)
                  # Temporary redirect
                  return redirect("register")
            else:
                  print("Customer Authentication Failed")
            return render(request,"accounts/login.html",
                    {
                    "error":"Invalid email or password"
                    })
      return render(request,"accounts/login.html")