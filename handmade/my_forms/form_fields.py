from django import forms


class SlugUpdateField(forms.CharField):

    def validate(self, value):
        pass
