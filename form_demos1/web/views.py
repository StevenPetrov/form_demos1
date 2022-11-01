from django import forms
from django.shortcuts import render

from form_demos1.web.forms import NameForm
from form_demos1.web.models import Person


def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Person.objects.create(name=name)
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name',)
        # exclude = ('age',)


def index_model(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(**form.cleaned_data)
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form
    }
    return render(request, 'base.html', context)
