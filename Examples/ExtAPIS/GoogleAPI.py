from Examples.ExtAPIS.FactorySecrets import FactorySecrets


class GoogleAPI():

    def __init__(self):
        self.source="gcs"
        self.creds = FactorySecrets(self.source).build().get_creds()

    def getGoogleDataByDay(self,path,day,*args):
        return f"Request result: {self.creds}-{path}-{day}-{'-'.join(args)}"



