from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from cart.forms import CartAddProductForm

class CartAddProductFormTest(TestCase):

    def test_form(self):
        form_data = {'quantity':100, 'update':True}
        form = CartAddProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_without_update(self):
        form_data = {'quantity':100}
        form = CartAddProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form_data = {'quantity':'foo', 'update':'bar'}
        form = CartAddProductForm(data=form_data)
        self.assertFalse(form.is_valid())
