from django.forms import ModelForm, DateTimeInput, HiddenInput
from personal.models import *

class PersonalForm(ModelForm):
    def form_valid(self, form):
        form.instance.creator = self.request.user.username
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


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        person = kwargs.pop('person','')
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['person'] = person


class NagriktaForm(ModelForm):
    class Meta:
        model = Nagrikta
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SocialForm(ModelForm):
    class Meta:
        model = Social
        fields = '__all__'

class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'

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
