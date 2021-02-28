from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def home(request):
    return render(request, "index.html")


# user resume
def resume(request, name):
    user_resume = Resume.objects.get(user=request.user)
    skills = Skills.objects.filter(resume=user_resume)
    works = Work_Experience.objects.filter(resume=user_resume)
    educations = Education.objects.filter(resume=user_resume)
    context = {
        "resume": user_resume,
        "skills": skills,
        "works": works,
        "educations":educations
    }
    return render(request, "resume/resume.html", context)


# edit resume page
@login_required(login_url='auth:login')
def edit_resume(request):
    form_instance = Resume.objects.get(user=request.user)
    profile_form = ProfilForm(instance=form_instance.profile)
    skill_form = SkillsForm()
    works_form = WorkForm()
    education_form = EducationForm()
    context = {
        "profile": profile_form,
        "skill": skill_form,
        "works": works_form,
        "education":education_form
    }
    return render(request, "edit.html", context)


# edit profile
def edit_profile(request):
    if request.method == "POST":
        obj = Resume.objects.get(user=request.user)
        form = ProfilForm(request.POST, instance=obj.profile)
        if form.is_valid():
            form.save()
            return redirect("resume:edit_resume")





# add skills
def add_skills(request):
    obj = Resume.objects.get(
        user=request.user,
    )
    new_skill = Skills.objects.create(
        resume=obj,
        skill_name=request.POST.get("skill_name"),
        skill_level=request.POST.get("skill_level"),
    )
    return redirect("resume:edit_resume")


# add works
def add_work(request):
    if request.method == "POST":
        obj = Resume.objects.get(
            user=request.user,
        )
        form = WorkForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.resume = obj
            r.save()
            return redirect("resume:edit_resume")


# add education
def add_education(request):
    if request.method == "POST":
        obj = Resume.objects.get(
            user=request.user,
        )
        form = EducationForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.resume = obj
            r.save()
            return redirect("resume:edit_resume")