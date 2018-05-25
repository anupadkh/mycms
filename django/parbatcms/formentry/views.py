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
    request.session['myurl'] = request.path

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
def all_people(request, status=0):
    request.session['myurl'] = request.path
    a = Personal.objects.all()
    if status==1:
        status_name = "Saved"
    else:
        status_name = None
    return render(request, 'design/all.html', {'user':request.user,  'status':status_name, 'all':a})


@login_required(login_url='users:login')
def geo_entry(request, id=0):
    request.session['myurl'] = request.path
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
    request.session['myurl'] = request.path
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
    request.session['myurl'] = request.path
    if fid==0:
        return redirect('formentry:house_head', coordinates=geo, pid=0)
    try:
        # family_head = Personal(id=fid)
        my_family = Family.objects.get(id=fid)
        # if my_family:
        #     return redirect('formentry:house_head', coordinates=geo, pid=0)
        if (request.POST or None) == None:
            return redirect('formentry:memberlist', family_id=fid)
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
    request.session['myurl'] = request.path

    if pid != 0:
        my_person = Personal.objects.get(pk = int(pid))
        form = PersonalForm(request.POST or None, instance=my_person)
    else:
        form = PersonalForm(request.POST or None, request=request)
    if form.is_valid():
        person_saved = form.save()
        return redirect('formentry:family_details', house=0, fid=person_saved.id, geo=coordinates, pid =0)

    # request.session['myurl'] = request.path
    return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'personid':pid, 'geo':coordinates, 'form_next':'house'})

@login_required(login_url='users:login')
def family_list(request, geo):
    request.session['myurl'] = request.path

    GeoObject = GeoCode.objects.get(pk=geo)
    # request.session['myurl'] = request.path
    ListofFamilies = Family.objects.filter(myhouse=GeoObject)
    return render(request, 'entry_forms/family_list.html',{'families':ListofFamilies, 'geo':geo, 'request':request})


@login_required(login_url='users:login')
def member_list(request, family_id):
    request.session['myurl'] = request.path

    my_family = Family.objects.get(pk=family_id)
    request.session['myurl'] = request.path
    head = my_family.person_head
    try:
        ListofMembers = Relation.objects.filter(family=my_family)
    except Relation.DoesNotExist:
        ListofMembers = {}
    geo = my_family.myhouse.id # To reference back to family from member_list.html
    return render(request, 'entry_forms/family_member_list.html',{'members':ListofMembers, 'mooli':my_family.id, 'geo' : geo , 'head':head })

@login_required(login_url='users:login')
def relation_entry(request,mooli=0,child=0, entry=0):
    request.session['myurl'] = request.path

    try:
        mool_family = Family.objects.get(id=mooli)
        family_child = Personal.objects.get(id=child)
        if entry==0:
            form = PersonalForm(request.POST or None, instance=family_child)
            return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'child':child, 'mooli':mooli, 'flag':'relation', 'personid':child })
    except Personal.DoesNotExist:
        form = PersonalForm(request.POST or None, request=request)
        if form.is_valid():
            # New Entry of PersonalForm
            # form = PersonForm(request.POST or None)
            saved_entry = form.save()
            return redirect('formentry:relation', mooli=mooli, child=saved_entry.id, entry=1)
        return render(request, 'entry_forms/user_forms.html',{'form':form, 'user':request.user, 'mooli':mooli, 'child':child, 'flag':'relation' })

    try:
        my_relation = Relation.objects.get(family=mool_family, person2=family_child)
        form = RelationForm(request.POST or None, instance=my_relation)
    except Relation.DoesNotExist:
        my_relation = Relation(family=mool_family, person2 =family_child)
        form = RelationForm(request.POST or None, instance=my_relation)
    if form.is_valid():
        relation_saved = form.save()
        return redirect('formentry:relation', mooli=mooli,  child=child, entry=0)
    return render(request, 'entry_forms/relation.html',{'form':form, 'mooli':mooli, 'child':child, 'entry':2})

@login_required(login_url='users:login')
def all_my_houses(request):
    request.session['myurl'] = request.path

    Houses = House.objects.all()
    # request.session['myurl'] = request.path
    HouseList = House.objects.all()
    return render(request, 'entry_forms/houselist.html',{'houses':HouseList, 'request':request})
