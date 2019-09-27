from django.forms import ModelForm, SplitDateTimeField
from django.contrib.admin import widgets
from .models import Event, Category, Account


class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ['host']
        fields = [
            'host',
            'title', 
            'location', 
            'venue', 
            'start_time',
            'end_time',
            'categories' 
            ]


class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]


