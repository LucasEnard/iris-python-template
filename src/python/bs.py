from grongier.pex import BusinessService


class CustomService(BusinessService):

    def getAdapterType():
        """
        Name of the registred Adapter
        """
        return "Ens.InboundAdapter"

    def on_init(self):
        return None

    def on_process_input(self,request):
        return request

    def on_task(self):
        return None
