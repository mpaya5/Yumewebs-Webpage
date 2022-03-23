from django.shortcuts import render, get_object_or_404
from .models import Work

# Create your views here.
def portfolio(request):
    works = Work.objects.all()
    return render(request, "portfolio/portfolio.html", {'work':work})

def work(request, work_id):
    work = get_object_or_404(Work, id=work_id)

    works = Work.objects.all()

    return render(request, "portfolio/sample.html", {'work':work})