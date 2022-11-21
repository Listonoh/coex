from polls.forms import RandomGeneratorForm, AdvanceRandomGeneratorForm
from django.views.generic import CreateView, ListView, DetailView

from polls.models import RandomGenerator


class RandomGeneratorFormView(CreateView):
    template_name = 'random_generator_form.html'
    form_class = RandomGeneratorForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return f'/results/{self.object.pk}/'

class AdvanceRandomGeneratorFormView(RandomGeneratorFormView):
    template_name = 'advance_random_generator_form.html'
    form_class = AdvanceRandomGeneratorForm


class ResultsView(ListView):
    model = RandomGenerator
    template_name = 'results.html'
    context_object_name = 'results'
    paginate_by = 5
    ordering = ['-timestamp']


class ResultView(DetailView):
    model = RandomGenerator
    template_name = 'result.html'
    context_object_name = 'result'