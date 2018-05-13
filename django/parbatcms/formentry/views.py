from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required

from .forms import *
from django.http import Http404


# Create your views here.
@login_required(login_url='users:login')
def index(request):
    #2 template = loader.get_template('polls/index.html')
    context = {

    }
    return render(request, 'design/index.html', context)
    #2 return HttpResponse(template.render(context, request))

@login_required(login_url='users:login')
def entry(request, person=0,house=None):
    if person!=0:
        my_person = Personal.objects.get(pk = int(person))
        form = PersonalForm(request.POST or None, instance=my_person)
    else:
        form = PersonalForm(request.POST or None)
    if form.is_valid():
        person_saved = form.save()
        return redirect('formentry:people_status', status=1)
    return render(request, 'design/forms.html',{'form':form, 'user':request.user, 'personid':person, 'houseid':house})

@login_required(login_url='users:login')
def address_entry(request,id,pt):
    try:
        my_person = Address.objects.get(person=id, addr_type=pt)
        form = AddressForm(request.POST or None, instance=my_person)
    except Address.DoesNotExist:
        form = AddressForm(request.POST or None)

    if form.is_valid():
        person_saved = form.save()
        return redirect('formentry:personid', person=id)
    return render(request, 'entry_forms/address.html',{'form':form, 'addressType':pt, 'person': id})

@login_required(login_url='users:login')
def card_entry(request,id,card):
    try:
        my_card = Nagrikta.objects.get(person=id, card_type=card)
        form = NagriktaForm(request.POST or None, instance=my_card)
    except Nagrikta.DoesNotExist:
        form = NagriktaForm(request.POST or None)

    if form.is_valid():
        card_saved =form.save()
        return redirect('formentry:personid', person=id)
    return render(request, 'entry_forms/card.html',{'form':form, 'cardType':card, 'person':id})

@login_required(login_url='users:login')
def contact_entry(request,id,contact):
    try:
        my_contact = Contact.objects.get(person=id, contact_type=contact)
        form = ContactForm(request.POST or None, instance=my_contact)
    except Contact.DoesNotExist:
        form = ContactForm(request.POST or None)

    if form.is_valid():
        contact_saved =form.save()
        return redirect('formentry:personid', person=id)
    return render(request, 'entry_forms/contact.html',{'form':form, 'contactType':contact, 'person':id})

@login_required(login_url='users:login')
def social_entry(request,id,media):
    try:
        my_Media = Media.objects.get(person=id, Media_type=media)
        form = MediaForm(request.POST or None, instance=my_Media)
    except Media.DoesNotExist:
        form = MediaForm(request.POST or None)

    if form.is_valid():
        Media_saved =form.save()
        return redirect('formentry:personid', person=id)
    return render(request, 'entry_forms/media.html',{'form':form, 'MediaType':media, 'person':id})

@login_required(login_url='users:login')
def hobby_entry(request,id):
    try:
        my_Hobby = Hobby.objects.get(person=id)
        form = HobbyForm(request.POST or None, instance=my_Hobby)
    except Hobby.DoesNotExist:
        form = HobbyForm(request.POST or None)

    if form.is_valid():
        Hobby_saved =form.save()
        return redirect('formentry:personid', person=id)
    return render(request, 'entry_forms/hobby.html',{'form':form, 'person':id})

@login_required(login_url='users:login')
def all_people(request, status=0):
    a = Personal.objects.all()
    if status==1:
        status_name = "Saved"
    else:
        status_name = None
    return render(request, 'design/all.html', {'user':request.user,  'status':status_name, 'all':a})


@login_required(login_url='users:login')
def geo_entry(request, id=0):
    if id !=0 :
        my_geo = GeoCode.objects.get(pk=int(id))
        form = GeoForm(request.POST or None, instance=my_geo)
    else:
        form = GeoForm(request.POST or None)
    if form.is_valid():
        geo_saved = form.save()
        return redirect('formentry:house_entry',geo=geo_saved.id, pid=0)
    return render (request,'entry_forms/geo.html',{'form':form, 'geoid':id})

@login_required(login_url='users:login')
def house_entry(request,geo=0, pid=0 ):
    coordinate = GeoCode(pk=geo)
    try:
        my_house = House.objects.get(coordinates=coordinate)
        form = HouseForm(request.POST or None, instance=my_house)
    except House.DoesNotExist:
        if pid ==0:
            return redirect('formentry:family_details', house=0,  fid=0, geo=geo, pid=0)
        owner = Family(id=pid)
        my_house = House(coordinates=coordinate, owner=owner)
        form = HouseForm(request.POST or None, instance=my_house)
    add_others = True
    if form.is_valid():
        house_saved = form.save()
        return redirect('formentry:family_list', geo=geo)
    return render (request, 'entry_forms/house.html', {'form':form, 'personid':pid, 'geoid':geo, 'add_others':add_others})

@login_required(login_url='users:login')
def family_entry(request, house=0, fid=0, geo=0, pid=0):
    #fid = family head
    #pid = family person... if fid doesn't exist pid becomes main head
    if fid==0:
        return redirect('formentry:house_head', coordinates=geo, pid=0)
    try:
        family_head = Personal(pk=fid)
        my_family = Family.objects.get(person_head=family_head)
        form = FamilyForm(request.POST or None, instance=my_family)
    except Family.DoesNotExist:
        family_head = Personal(id=fid)
        my_family = Family(person_head=family_head, myhouse=GeoCode(id=geo))
        form = FamilyForm(request.POST or None, instance=my_family)
    try:
        house_families = Family.objects.filter(myhouse=house)
    except:
        house_families = None
    if form.is_valid():
        family_saved =form.save()
        if house==0:
            return redirect ('formentry:house_entry', geo=geo, pid=family_saved.id)
        else:
            return redirect('formentry:family_details', house=house, fid=fid, geo=geo, pid=pid)
    return render(request, 'entry_forms/family.html',{'form':form, 'families':house_families, 'geo':geo, 'house':house, 'pid':pid, 'fid':fid})

@login_required(login_url='users:login')
def house_head_entry(request,coordinates=0, pid=0):
    if pid != 0:
        my_person = Personal.objects.get(pk = int(pid))
        form = PersonalForm(request.POST or None, instance=my_person)
    else:
        form = PersonalForm(request.POST or None)
    if form.is_valid():
        person_saved = form.save()
        return redirect('formentry:house_head', coordinates=coordinates, pid=person_saved.id)
    return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'personid':pid, 'geo':coordinates, 'form_next':'house'})

@login_required(login_url='users:login')
def family_list(request, geo):
    GeoObject = GeoCode.objects.get(pk=geo)
    ListofFamilies = Family.objects.filter(myhouse=GeoObject)
    return render(request, 'entry_forms/family_list.html',{'families':ListofFamilies, 'geo':geo})


@login_required(login_url='users:login')
def member_list(request, family_id):
    my_family = Family.objects.get(pk=family_id)
    try:
        ListofMembers = Relation.objects.filter(family=my_family)
    except Relation.DoesNotExist:
        ListofMembers = {}
    return render(request, 'entry_forms/family_member_list.html',{'members':ListofMembers, 'mooli':my_family.id })

@login_required(login_url='users:login')
def relation_entry(request,mooli=0,child=0, entry=0):
    try:
        mool_family = Family.objects.get(id=mooli)
        family_child = Personal.objects.get(id=child)
        if entry==0:
            form = PersonalForm(request.POST or None, instance=family_child)
            return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'child':child, 'mooli':mooli, 'flag':'relation', 'personid':child })
    except Personal.DoesNotExist:
        form = PersonalForm(request.POST or None)
        if form.is_valid():
            # New Entry of PersonalForm
            # form = PersonForm(request.POST or None)
            saved_entry = form.save()
            return redirect('formentry:relation', mooli=mooli, child=saved_entry.id, entry=0)
        return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'mooli':mooli, 'child':child, 'flag':'relation' })
    try:
        my_relation = Relation.objects.get(family=mool_family, person2=family_child)
        form = FamilyForm(request.POST or None, instance=my_relation)
    except Relation.DoesNotExist:
        my_relation = Relation(family=mool_family, person2 =family_child)
        form = RelationForm(request.POST or None, instance=my_relation)
    if form.is_valid():
        relation_saved = form.save()
        return redirect('formentry:relation', mooli=mooli,  child=child, entry=2)
    return render(request, 'entry_forms/relation.html',{'form':form, 'mooli':mooli, 'child':child, 'entry':2})
