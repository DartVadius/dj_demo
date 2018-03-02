from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    file = forms.FileInput()

    def save(self, commit=True):
        file = self.cleaned_data.get('file', None)
        # ...do something with extra_field here...
        return super(GalleryForm, self).save(commit=commit)

    class Meta:
        model = Gallery
        fields = '__all__'
