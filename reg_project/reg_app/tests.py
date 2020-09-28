from django.test import TestCase
from reg_app import forms


class ItemFormTest(TestCase):

    def test_form_validation_for_all_items(self):
        form = forms.EntryForm()
        self.fail(form.as_p())
