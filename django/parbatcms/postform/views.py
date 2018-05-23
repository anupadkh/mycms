from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Import modals for form Fields
from formentry.submodals.formGenerator import *

from postform.models import *
from postform.forms import *

#debug mode
from pprint import pprint


def seePost(request):
    # pprint(globals())
    # pprint(locals())
    if request.POST:
        myquestions = request.POST.getlist('questionID[]')
        answers = request.POST.getlist('question_value[]')
        form = formValue.objects.get(pk = request.POST.get('formid'))
        member = request.POST.get('member')

        object_questions = questions.objects.filter(pk__in=myquestions)

        formmarkers = [{"प्रश्नकर्ता नं "+str(i),"mark"+str(i)} for i in range(form.markers)]

        # yn = {1:'Yes', 2:'No'}
        # choices = QuestionChoice.objects.filter(questionID__in=myquestion, )
        # pprint (choices)
        postquestions = list(zip(object_questions,answers))
        choices = []
        for ques,ans in postquestions:
            if ques.answerType == 'sc':
                choice = QuestionChoice.objects.get(pk=ans)
            elif ques.answerType == 'yn':
                choice = {'1':'Yes, हो','2':'No, होइन'}.get(ans)
            else:
                choice = ans
            choices.append(choice)
        postqna = list(zip(object_questions, answers, choices))
        # https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe#11011846
        # pprint (object_questions)
        # pprint (answers)
        return render(request, 'base_forms/mytemplate.html',{
            'field_choices':postqna, 'markers': formmarkers, 'form':form, 'member':member,
        })

def makePost(request):
    if request.POST:
        myquestions = request.POST.getlist('questions[]')
        answers = request.POST.getlist('answers[]')
        formid = request.POST.get('formid')
        member = request.POST.get('member')
        # pprint(request.POST)

        form = formValue.objects.get(pk = int(formid))
        markers = ["mark"+str(i)+"[]" for i in range(form.markers)]
        marks=[]
        for a in markers:
            marks.append(request.POST.getlist(a))
            pprint(request.POST.getlist(a))
        qna = list(zip(myquestions,answers))
        pprint(qna)
        pprint(marks)
        for idx,(q,a) in enumerate(qna):
            data = {'formfield' : q, 'answers':a, 'form' : formid, 'member':member}
            # pprint(myinstance)
            theform = EntryForm(data)
            # pprint(theform)
            if theform.is_valid():
                # pprint("Hi this is working \n")
                saved_entry = theform.save()
                for jdx,b in enumerate(marks):
                    data = {'valueid' : saved_entry.id, 'marks' : b[idx], 'marker':markers[jdx]}
                    pprint(data)
                    markform = MarksForm(data)
                    # pprint(mymarkform)
                    if markform.is_valid():
                        markform.save()

        return redirect(request.session['myurl'])
    return redirect('formentry:people')


def index(request):
    return render(request, 'design/icons.html',{})
