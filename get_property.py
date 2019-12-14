
def get_property(line):

    p = line['id']

    en_label = ''
    zh_label = ''
    if 'labels' in line:
        if 'en' in line['labels']:
            en_label = line['labels']['en']['value']
        if 'zh' in line['labels']:
            zh_label = line['labels']['zh']['value']
        elif 'zh-cn' in line['labels']:
            zh_label = line['labels']['zh-cn']['value']
#
#    en_desc = ''
#    zh_desc = ''
#    if 'descriptions' in line:
#        if 'en' in line['descriptions']:
#            en_desc = line['descriptions']['en']['value']
#        if 'zh' in line['descriptions']:
#            zh_desc = line['descriptions']['zh']['value']
#
    data = [
        p,
        en_label,
        zh_label
    ]
    #data = json.dumps({
    #    'id': q,
    #    'en_label': en_label,
    #    'zh_label': zh_label,
    #    'en_description': en_desc,
    #    'zh_description': zh_desc
    #})

    return data
