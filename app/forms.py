from parler.forms import TranslatableModelForm, TranslatedField

from .models import Blog


class BlogForm(TranslatableModelForm):
    title = TranslatedField()
    description = TranslatedField()

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'description', 'image', 'region', 'category','hashtag')

    # Form for admin panel
