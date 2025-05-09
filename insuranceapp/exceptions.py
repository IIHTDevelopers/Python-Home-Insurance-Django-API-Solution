
from rest_framework.exceptions import APIException
class IdDoesNotExist(APIException):
    default_detail = 'Specified Quote Id Or User Iid Does Not Exist'

class PolicyKeyDoesNotExist(APIException):
    default_detail = 'Specified Policy Key Does Not Exist'

class UserDoesNotExist(APIException):
    default_detail = 'Specified User Id Does Not Exist'

class QuoteIdDoesNotExist(APIException):
    default_detail = 'Specified Quote Id Does Not Exist To Buy A Policy'
