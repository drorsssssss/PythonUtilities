from pyhocon import ConfigFactory

class ConfigUtil:
    def __init__(self):
        self.conf = ConfigFactory.parse_file('/Users/dsivan/GitRepos/PythonUtilities/Examples/Requests/Config/application.conf')

    def getConf(self):
        return self.conf


