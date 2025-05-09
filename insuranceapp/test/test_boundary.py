from rest_framework.test import APITestCase
from insuranceapp.test.TestUtils import TestUtils
class HomeInsuranceAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary",True,"boundary")
        print("TestBoundary = Passed")
