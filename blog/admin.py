from django.contrib import admin
from .models import Post, Image
from django.contrib.auth.models import User
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update(
            {'multiple': True, 'accept': 'image/jpg,image/png,image/gif,image/jpeg', })


class PostAdmin(admin.ModelAdmin):
    form = PostForm

    def save_model(self, request, obj, form, change):
        files = request.FILES.getlist('images')
        print(files, request.POST, request.user, User.objects.get(id=request.POST['author']))
        if files:
            instance = Post.objects.create(author=User.objects.get(id=request.POST['author']), title=request.POST['title'], text=request.POST['text'], images=files[0])
            for image_field in files:
                try:
                    Image.objects.create(post=instance,  image=image_field)
                except Post.DoesNotExist:
                    pass
        # else:
        #     return super().save_model(request, obj, form, change)




admin.site.register(Post, PostAdmin)