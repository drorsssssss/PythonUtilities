import abc


class ISecurable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_creds(self):
        pass
a
