from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Rebenok, Roditel


def index(request):
    bbs = Rebenok.objects.order_by('-published')
    roditeli = Roditel.objects.all()
    context = {'bbs': bbs, 'roditeli': roditeli}
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bbs = Rebenok.objects.filter(roditel=rubric_id)
    roditeli = Roditel.objects.all()
    current_rubric = Roditel.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rodteli': roditeli,
               'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roditeli'] = Roditel.objects.all()
        return context
