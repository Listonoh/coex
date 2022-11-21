from django.urls import  path
from polls.views import RandomGeneratorFormView, AdvanceRandomGeneratorFormView, ResultsView, ResultView

urlpatterns = [
    path('', RandomGeneratorFormView.as_view(), name='random_generator_form'),
    path('generate/', RandomGeneratorFormView.as_view(), name='generate'),
    path('advance/', AdvanceRandomGeneratorFormView.as_view(), name='advance'),
    path('results/', ResultsView.as_view(), name='results'),
    path('results/<int:pk>/', ResultView.as_view(), name='detail'),
]
