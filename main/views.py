from django.shortcuts import render
from main.models import *
from baseschool.settings import BASE_DIR
from django.http import FileResponse, HttpResponse



def index(request):
    subject = Subject.objects.all()[:3]
    practical = Practical.objects.all()[:3]
    presentation = Presentation.objects.all()[:3]
    video = Video.objects.all()[:3]
    independent = Independent.objects.all()[:3]
    pdf = Pdf.objects.all()
    ctxx = {
        "subject": subject,
        'practical': practical,
        'presentation': presentation,
        "video": video,
        'independent': independent,
        'pdf': pdf
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

def subject_pdf(request, id):
    pdf = Pdf.objects.filter(subject_id=id)
    ctx = {
        "pdf": pdf
    }

    return render(request, 'main/pdf.html', ctx)




def venue_pdf(request, pk):
    vanue = Pdf.objects.get(pk=pk)

    absolute_url = str(BASE_DIR) + vanue.pdf.url
    with open(absolute_url, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type="application/pdf")
        response['Content-Disposition'] = "attachment; filename" + vanue.pdf.name
        return response