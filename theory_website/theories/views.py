from django.shortcuts import render, get_object_or_404
from .models import Theory

def theory_list(request):
    theories = Theory.objects.all()
    return render(request, 'theory_list.html', {'theories': theories})

def theory_detail(request, pk):
    theory = get_object_or_404(Theory, pk=pk)
    return render(request, 'theory_detail.html', {'theory': theory})



