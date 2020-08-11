from django import forms

class getLinkForm(forms.Form):
    Paste_Video_link = forms.CharField(max_length = 200)
    # quality = forms.ChoiceField(choices=[('360p'),('480p'),('720p'),('1080p')])