def getProperties(object):
    this_dict = {}
    for property, value in vars(object).items():
        item_to_add = {f"{property}": f"{value}"}
        this_dict.update(item_to_add)
    return this_dict
    
    