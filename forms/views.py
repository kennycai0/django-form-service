from django.shortcuts import render, redirect
from .models import Participant, FormModel, FormRecord, FormField, FormData


def welcome(request):
    context = {
        'participants': Participant.objects.all()
    }
    return render(request, 'index.html', context)


def register(request):
    form_fields = FormField.objects.filter(form__name="participants")
    form_model = FormModel()
    if request.POST:
        name = request.POST.get('name')
        age = request.POST.get('age')
        favorite_book = request.POST.get('favorite_book')
        participant = Participant(name=name, age=age, favorite_book=favorite_book)
        participant.save()
        return redirect('forms-welcome')
    context = {
        'form_model': form_model,
        'form_fields': form_fields
    }
    return render(request, 'register.html', context)
