from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import json
import os, random, string
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
from collections import Counter
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid details')
            # return redirect('login')
            return render(request, 'authentication-login1.html')
    else:
        return render(request, 'authentication-login1.html')    


def register(request):
    if request.method=="POST":
    
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=confirmpassword)
                user.save();
                print("user created!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("pasword not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'authentication-register1.html')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def is_multichoice_column(series, delimiter=","):
    threshold = 0.3
    count_with_delim = series.dropna().apply(lambda x: delimiter in str(x)).sum()
    ratio = count_with_delim / len(series.dropna()) if len(series.dropna()) > 0 else 0
    return ratio > threshold

def aggregate_multichoice_counts(responses_dict, delimiter=","):
    counter = Counter()
    for combo, count in responses_dict.items():
        options = [opt.strip() for opt in str(combo).split(delimiter)]
        for option in options:
            counter[option] += count
    return dict(counter)

@login_required(login_url='login')
def upload_excel(request):
    if request.method == "POST" and request.FILES.get("file"):
        excel_file = request.FILES["file"]

        # generate random filename
        random_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        extension = os.path.splitext(excel_file.name)[1]
        new_filename = f"{random_name}{extension}"

        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, "excel_files"))
        filepath = fs.save(new_filename, excel_file)
        full_path = fs.path(filepath)

        # --- Run analysis ---
        df = pd.read_excel(full_path)
        summary = {}
        for column in df.columns:
            if df[column].dtype == object:
                counts = df[column].value_counts().to_dict()
                if is_multichoice_column(df[column]):
                    counts = aggregate_multichoice_counts(counts)
                summary[column] = counts
        json_filename = f"{random_name}.json"
        json_path = os.path.join(settings.MEDIA_ROOT, "results", json_filename)
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, "w") as f:
            json.dump(summary, f)
        # Store result in session
        # request.session["analysis_result"] = summary
        request.session["json_file"] = json_filename
        # Redirect after completion
        return redirect("uploaded_excel")

    return render(request, "index.html")   # upload form page

@login_required(login_url='login')
def uploaded_excel(request):
    json_file = request.session.get("json_file")
    summary_json = "{}"
    if json_file:
        json_path = os.path.join(settings.MEDIA_ROOT, "results", json_file)
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                summary_json = f.read()

    print(">>> SUMMARY JSON:", summary_json)   
    return render(request, "uploaded_excel.html", {"summary_json": summary_json})

def logout(request):
    auth_logout(request)  # ✅ now calls Django’s logout
    return redirect("login")

