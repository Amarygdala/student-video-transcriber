from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
        labels = {
            "name": "Random Unique ID",
            "videofile":""
        }