from django import forms
from reg_app.models import Entry


class DatePicker(forms.DateInput):
    input_type = "date"


class EntryForm(forms.ModelForm):
    files = forms.FileField(required=False)
    #date_responded = forms.DateInput(required=False)

    class Meta:
        model = Entry
        fields = ['user', 'date_responded', 'subject', 'sender', 'files',
                  'num_of_file', 'date_of_file', 'date_recived']
        widgets = {
            'date_responded': DatePicker(format='%Y-%m-%d'),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'sender': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.FileInput(attrs={'class': 'form-control'}),
            'num_of_file': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_file': DatePicker(format='%Y-%m-%d'),
            'date_recived': DatePicker(format='%Y-%m-%d')
        }
