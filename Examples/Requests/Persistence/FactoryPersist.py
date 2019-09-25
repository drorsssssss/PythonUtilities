from Examples.Requests.Persistence.PersistFS import PersistFS
from Examples.Requests.Config.ConfigUtil import ConfigUtil

class FactoryPersist:
    def __init__(self):
        self.conf=ConfigUtil.getConf()

    def build(self):
        if self.conf['App.Wikipedia.persist.type'] == 'PersistFS':
            return PersistFS()


