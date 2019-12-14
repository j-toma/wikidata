import json
from get_claims import get_claims_first

def transform(line):
    """
    {
     "id": "Q60",
     "labels": {'en': [], 'zh': []},
     "descriptions": {'en': [], 'zh': []},
     "aliases": {'en': [], 'zh': []},
     "claims": {"Pxx": "Qxx", "Pxy": "Qxy", ...},
     "sitelinks": {'enwiki': {}, 'zhwiki':{} },
    }   
    """
    q = line['id']
    claims = get_claims_first(line)
    
    en_label = ''
    zh_label = ''
    if 'labels' in line:
        if 'en' in line['labels']:
            en_label = line['labels']['en']['value']
        if 'zh' in line['labels']:
            zh_label = line['labels']['zh']['value']
        elif 'zh-cn' in line['labels']:
            zh_label = line['labels']['zh-cn']['value']


    en_desc = ''
    zh_desc = ''
    if 'descriptions' in line:
        if 'en' in line['descriptions']:
            en_desc = line['descriptions']['en']['value']
        if 'zh' in line['descriptions']:
            zh_desc = line['descriptions']['zh']['value']
        elif 'zh-cn' in line['descriptions']:
            zh_label = line['descriptions']['zh-cn']['value']


    en_aliases = []
    zh_aliases = []
    if 'aliases' in line:
        if 'en' in line['aliases']:
            en_aliases = [ alias['value'] for alias in line['aliases']['en'] ]
        if 'zh' in line['aliases']:
            zh_aliases = [ alias['value'] for alias in line['aliases']['zh'] ]
        elif 'zh-cn' in line['aliases']:
            zh_aliases = [ alias['value'] for alias in line['aliases']['zh-cn'] ]

    enwiki = ''
    zhwiki = ''
    if 'sitelinks' in line:
        if 'enwiki' in line['sitelinks']:
            enwiki = line['sitelinks']['enwiki']['title']
        if 'zhwiki' in line['sitelinks']:
            zhwiki = line['sitelinks']['zhwiki']['title']


    data = json.dumps({ 
        'id': q, 
        'en_label': en_label,
        'zh_label': zh_label,
        'en_description': en_desc,
        'zh_description': zh_desc,
        'en_aliases': en_aliases,
        'zh_aliases': zh_aliases,
        'claims': claims,
        'enwiki': enwiki,
        'zhwiki': zhwiki
    })

    item_id = [
        q,
        en_label,
        zh_label
    ]

    return data, item_id


