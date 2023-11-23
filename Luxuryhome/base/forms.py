from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image','publish_date']

def clean_title(self, *args, **kwargs):
    instance = self.instance
    title = self.cleaned_data.get('title')        
    qs = BlogPost.objects.filter(title_iexact=title)
    if instance is not None:
        qs = qs.exclude(pk=instance.pk)
    if qs.exists():
        raise forms.ValidationError('This title has already been used. Please use another title')

class ContactForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)




    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith('.edu'):
            raise forms.ValidationError('This is not a valid email. ')
        return email