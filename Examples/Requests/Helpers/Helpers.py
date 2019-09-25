def configtree_to_dict(configtree):
    res={}
    for k,v in configtree.items():
        res[k]=v
    return res