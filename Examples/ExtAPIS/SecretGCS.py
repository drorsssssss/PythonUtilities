from Examples.ExtAPIS.ISecurable import ISecurable


class SecretGCS(ISecurable):

    def get_creds(self):

        print("get gcs creds")
        return "get gcs creds"






