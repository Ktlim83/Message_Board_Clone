from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    # Meta takes in the attributes of the model
    class Meta:
        model = Post
        fields = '__all__'