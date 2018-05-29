from django import forms
from django.forms import ModelForm, DateTimeInput, HiddenInput, Textarea, FileField
from photouploads.models import ImageUploads

class DocumentForm(forms.ModelForm):
    class Meta:
        model = ImageUploads
        fields = ('member', 'memberType', 'document',
        # 'upload_path'
        )
        widgets = {
            'member': HiddenInput(),
            'memberType':HiddenInput(),
            # 'upload_path':HiddenInput(),
            # accept="image/*" capture="camera"
            # 'document':ImageField(attrs={'accept':'image/*', 'capture':'camera'}),

        }
