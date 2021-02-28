from django import forms
from .models  import *

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['resume']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work_Experience
        fields = '__all__'
        exclude = ['resume']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['resume']