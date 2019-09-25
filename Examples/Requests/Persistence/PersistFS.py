from Examples.Requests.Persistence import IPersistence
import json
from Examples.Requests.Config.ConfigUtil import ConfigUtil

class PersistFS(IPersistence):

    def __init__(self):
        self.conf=ConfigUtil.getConf()
    def process(self,value):
        output_file=self.conf['App.Wikipedia.output_file']

        with open(output_file,'w') as file_obj:
            file_obj.write(json.dumps(value.json(),indent=4))


