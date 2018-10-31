# Imported Modules and Classes from User Models
# =============================================

from django.shortcuts import render, redirect
from .models import Job, User
from django.contrib import messages
from django.db import IntegrityError
# from datetime import datetime
# import bcrypt


# {% extends "useraccounts/base.html"
# ----------------------------------
# shall render homepage and displays
# all jobs into tables
# ---------------------
def dashboardView(request):
    if 'uid' in request.session:
        user = User.objects.get(pk=request.session['uid'])
        context = {
            'jobs': Job.objects.all(),
            'myjobs': user.myjobs.all()
        }
        return render(request, 'handyhelper/JobsDashboard.html', context)
    messages.add_message(request, messages.INFO, "You must be a registered user to view the intented page.", extra_tags = 'login')
    return redirect('/login')


# @instructor.dojo
# ----------------------------
# shall redirect to jobs after
# adding new Job schedule
# ------------------------
def addNewJobView(request):
    if not 'uid' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    return render(request,'handyhelper/AddJobs.html')

def addNewJobForm(request):
    errors = Job.objects.jobValidator(request.POST)
    if len(errors):
        for tag,error in errors.items():
            messages.error(request, error, extra_tags=tag)
    else:
        try:
            # user = User.objects.get(id=request.session['uid'])
            # job  = Job.objects.create(
            Job.objects.create(
	            title   = request.POST['title'],
	            desc    = request.POST['description'],
                location= request.POST['location'],
	            creator = User.objects.get(id=request.session['uid']))
            return redirect('/handyhelper')
        except IntegrityError:
            pass
    return redirect('/handyhelper/addjob')


def editJobPlanView(request, id):
    if not 'uid' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/')
    context = {'job': Job.objects.get(id=id) }
    return render(request,'handyhelper/EditJobPlan.html', context)

# < shall process user updates >
def editJobPlanrForm(request, id):
    errors = Job.objects.jobValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect('/')
    else:
        job = Job.objects.get(pk=id)
        Job.filter(pk=id).update(request.POST)
        # job.title   = request.POST['title']
        # job.desc    = request.POST['description']
        # job.creator = User.objects.get(id=request.session['uid'])
        # job.save()
        request.session['job_title'] = job.title
        request.session['job_desc']   = job.desc
        request.session['job_location'] = job.location
        request.session['job_creator'] = job.creator
    return redirect('/')


# --------------------------------------
# shall display detail info about a job
# Also does not allow anyone to proceed
# to the route unless they have logged in
# --------------------------------------
def viewJobPlans(request, id):
    if not 'uid' in request.session:
        messages.add_message(request, messages.INFO, "Sorry, only registered users hava access for this requested!", extra_tags = 'login')
        return redirect('/handyhelper')
    job = Job.objects.get(pk=id)
    context = {
        'job': job
        # 'plans': Job.objects.filter(creator=job.creator).all()
		# 'userjobs': User.objects.get(id=request.session['uid']).jobs_created.all(),
    }
    return render(request, 'handyhelper/Plans.html/', context)


# -----------------------------------
# shall handle events regarding users
# disliking events of a particular job
# --------------------------------------
def addJobEvent(request, id):
    job = Job.objects.get(id=id)
    user = User.objects.get(id=request.session['uid'])
    job.users_jobs.add(user)
    return redirect('/handyhelper')


# -----------------------------------
# shall handle events regarding users
# dropping a particular job in their list
# ---------------------------------------
def cancelJobEvent(request, id):
    job  = Job.objects.get(id=id)
    user = User.objects.get(id=request.session['uid'])
    job.users_jobs.remove(user)
    return redirect('/handyhelper')

# ------------------------------------------------
# Removes user from targeted scheduled jobs by id
# ------------------------------------------------
def deleteJobEvent(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/handyhelper')


# ------------------------------------------------------
# shall display detail all jobs posted/joinded by a user
# Also does not allow anyone to proceed
# to the route unless they have logged in
# --------------------------------------
def userJobsView(request, id):
    if not 'uid' in request.session:
        messages.add_message(request, messages.INFO, "Sorry, only registered users hava access for this requested!", extra_tags = 'login')
        return redirect('/handyhelper')
    user = User.objects.get(pk=id)
    context = {
        'created_by': user,
        'alljobs': Job.objects.filter(creator=user).all()
    }
    return render(request, 'handyhelper/UserJobs.html/', context)
