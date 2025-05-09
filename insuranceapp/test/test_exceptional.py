#python manage.py test donationapp.test.test_exceptional
from rest_framework.test import APITestCase
from insuranceapp.models import *
from insuranceapp.test.TestUtils import TestUtils
class HomeInsuranceAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(
        user_id= 2,
        first_name= "Venu",
        last_name= "Gopal",
        user_name="Venu Gopal"
        )

        QuoteModel.objects.create(
        user_id=2,
        quote_id=2,
        hno= "21-133",
        city= "Nijamaabad",
        state= "TS",
        country= "India",
        residance_type= "Individual",
        residance_use= "living",
        detached_structure= "structure2",
        market_value= "7000000.00",
        year_build= 2015,
        square_foot_value= 350,
        dwelling_style= "style2",
        roof_material= "material2",
        garage_type= "type1",
        numfullBaths= 1,
        numhalfBaths= 2
        )

        PolicyModel.objects.create(
        policy_key=1,
        quote_id=2,
        policy_term= "2 years",
        policy_effective_date= "2022-09-01",
        policy_end_date= "2035-01-01"
        )

    def test_register_user_error(self):
        url='http://127.0.0.1:8000/registeruser/'
        data= {
        "user_id": 1,
        "first_name": "Shibu",
        "last_name": "Darshan",
        #"user_name": "Shibu Darshan",
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==400:
            test_obj.yakshaAssert("TestRegisterUserError", True, "functional")
            print("TestRegisterUserError = Passed")
        else:
            test_obj.yakshaAssert("TestRegisterUserError", False, "functional")
            print("TestRegisterUserError = Failed")

    def test_create_quote_error(self):
        url='http://127.0.0.1:8000/createquote/?user_id=22'
        data= {
        "quote_id": 2,
        "user_id": 2,
        "hno": "21-133",
        "city": "Nijamaabad",
        "state": "TS",
        "country": "India",
        "residance_type": "Individual",
        "residance_use": "living",
        "detached_structure": "structure2",
        "market_value": "7000000.00",
        "year_build": 2015,
        "square_foot_value": 350,
        "dwelling_style": "style2",
        "roof_material": "material2",
        "garage_type": "type1",
        "numfullBaths": 1,
        "numhalfBaths": 2
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestCreateQuoteError", True, "functional")
            print("TestCreateQuoteError = Passed")
        else:
            test_obj.yakshaAssert("TestCreateQuoteError", False, "functional")
            print("TestCreateQuoteError = Failed")

    def test_get_quote_error(self):
        url='http://127.0.0.1:8000/getquote/?quote_id=22&user_id=22'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetQuoteError", True, "functional")
            print("TestGetQuoteError = Passed")
        else:
            test_obj.yakshaAssert("TestGetQuoteError", False, "functional")
            print("TestGetQuoteError = Failed")

    def test_buy_policy_error(self):
        url='http://127.0.0.1:8000/buypolicy/?quote_id=22'
        data= {
        "quote_id":2,
        "policy_term": "2 years",
        "policy_effective_date": "2022-09-01",
        "policy_end_date": "2035-01-01"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBuyPolicyError", True, "functional")
            print("TestBuyPolicyError = Passed")
        else:
            test_obj.yakshaAssert("TestBuyPolicyError", False, "functional")
            print("TestBuyPolicyError = Failed")

    def test_show_policy_error(self):
        url='http://127.0.0.1:8000/showpolicy/11/'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==500:
            test_obj.yakshaAssert("TestShowPolicyError", True, "functional")
            print("TestShowPolicyError = Passed")
        else:
            test_obj.yakshaAssert("TestShowPolicyError", False, "functional")
            print("TestShowPolicyError = Failed")

    def test_renew_policy_error(self):
        url='http://127.0.0.1:8000/renewpolicy/11/'
        data= {
        "status":"Renewed"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestRenewPolicyError", True, "functional")
            print("TestRenewPolicyError = Passed")
        else:
            test_obj.yakshaAssert("TestRenewPolicyError", False, "functional")
            print("TestRenewPolicyError = Failed")

    def test_cancel_policy_error(self):
        url='http://127.0.0.1:8000/renewpolicy/11/'
        data= {
        "status":"Cancelled"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestCancelPolicyError", True, "functional")
            print("TestCancelPolicyError = Passed")
        else:
            test_obj.yakshaAssert("TestCancelPolicyError", False, "functional")
            print("TestCancelPolicyError = Failed")
