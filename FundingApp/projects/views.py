from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Project, Images, Categories, Comment, Donation, Rating
from .forms import ProjectForm, CommentForm, DonationForm, RatingForm
from django.contrib.auth import authenticate, login, logout
from users.models import user
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def project(request):
    id = request.user.id
    project = Project.objects.filter(user_id=id)
    comments = Comment.objects.all()
    rate = Rating.objects.all()
    dict = Donation.objects.filter(project_id=id).aggregate(sum=Sum('donation_amount'))
    donate = DonationForm()
    new_comment = None
    new_rate = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.project = project
            new_comment.save()
        rate_form = RatingForm(data=request.POST)
        if rate_form.is_valid():
            new_rate = rate_form.save(commit=False)
            new_rate.project = project
            new_rate.save()
    else:
        comment_form = CommentForm()
        rate_form = RatingForm()
    context = {'projects': project,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form,
               "total_donation": dict['sum'],
               'donate_form': donate,
               'rate': rate,
               'new_rate': new_rate,
               'rate_form': rate_form,
               }
    return render(request, 'project.html', context)


def addproject(req):
    if req.method == "POST":
        form = ProjectForm(req.POST)
        if form.is_valid():
            # email = req.session['email']
            # myuser = user.objects.get(email=email)
            # form.id = myuser.id
            # print(form.id)
            # email = req.session['email']
            # User = user.objects.get(email=email)
            form.save()
            return redirect('/project')
    else:
        form = ProjectForm()
    return render(req, 'addproject.html', {'form': form})


def cancel_project(res, id):
    if res.method == "POST":
        email = res.session['email']
        myuser = user.objects.filter(email=email)
        user_id = myuser.id
        project = Projects.objects.get(id=id, user_id=user_id)
        if not project:
            raise HttpResponseForbidden("Not Authorized")
        project.delete()
        return render(res, 'project.html', {'project': project})


def myProjects(request):
    current_user = request.user.id

    myProjects = Project.objects.filter(id=current_user).order_by('start_date')
    # preparing User Projects in One List
    myProjectsList = []
    for project in myProjects:
        print("my projects : ", myProjectsList)
        myProjectsList.append({
            'id': project.id,
            'title': project.title,
            'details': project.details,
            'target': project.target,
            'start_date': project.start_date,
        })
    return render(request, 'project.html', {'myProjects': myProjectsList})


def donate(request, id):
    session_user = request.user.id
    if request.method == 'POST':
        form = DonationForm(request.POST)
        Projectdata = Project.objects.get(id=id)

        dict = Donation.objects.filter(project_id=id).aggregate(sum=Sum('donation_amount'))
        totalDon = dict['sum']
        print(totalDon)
        inputDon = int(form.data['donation_amount'])

        if form.is_valid():

            if totalDon:
                total = inputDon + totalDon
                if total <= int(Projectdata.totalTarget):
                    donation = form.save(commit=False)
                    donation.save()
                    messages.add_message(request, messages.INFO,
                                         'Donation Added successfully, Thank you for contribution')
                else:

                    messages.add_message(request, messages.INFO, 'Invalid Donation')
            else:
                total = inputDon
                if total <= int(Projectdata.totalTarget):
                    donation = form.save(commit=False)
                    donation.user_id = get_object_or_404(User, id=session_user)
                    donation.project_id = get_object_or_404(Project, pk=id)
                    donation.save()
                    messages.add_message(request, messages.INFO,
                                         'Donation Added successfully, Thank you for contribution')
                else:
                    messages.add_message(request, messages.INFO, 'Invalid Donation')

    return redirect("/project", id=id)