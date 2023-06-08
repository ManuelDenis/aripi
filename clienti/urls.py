from django.urls import path
from clienti.views import Index, Echipa

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('echipa/', Echipa.as_view(), name='echipa'),
]