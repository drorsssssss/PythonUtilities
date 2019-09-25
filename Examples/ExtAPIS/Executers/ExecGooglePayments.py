from Examples.ExtAPIS.AdapterGoogleAPI import AdapterGoogleAPI

class Executer:
    googleAdapter = AdapterGoogleAPI().getPaymentsDataByDay("local","2019-07-17")
    print(googleAdapter)