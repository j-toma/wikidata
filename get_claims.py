import json
import pandas as pd


def get_claims_second(line, prop_list, item_list):

    claims = []
    for i in range(len(line['claims'])):
        prop_id = line['claims'][i][0]
        item_id = line['claims'][i][1]
        if item_id in item_list and prop_id in prop_list:
            prop_label = prop_list[prop_id]
            item_label = item_list[item_id]
            claim = prop_label + ' ' + item_label
            claims.append(claim)
        #elif item_id in item_list:
        #    item_label = item_list[item_id]
        #    claim = prop_id + ' ' + item_label
        #    claims.append(claim)
        #elif prop_id in prop_list:
        #    prop_label = prop_list[prop_id]
        #    claim = prop_label + ' ' + item_id
        #    claims.append(claim)
        #else:
        #    claim = prop_id + ' ' + item_id
        #    claims.append(claim)
    line['claims'] = claims
    data = json.dumps(line)
    return data

def get_claims_first(line):

    claims = []
    properties = line['claims'].keys()
    for prop in properties:
#        for obj in line['claims'][prop]:
# just get the first claim for each property
        obj = line['claims'][prop][0]
        if 'mainsnak' in obj:
            mainsnak = obj['mainsnak']
            if 'datavalue' in mainsnak:
                data_value = mainsnak['datavalue']
                if 'value' in data_value:
                    val = data_value['value']
                    if 'numeric-id' in val:
                        obj_id = val['numeric-id']
                        obj_id = 'Q' + str(obj_id)
                        claims.append((prop,obj_id))

    return claims

#def get_claims_orig(line, prop_list, item_list):
#
#    claims = []
#    properties = line['claims'].keys()
#    for prop in properties:
##        for obj in line['claims'][prop]:
## just get the first claim for each property
## leave immediately if prop isnt in prop list
#        if prop in prop_list:
#            obj = line['claims'][prop][0]
#            if 'mainsnak' in obj:
#                mainsnak = obj['mainsnak']
#                if 'datavalue' in mainsnak:
#                    data_value = mainsnak['datavalue']
#                    if 'value' in data_value:
#                        val = data_value['value']
#                        if 'numeric-id' in val:
#                            obj_id = val['numeric-id']
#                            obj_id = 'Q' + str(obj_id)
#                            if obj_id in item_list:
#                                claim = ''
#                                claim += prop_list[prop] + ' ' + item_list[obj_id]
#                                claims.append(claim)
#
#    # sub in the new claim
#    line['claims'] = claims
#    data = json.dumps(line)
#
#    return data
