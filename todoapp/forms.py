from django import forms
from . import models


class TodoForm(forms.ModelForm):

    class Meta:
        model = models.Todo
        fields = ("title", "content")
