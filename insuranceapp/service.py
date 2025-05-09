from insuranceapp.models import PolicyModel
from insuranceapp.serializers import PolicySerializer
class PolicyService:
    def cancel_policy(pk,request):
        policy=PolicyModel.objects.get(policy_key=pk)
        serializer=PolicySerializer(policy,data=request.data,partial=True)
        return serializer
