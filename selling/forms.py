from django import forms
from .models import Post

# Note: Form only for testing purposes
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "seller_name",
            "price",
            "phone",
            "De_Neve",
            "Feast",
            "Bplate",
            "Covel",


        ]