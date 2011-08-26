import datetime

from django import forms
from timing import models

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December']

ENUM_MONTHS = [(i+1, m) for i, m in enumerate(MONTHS)]

ENUM_YEARS = [(y, y) for y in range(2002, 1900, -1)]


class ConsentForm(forms.Form):
    consent = forms.BooleanField(
        label="I have read the above and give my consent to take part in this study.")


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        {'autofocus':'autofocus'}))


class DemographicsForm(forms.ModelForm):

    class Meta:
        model = models.Participant
        exclude = ['participant_number', 'consent_given', 'email']

    birth_year = forms.TypedChoiceField(choices=ENUM_YEARS, coerce=int)

    birth_month = forms.TypedChoiceField(choices=ENUM_MONTHS, coerce=int)

    email_ok = forms.BooleanField(required=False,
        label="I would like to be contacted to participate in future experiments.")

    def clean(self):
        cleaned_data = self.cleaned_data

        b_year = cleaned_data.get("birth_year")
        b_month = cleaned_data.get("birth_month")

        birth_date = datetime.date(year=b_year, month=b_month, day=1)
        now = datetime.date.today()
        old_enough_date = datetime.date(
            year=now.year-18, month=now.month, day=1)

        if birth_date > old_enough_date:
            raise forms.ValidationError("You must be at least 18.")

        return cleaned_data
