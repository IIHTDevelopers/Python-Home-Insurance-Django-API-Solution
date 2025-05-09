from rest_framework.serializers import ModelSerializer
from insuranceapp.models import UserModel,QuoteModel,PolicyModel

class UserSerializer(ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'

class QuoteSerializer(ModelSerializer):
    class Meta:
        model=QuoteModel
        fields='__all__'

class PolicySerializer(ModelSerializer):
    class Meta:
        model=PolicyModel
        fields='__all__'
