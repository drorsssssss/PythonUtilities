import abc

class IAdapterPayments(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getPaymentsDataByDay(self,*args) :
        pass