from Examples.ExtAPIS.ISecurable import ISecurable


class SecretMysql(ISecurable):
    def get_creds(self):
        print("get mysql creds")
        return "get mysql creds"






