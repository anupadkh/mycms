from django.forms import ModelForm, DateTimeInput, HiddenInput
from personal.models import *

class PersonalForm(ModelForm):
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(PersonalForm, self).form_valid(form)

    class Meta:
        model = Personal
        exclude = ['gened']
        fields = '__all__'
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        field_classes = {
            # 'slug': MySlugFormField,
            'hari':'freaks', 'class':'form-control'
        }
        widgets = {
            'pub_date': DateTimeInput(attrs={'class': 'datetime-input'}),
            'creator' : HiddenInput()
        }
