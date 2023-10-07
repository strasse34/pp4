from django.test import TestCase
from .forms import AddFlightForm


class TestAddFlightForm(TestCase):
    """
    Class for testing AddFlightForm to add first name and last name
    """

    def test_origin_field_placeholder(self):
        form = AddFlightForm()
        self.assertEqual(
            form.fields["fname"].widget.attrs.get("placeholder"), "First Name"
        )

    def test_destination_field_placeholder(self):
        form = AddFlightForm()
        self.assertEqual(
            form.fields["lname"].widget.attrs.get("placeholder"), "Last Name"
        )
