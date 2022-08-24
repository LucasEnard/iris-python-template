from grongier.pex import BusinessOperation

from msg import CustomRequest,CustomResponse

import random
class CustomOperation(BusinessOperation):
    def on_init(self):
        return None

    def on_mesage(self, request):
        return request
    
    def on_custom_message(self,request:CustomRequest):
        resp = CustomResponse(CustomResponse.custobj,random.randint(0,9))
        return resp