from Examples.ExtAPIS.IAdapterPayments import IAdapterPayments
from Examples.ExtAPIS.GoogleAPI import GoogleAPI


class AdapterGoogleAPI(IAdapterPayments):

    def getPaymentsDataByDay(self,*args):
        return f"{GoogleAPI().getGoogleDataByDay(*args)}-ADAPTER"
