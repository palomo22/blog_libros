from django import forms
from .models import Comment, Page
from ckeditor.widgets import CKEditorWidget
class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribí tu comentario aquí...',
                'class': 'form-control'  
            })
        }
