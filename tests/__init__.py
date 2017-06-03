import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

parent = os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)))

sys.path.insert(0, parent)

from django.test import TestCase
from django.template import Template
from django.core.management import call_command
from django import forms


TEST_DIR = os.path.abspath(os.path.join(__file__, '..'))


CHOICES = (
    (0, 'Zero'), 
    (1, 'One'), 
    (2, 'Two'),
)

class ExampleForm(forms.Form):
    char_field = forms.CharField()
    choice_field = forms.ChoiceField(choices=CHOICES)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    file_fied = forms.FileField()
    password_field = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    boolean_field = forms.BooleanField()


class BootstrapTemplateTagTests(TestCase):
    def setUp(self):
        call_command('syncdb', interactive=False)

    def test_basic_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap %}{{ form|bootstrap }}").render({'form': form})

        tpl = os.path.join('fixtures', 'basic.html')
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)

    def test_horizontal_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap %}{{ form|bootstrap_horizontal }}").render({'form': form})

        tpl = os.path.join('fixtures', 'horizontal.html')
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)
