from django import forms
from .models import Experience
from .widgets import DurationPickerWidget

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['activity', 'duration', 'notes']  # Include the fields you want in the form
        widgets = {
            'duration': DurationPickerWidget(),
        }
