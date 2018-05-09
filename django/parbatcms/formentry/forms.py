from django.forms import ModelForm
from personal.models import *

class PersonalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs.update({'class': 'form-control'})
        # self.fields['comment'].widget.attrs.update(size='40')
    class Meta:
        model = Personal
        # exclude = ['gened']
        fields = '__all__'
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        field_classes = {
            # 'slug': MySlugFormField,
            'hari':'freaks', 'class':'form-control'
        }
