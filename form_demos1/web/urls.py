from django.urls import path

from form_demos1.web.views import index, index_model

urlpatterns = (
    path('', index, name='index'),
    path('model', index_model, name='index-model'),

)