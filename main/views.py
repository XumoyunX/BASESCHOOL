from django.shortcuts import render
from main.models import *



def index(request):
    subject = Subject.objects.all().order_by('-id')[:3]
    practical = Practical.objects.all().order_by('-id')[:3]
    presentation = Presentation.objects.all().order_by('-id')[:3]
    video = Video.objects.all().order_by('-id')[:3]
    independent = Independent.objects.all().order_by('-id')[:3]
    ctxx = {
        "subject": subject,
        'practical': practical,
        'presentation': presentation,
        "video": video,
        'independent': independent
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
