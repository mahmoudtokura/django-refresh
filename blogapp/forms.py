from django import forms

from blogapp.models import Blog, Category


class CreateBlogForm(forms.ModelForm):
    blog_categories = Category.objects.all()

    category = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Select a Category"},
        ),
        queryset=blog_categories,
    )
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Title"}
        ),
    )
    content = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter Content"}
        ),
    )
    thumbnail = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        required=False,
    )
    featured = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "mt-4", "type": "checkbox"}),
        required=False,
    )

    class Meta:
        model = Blog
        fields = ("category", "title", "content", "thumbnail", "featured")
