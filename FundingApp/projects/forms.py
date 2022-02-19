from django import forms
from projects.models import Project, Images, Comment, Donation, Rating
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'title', 'category', 'details', 'totalTarget', 'startproject', 'endproject']
        widgets = {
            'startproject': DateInput(),
            'endproject': DateInput(),
        }


# class ProjectImageForm(forms.Form):
#     project_images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta:
#         model = Images
#         fields = '_all_'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content', 'project_id']


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donation_amount', 'project_id', 'user_id']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_content', 'Rating_project_id']
