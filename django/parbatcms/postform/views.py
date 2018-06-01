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
        form = formValue.objects.get(pk = request.POST.get('formid'))
        member = request.POST.get('member')
        # answers = request.POST.getlist('question_value[]')
        answers = []
        marks = []
        object_questions = questions.objects.filter(pk__in=myquestions)
        total_self=0
        total_ward=0
        for onequestion in object_questions:
            # pprint(onequestion.id)
            # pprint(" is Question and Answer is ")
            if onequestion.answerType == 'mc':
                # pprint(request.POST.getlist('question_value[' + str(onequestion.pk)+']'))
                ans = ",".join(str(x) for x in request.POST.getlist('question_value[' + str(onequestion.pk)+']'))
                pprint (ans)
            else:
                ans = (request.POST.get('question_value[' + str(onequestion.pk)+']'))
            if form.markers ==0:
                a=[]
            else:
                mark0 = request.POST.get('mark0['+ str(onequestion.pk)+']')
                mark1 = request.POST.get('mark1['+ str(onequestion.pk)+']')
                if mark0:
                    mark1 = 0 if (mark1=='') else mark1
                    a = [mark0, mark1]
                elif mark1:
                    mark0 = 0 if mark0 == '' else mark0
                    a = [mark0, mark1]
                else:
                    mark1 = 0
                    mark0 = 0
                    a = [mark0, mark1]
            myzip = {onequestion.pk:a}
            if a:
                somemarks = float(onequestion.marks)
                total_self += somemarks * float(mark0)/10
                total_ward += somemarks * float(mark1)/10
            marks.append(myzip)

            # pprint(ans)
            answers.append(ans)

        # pprint(marks)


        obtained = {'own':total_self, 'ward':total_ward}


        formmarkers = [{"प्रश्नकर्ता नं "+str(i),"mark"+str(i)} for i in range(form.markers)]

        # yn = {1:'Yes', 2:'No'}
        # choices = QuestionChoice.objects.filter(questionID__in=myquestion, )
        # pprint (choices)
        postquestions = list(zip(object_questions,answers))
        # pprint(str(list(zip(myquestions, answers))) + " Search Questions " + str(len(answers)) + " Answers " +str((postquestions)) + "Post questions")
        choices = []
        for ques,ans in postquestions:
            if ques.answerType == 'sc':
                try:
                    choice = QuestionChoice.objects.get(pk=ans)
                except:
                    choice = ans

            elif ques.answerType == 'yn':
                choice = {'1':'Yes, हो','2':'No, होइन'}.get(ans)
            else:
                choice = ans
            choices.append(choice)
        postqna = list(zip(object_questions, answers, choices, marks))
        # https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe#11011846
        # pprint (object_questions)
        # pprint (answers)
        return render(request, 'base_forms/mytemplate.html',{
            'field_choices':postqna, 'markers': formmarkers, 'form':form, 'member':member, 'obtained_marks':obtained
        })

def makePost(request):
    if request.POST:
        myquestions = request.POST.getlist('questions[]')
        answers = request.POST.getlist('answers[]')
        formid = request.POST.get('formid')
        member = request.POST.get('member')
        # pprint(request.POST)
        # pprint(request.POST)

        form = formValue.objects.get(pk = int(formid))
        markers = ["mark"+str(i)+"[]" for i in range(1,form.markers+1)]
        marks=[]
        for a in markers:
            marks.append(request.POST.getlist(a))
            # pprint(request.POST.getlist(a))
        qna = list(zip(myquestions,answers))
        # pprint(qna)
        # pprint(marks)
        f=0
        for idx,(q,a) in enumerate(qna):
            data = {'formfield' : q, 'answers':a, 'form' : formid, 'member':member}
            # pprint(myinstance)
            try:
                f=formEntries.objects.get(formfield=q, form=formid, member=member)
            except formEntries.MultipleObjectsReturned:
                f = formEntries.objects.filter(formfield=q, form=formid, member=member)
                # for d in f:
                #     if d == f[0]:
                #         continue
                #     else:
                #         d.delete()
                f=f[0]
            except:
                pprint("Everything is first")

            theform = EntryForm(data)
            # pprint(theform)
            if theform.is_valid():
                # pprint("Hi this is working \n")
                if f:
                    saved_entry = theform.save(commit=False)
                    saved_entry.id = f.id
                    saved_entry.save()
                else:
                    saved_entry = theform.save()

                for jdx,b in enumerate(marks):
                    # pprint(idx)
                    # pprint(b)
                    data = {'valueid' : saved_entry.id, 'marks' : b[idx], 'marker':markers[jdx]}
                    # pprint(data)
                    markform = MarksForm(data)
                    marks_saved_entries = MarkValues.objects.filter(valueid = saved_entry, marker = markers[jdx])
                    if marks_saved_entries:
                        marks_saved_entry = marks_saved_entries[0]
                    # pprint(mymarkform)
                    if markform.is_valid():
                        mymark = markform.save(commit=False)
                        if marks_saved_entries:
                            mymark.id = marks_saved_entry.id
                            mymark.save()
                        else:
                            mymark.save()


        return redirect(request.session['myurl'])
    return redirect('formentry:people')


def index(request):
    return render(request, 'design/icons.html',{})
