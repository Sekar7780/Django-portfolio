from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': 'Amazon Clone',
            'path': 'images/amazon_img.jpg',
        },
        {
            'title': 'Gamble Gaming',
            'path': 'images/gamble_img.jpg',
        },

        {
            'title': 'sample portfolio',
            'path': 'images/personal_portfolio_img.jpg',
        },
        {
            'title': 'User Login-id',
            'path': 'images/login_img.jpg',
        },

         {
            'title': 'Sammys Mind Chirps',
            'path': 'images/sammy_img.jpg',
        },
          {
            'title': 'Django Portfolio',
            'path': 'images/django_img.png',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience (request):
    experience=[
        {
            'company':'8 Queens Software Technology',
            'position':'FullStack Development',
            'duration':'SEP-2024 to DEC-2024',

        }
    ]
    return render (request,"experience.html",{"experience":experience})

def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/T.sekar-resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content.Disposition']="attachment";filename="T.sekar-resume.pdf"
            return response
        
    else:
        return HttpResponse("resume not found", status=404)