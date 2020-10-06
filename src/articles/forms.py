from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Your title'
                            }))
    content = forms.TextInput()
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = ['title', 'content', 'active']