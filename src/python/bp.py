from grongier.pex import BusinessProcess

class CustomProcess(BusinessProcess):
    
    def on_init(self):
        return None

    def on_request(self, request):
        return request
