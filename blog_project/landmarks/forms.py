from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['landmark', 'user']
    def clean(self):
        text = self.cleaned_data['text']
        file = self.cleaned_data['file']
        if not text and  not file:
            raise forms.ValidationError("You must provide a comment or upload a file.")