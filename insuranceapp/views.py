from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from insuranceapp.serializers import UserSerializer,QuoteSerializer,PolicySerializer
from insuranceapp.models import UserModel,QuoteModel,PolicyModel
from insuranceapp.exceptions import PolicyKeyDoesNotExist,IdDoesNotExist,UserDoesNotExist,QuoteIdDoesNotExist
from insuranceapp.service  import PolicyService
class UserRegisterView(APIView):
    #Register a new user
    def post(self, request,format=None):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User registred successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class QuoteView(APIView):
    #Retrieve an existing Quote with  quote_id and user_id
    def get(self,request,pk=None,format=None):
        #id=pk
        quote_id=self.request.GET.get('quote_id')
        user_id=self.request.GET.get('user_id')

        qs=QuoteModel.objects.filter(quote_id=quote_id,user_id=user_id)
        if qs:
            serializer=QuoteSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise IdDoesNotExist()
    #Create Quote
    def post(self, request,format=None):
        user_id=self.request.GET.get('user_id')
        qs=UserModel.objects.filter(user_id=user_id)
        if qs:
            serializer=QuoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Quote created successfully"},status=status.HTTP_201_CREATED)
        else:
            raise UserDoesNotExist()
            #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BuyPolicyView(APIView):
    #Buy a policy
    def post(self, request,format=None):
        quote_id=self.request.GET.get('quote_id')
        qs=QuoteModel.objects.filter(quote_id=quote_id)
        if qs:
            serializer=PolicySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Policy bought successfully"},status=status.HTTP_201_CREATED)
            #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            raise QuoteIdDoesNotExist()

class ShowPolicyView(APIView):
    #View policy
    def get(self,request,pk=None,format=None):
        id=pk
        qs=PolicyModel.objects.filter(policy_key=id)
        if qs:
            serializer=PolicySerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise PolicyKeyDoesNotExist()

class RenewPolicyView(APIView):
    #Renew Policy
    def patch(self,request,pk,format=None):
        try:
            policy=PolicyModel.objects.get(policy_key=pk)
            serializer=PolicySerializer(policy,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Policy Renewed"})
        except PolicyModel.DoesNotExist:
            raise PolicyKeyDoesNotExist()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CancelPolicyView(APIView):
    #Cancel Policy
    def patch(self,request,pk,format=None):
        try:
            serializer=PolicyService.cancel_policy(pk,request)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Policy Cancelled"})
        except PolicyModel.DoesNotExist:
            raise PolicyKeyDoesNotExist()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
