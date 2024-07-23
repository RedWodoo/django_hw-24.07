from django.forms import ModelForm

from .models import Rebenok


class BbForm(ModelForm):
    class Meta:
        model = Rebenok
        fields = ('title', 'content', 'roditel')
