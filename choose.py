

def choose_1(line):
    """
    return a boolean about whether to eat or chuck this line
    1. return english or chinese items (not properties!)
    2. must be instance of or subclass of something else
    3. must have a wikipedia page
    """
    flag = 'not_chosen'

    if line['type'] == 'item' and 'sitelinks' in line:
        if 'labels' in line:
            lbl_langs = line['labels']
            if 'en' in lbl_langs or 'zh' in lbl_langs or 'zh-cn' in lbl_langs:
                if 'descriptions' in line:
                    dsc_langs = list(line['descriptions'].keys())
                    alias_langs = list(line['aliases'].keys())
                    alt_langs = set(dsc_langs + alias_langs)
                    if 'en' in alt_langs or 'zh' in alt_langs or 'zh-cn' in alt_langs:
                        if 'claims' in line:
                            properties = line['claims']
                            if 'P31' in properties or 'P279' in properties:
                                flag = 'item'
    elif line['type'] == 'property':
        flag = 'property'

    return flag

def choose_2(line):
    """
    Now unused
    """
    flag = False

    if line['type'] == 'item' and 'sitelinks' in line:
        if 'labels' in line:
            lbl_langs = line['labels']
            if 'en' in lbl_langs or 'zh' in lbl_langs:
                if 'descriptions' in line:
                    dsc_langs = line['descriptions']
                    if 'en' in dsc_langs or 'zh' in dsc_langs:
                        if 'claims' in line:
                            properties = line['claims']
                            if 'P31' in properties or 'P279' in properties:
                                flag = True

    return flag



