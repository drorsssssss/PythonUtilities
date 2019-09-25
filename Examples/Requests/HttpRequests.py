import requests
import json
from Examples.Requests.Config.ConfigUtil import ConfigUtil
from Examples.Requests.Helpers import Helpers
from Examples.Requests.Persistence.FactoryPersist import FactoryPersist

#Configuration
conf = ConfigUtil().getConf()
url=conf.get_string('App.Wikipedia.url')
params_configtree = conf.get('App.Wikipedia.params')
params = Helpers.configtree_to_dict(params_configtree)

#Get Http Request
result = requests.get(url,params=params)

#Persistence to FS
# output_file=conf['App.Wikipedia.output_file']
# with open(output_file,'w') as file_obj:
#     file_obj.write(json.dumps(result.json(),indent=4))
conf_factory = conf['App.Wikipedia.persist']

cls =FactoryPersist().build(conf_factory)
cls.process()
