from django import forms
from ghost_post_app.models import BoastRoast

class PostForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ['choices', 'user_input']