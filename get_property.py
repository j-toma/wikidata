
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

    data = [
        p,
        en_label,
        zh_label
    ]


    return data
