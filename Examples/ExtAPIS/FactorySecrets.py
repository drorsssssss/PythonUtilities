from Examples.ExtAPIS.SecretGCS import SecretGCS
from Examples.ExtAPIS.SecretMysql import SecretMysql


class FactorySecrets:

    def __init__(self,source):
        self.source=source

    def build(self):
        if self.source == "mysql": return SecretMysql()
        elif self.source == "gcs": return SecretGCS()

