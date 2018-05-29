from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required

from .designforms import *
from django.http import Http404
from formentry.submodals.formGenerator import *
from postform.models import *

@login_required(login_url='users:login')
def mainforms(request,form_id, member, mark, marker):
    the_form = formValue.objects.get(id=form_id)
    tables = headings.objects.filter(formID=the_form).order_by('-weight')
    formquestions = []
    try:
        filled = formEntries.objects.filter(form=the_form, member=member).values()
        # filledids = [d['formfield'] for d in filled] Not Necessary
    except formEntries.DoesNotExist:
        filled = []

    # Building an array of fields
    for table in tables:
        table_questions = (questions.objects.filter(tableID = table)).order_by('-weight')
        table_questions_list = []
        values_list = []
        entryids = []

        for one_question in table_questions:
            #find the entry item
            mysearch = next((item for item in filled if item["formfield_id"] == one_question.id), {'id': '', 'formfield_id': '', 'answers': '', 'member': '', 'form_id': ''})
            if mysearch['id']:
                from pprint import pprint
                # pprint(mysearch)

                marks = MarkValues.objects.filter(valueid = mysearch['id'])

                # pprint(marks)

            # mark_gained =
            # Find index for the found id from filled array
            # Find the answers from the indexed array to load to values_list
            ###
            # people = [
            # {'name': "Tom", 'age': 10},
            # {'name': "Mark", 'age': 5},
            # {'name': "Pam", 'age': 7}
            # ]
            #
            # filter(lambda person: person['name'] == 'Pam', people)
            # result (returned as a list in Python 2):
            #
            # [{'age': 7, 'name': 'Pam'}]
            ###

            if one_question.choicequestion:
                queschoices = QuestionChoice.objects.filter ( questionID = one_question.choicequestion ).order_by('-weight')
            else:
                queschoices = QuestionChoice.objects.filter (questionID = one_question).order_by('-weight')
            quesAndchoice = dict(zip(
                ['question', 'choice', 'answer', 'entryid', 'marks'],
                [one_question, queschoices, mysearch['answers'], mysearch['id'], marks]
            ))
            table_questions_list.append(quesAndchoice)
        formquestions.append(dict(zip(
            ['table', 'table_questions'],
            [table, table_questions_list]
        )))
    # else:
    #     # Things need to get messy hereself.
    #     # Blank fields are absent
    #     # Only the filled up forms are available in filled
    #     a = 2
    # var = []
    # for i in range (1, the_form.markers + 1):
        # var = var.append('mark' + str(i))
    no_of_markings = the_form.markers
    formmarkers = range(int(the_form.markers))
    nameofmarkers = dict(zip(formmarkers,['आफैँ','वडाको कर्मचारी']))
    return render(request, 'base_forms/displayform.html',{
        'form':the_form, 'formquestions': formquestions, 'marktype':mark, 'marker':marker, 'member':member, 'mark':no_of_markings,
        'formmarkers':formmarkers, 'nameofmarkers':nameofmarkers,
    })



@login_required(login_url='users:login')
def all_my_forms(request):
    allforms = formValue.objects.all()

    formtitle = 'सम्पुर्ण फारमहरु'
    formdescription = 'यस लिस्टमा तपाइँका सबै फारमहरू उपलब्ध छन्'
    return render(request,'base_forms/allforms.html',{
        'allforms':allforms, 'member':0, 'mark':0, 'marker':0 ,
        'formtitle':formtitle, 'formdescription':formdescription,
    })

@login_required(login_url='users:login')
def all_member_forms(request,member,memtype):
    allforms = formValue.objects.filter(formType=memtype)

    formtitle = 'फारमहरु - परिवार, घर र व्यक्ति सम्बन्धित'
    formtype = {1:'घरसँग सम्बन्धित', 2:'परिवार सम्बन्धित', 3: 'व्यक्ति सम्बन्धित'}
    formdescription = formtype[memtype]
    return render(request,'base_forms/allforms.html',{
        'allforms':allforms, 'member':member, 'mark':1, 'marker':request.user.id,
        'formtitle':formtitle, 'formdescription':formdescription,
    })


login_required(login_url='users:login')
def index(request):
    myforms = formValue.objects.all()
    newLink = '/forms/design/'+'0/main/'
    formtitle = 'सम्पुर्ण फारमहरु'
    formdescription = 'यस लिस्टमा तपाइँका सबै फारमहरू उपलब्ध छन्'
    return render(request,'base_forms/list.html',{
        'new': newLink, 'list':myforms, 'form_type':'form',
        'formtitle':formtitle, 'formdescription':formdescription,
    })

login_required(login_url='users:login')
def formindex(request,id):
    if id!=0:
        forminstance = formValue.objects.get(id=id)
        savedform = forminstance
        #next url addition
        nextPage = '/forms/design/' + str(id) + '/table/'
    else:
        forminstance = None
        nextPage = None
    form = mainForm(request.POST or None, instance=forminstance)
    if form.is_valid():
        savedform = form.save()
        id= savedform.id
    url = '/forms/design/' + str(id) +'/main/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage})

login_required(login_url='users:login')
def tableindex(request,id):
    try:
        tables = headings.objects.filter(formID=id)
    except headings.DoesNotExist:
        redirect(request,'formentry:submit_tableindex',tid=0, formid=id)
    newLink = '/forms/design/'+str(id)+'/form/0/mytable'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':tables, 'formid':id, 'tab_type':'table'})

login_required(login_url='users:login')
def submit_tableindex(request,tid,formid):
    id=tid
    mainform = formValue.objects.get(id=formid)
    if id==0:
        try:
            table = headings.objects.get(id=tid)
        except headings.DoesNotExist:
            table = headings(formID=mainform)
    else:
        table = headings.objects.get(id=tid)
    form = tableForm(request.POST or None, instance=table)
    if form.is_valid():
        saved_table = form.save()
        return redirect('formentry:submit_tableindex', formid=mainform.id, tid=saved_table.id)
    url = '/forms/design/' + str(formid) +'/form/'+ str(id) + '/mytable/'
    nextPage = '/forms/design/' + str(id) + '/question'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage, 'tab_type': 'table'})

login_required(login_url='users:login')
def questionindex(request,id):
    try:
        tables = questions.objects.filter(tableID=id).order_by('weight')
    except questions.DoesNotExist:
        redirect(request,'formentry:submit_questionindex',qid=0, tid=id)
    newLink = '/forms/design/'+str(id)+'/table/0/myquestion'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':tables, 'tid':id, 'ques_type': 'question' })

login_required(login_url='users:login')
def submit_questionindex(request,tid,qid):
    newLink = '/forms/design/'+str(tid)+'/table/0/myquestion/'
    #copied from submit_tableindex mainform: maintable, table:question, saved_table: saved_question
    id=qid
    mainform = headings.objects.get(id=tid)
    if id==0:
        try:
            table = questions.objects.get(id=qid)
        except questions.DoesNotExist:
            table = questions(tableID=mainform)
    else:
        table = questions.objects.get(id=qid)
    form = questionForm(request.POST or None, instance=table)
    if form.is_valid():
        saved_table = form.save()
        return redirect('formentry:submit_questionindex', tid=mainform.id, qid=saved_table.id)
    url = '/forms/design/' + str(tid) +'/table/'+ str(id) + '/myquestion/'
    nextPage = '/forms/design/' + str(id) + '/choice'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage, 'new':newLink})

login_required(login_url='users:login')
def choiceindex(request,id):
    try:
        myquestion = questions.objects.get(id=id)
        choices = QuestionChoice.objects.filter(questionID=id).order_by('weight')
    except QuestionChoice.DoesNotExist:
        redirect(request,'formentry:submit_choiceindex',cid=0, qid=id)
    newLink = '/forms/design/'+str(id)+'/question/0/mychoice'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':choices, 'qid':id, 'choice_type': 'choice' })

login_required(login_url='users:login')
def submit_choiceindex(request,cid,qid):
    newLink = '/forms/design/'+str(qid)+'/question/0/mychoice/'
    id=cid
    mainform = questions.objects.get(id=qid)
    if id==0:
        try:
            choice = QuestionChoice.objects.get(id=id)
        except QuestionChoice.DoesNotExist:
            choice = QuestionChoice(questionID=mainform)
    else:
        choice = QuestionChoice.objects.get(id=id)
    form = choiceForm(request.POST or None, instance=choice)
    if form.is_valid():
        saved_choice = form.save()
        return redirect('formentry:submit_choiceindex', qid=mainform.id, cid=saved_choice.id)
    url = '/forms/design/' + str(qid) +'/question/'+ str(id) + '/mychoice/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'new':newLink})

@login_required(login_url='users:login')
def designform(request,form_id=0):
    if form_id==0:
        return render(request, 'base_forms/base.html')


def deleteforms(request,form_id, member, mark, marker):
    the_form = formValue.objects.get(id=form_id)
    tables = headings.objects.filter(formID=the_form)
    formquestions = []
    request.session['delurl'] = request.path
    # Building an array of fields
    for table in tables:
        table_questions = (questions.objects.filter(tableID = table))
        table_questions_list = []
        for one_question in table_questions:
            queschoices = QuestionChoice.objects.filter(questionID = one_question)
            quesAndchoice = dict(zip(
                ['question', 'choice'],
                [one_question, queschoices]
            ))
            table_questions_list.append(quesAndchoice)
        formquestions.append(dict(zip(
            ['table', 'table_questions'],
            [table, table_questions_list]
        )))
    # var = []
    # for i in range (1, the_form.markers + 1):
        # var = var.append('mark' + str(i))
    no_of_markings = the_form.markers
    return render(request, 'base_forms/deleteform.html',{
        'form':the_form, 'formquestions': formquestions, 'marktype':mark, 'marker':marker, 'member':member, 'mark':no_of_markings,

    })

def delete_my_forms(request):
    allforms = formValue.objects.all()

    formtitle = 'सम्पुर्ण फारमहरु'
    formdescription = 'यस लिस्टमा तपाइँका सबै फारमहरू उपलब्ध छन्'
    return render(request,'base_forms/listdeleteforms.html',{
        'allforms':allforms, 'member':0, 'mark':0, 'marker':0 ,
        'formtitle':formtitle, 'formdescription':formdescription,
    })

def printforms(request,form_id, member, mark, marker):
    the_form = formValue.objects.get(id=form_id)
    tables = headings.objects.filter(formID=the_form)
    formquestions = []
    request.session['delurl'] = request.path
    # Building an array of fields
    for table in tables:
        table_questions = (questions.objects.filter(tableID = table))
        table_questions_list = []
        for one_question in table_questions:
            queschoices = QuestionChoice.objects.filter(questionID = one_question)
            quesAndchoice = dict(zip(
                ['question', 'choice'],
                [one_question, queschoices]
            ))
            table_questions_list.append(quesAndchoice)
        formquestions.append(dict(zip(
            ['table', 'table_questions'],
            [table, table_questions_list]
        )))
    # var = []
    # for i in range (1, the_form.markers + 1):
        # var = var.append('mark' + str(i))
    no_of_markings = the_form.markers
    return render(request, 'base_forms/print_form.html',{
        'form':the_form, 'formquestions': formquestions, 'marktype':mark, 'marker':marker, 'member':member, 'mark':no_of_markings,

    })

def print_my_forms(request):
    allforms = formValue.objects.all()

    formtitle = 'सम्पुर्ण फारमहरु'
    formdescription = 'यस लिस्टमा तपाइँका सबै फारमहरू उपलब्ध छन्'
    return render(request,'base_forms/listprintforms.html',{
        'allforms':allforms, 'member':0, 'mark':0, 'marker':0 ,
        'formtitle':formtitle, 'formdescription':formdescription,
    })

def deleteEntry(request, id, del_type):
    link = request.session['delurl']
    if del_type == 1:
        a = formValue.objects.get(pk=id)
        a.delete()
    elif del_type == 2:
        a = headings.objects.get(pk=id)
        a.delete()
    elif del_type == 3:
        a = questions.objects.get(pk=id)
        a.delete()
    elif del_type == 4:
        a = QuestionChoice.objects.get(pk=id)
        a.delete()
    return redirect(link)
