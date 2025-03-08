from django import forms

from app_url_shortener.models import Url


class UrlModelForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = (
            'original_url',
        )
