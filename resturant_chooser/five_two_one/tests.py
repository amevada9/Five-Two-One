from django.test import TestCase
from django.urls import reverse
from .models import Resturants
# Create your tests here.
class ResturantTestCase(TestCase):
    """This class defines the test suite for the Resturant model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.resturant_name = "Write world class code"
        self.resturant = Resturants(name=self.resturant_name)

    def test_model_can_create_a_resturant(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Resturants.objects.count()
        self.resturant.save()
        for i in range(100):
            new_resturant = Resturants()
            new_resturant.save()
            new_count = Resturants.objects.count()
            self.assertNotEqual(old_count, new_count)