from django import forms

from .models import Subject, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "subject", "due_date"]
        widgets = {
            # input type="date" gives you a calendar picker in the browser
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
