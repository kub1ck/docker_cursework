from django import forms
from .models import File


class FileAddAndUpdateForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)
