from django.contrib import admin
from .models import Participant, FormModel, FormField

admin.site.register(Participant)
admin.site.register(FormModel)
admin.site.register(FormField)
