from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from baseschool.settings import BASE_DIR
from django.http import FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Test, Question, UserTest



def index(request):
    subject = Subject.objects.all()[:3]
    practical = Practical.objects.all()[:3]
    presentation = Presentation.objects.all()[:3]
    video = Video.objects.all()[:3]
    independent = Independent.objects.all()[:3]
   
    ctxx = {
        "subject": subject,
        'practical': practical,
        'presentation': presentation,
        "video": video,
        'independent': independent,
      
    }
    return render(request, 'main/index.html', ctxx)






def subject(request):

    subjects = Subject.objects.all()

    ctx = {
        "subjects": subjects
    }
    return  render(request, "main/maruza.html", ctx)


def practical(request):
    practical = Practical.objects.all()

    ctx = {
        "practical": practical
    }
    return render(request, "main/amaliy.html", ctx)







def independent(request):
    independent = Independent.objects.all()

    ctx = {
        "independent": independent
    }
    return render(request, "main/mustaqil.html", ctx)



def presentation(request):
    presentation = Presentation.objects.all()

    ctx = {
        "presentation": presentation
    }
    
    return render(request, "main/taqdimot.html", ctx)



def video(request):
    video = Video.objects.all()

    ctx = {
        "video": video
    }

    return render(request, "main/videodars.html", ctx)





# def venue_pdf(request, pk):
#     vanue = Subject.objects.get(pk=pk)

#     absolute_url = str(BASE_DIR) + vanue.pdf.url
#     with open(absolute_url, 'rb') as pdf:
#         response = HttpResponse(pdf.read(), content_type="application/pdf")
#         response['Content-Disposition'] = "attachment; filename" + vanue.pdf.name
#         return render(request, 'main/index.html', {'vanue': vanue})




def pdf(request):
    return render(request, "main/test.html")




@login_required
def test_list(request):
    tests = Test.objects.all()
    return render(request, 'main/test_list.html', {'tests': tests})





@login_required
def start_test(request, id):
    test = get_object_or_404(Test, id=id)
    questions = test.questions.all()
    return render(request, 'main/test.html', {'test': test, 'questions': questions})



@login_required
def submit_test(request, id):
    test = get_object_or_404(Test, id=id)
    questions = test.questions.all()
    
    score = 0

    for question in questions:
        answer_id = request.POST.get(str(question.id))
        if answer_id:
            answer = question.answers.get(id=answer_id)
            if answer.is_correct:
                score += 1

    user_test, created = UserTest.objects.get_or_create(user=request.user, test=test)
    user_test.score = score
    # user_test.completed_at = timezone.now()
    user_test.save()

    return render(request, 'main/test_result.html', {'test': test, 'score': score})