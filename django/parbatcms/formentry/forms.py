from django.forms import ModelForm, DateTimeInput, HiddenInput, Textarea
from personal.models import *

class PersonalForm(ModelForm):
    def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
       return super(PersonalForm, self).__init__(*args, **kwargs)

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
            'creator' : Textarea(attrs={'disabled':'True'}),
        }


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

class GeoForm(ModelForm):
    class Meta:
        model = GeoCode
        fields = '__all__'

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = '__all__'

class RelationForm(ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'
