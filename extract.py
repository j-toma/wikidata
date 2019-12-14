import json
import csv
from choose import choose_1, choose_2
from transform_json import transform
from get_property import get_property
from get_claims import get_claims_second
import pandas as pd
import cython

#col_names = ['p_id', 'en_label', 'zh_label']
#props = pd.read_csv('properties.csv',names=col_names,delimiter='|')
#col_names = ['q_id', 'en_label', 'zh_label']
#items = pd.read_csv('items.csv',names=col_names,delimiter='|')

def csv_2_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')
        d = dict()
        for line in reader:
            d.update({line[0]: line[1] + ' ' + line[2]})
    return d

def second_pass():
    #items = csv_2_dict('items.csv')
    #props = csv_2_dict('properties.csv')
    #with open('filtered-claims.json', 'r') as f, open('filtered-claims-2.json', 'w') as n:
    items = csv_2_dict('/mnt/storage/wikidata/items.csv')
    props = csv_2_dict('/home/jtoma/dbClass/properties.csv')
    with open('/mnt/storage/wikidata/wikidata-first.json', 'r') as f, open('/mnt/storage/wikidata/wikidata-second.json', 'w') as n:
        g = 0
        c = 0
        for line in f:
            c += 1
            if c%10000==0:
                print(str(c) + ' lines processed')
            line_dict = json.loads(line)
            new_line = get_claims_second(line_dict, props, items)
            n.write(new_line + "\n")
    return 


def first_pass():
#    with open('20141103.json', 'r') as f, \
#         open('filtered-claims.json', 'w') as n, \
#         open('properties.csv', 'w', newline='') as p, \
#         open('items.csv', 'w', newline='') as i:
    with open('/mnt/storage/wikidata/wikidata.json', 'r') as f, \
         open('/mnt/storage/wikidata/wikidata-first.json', 'w') as n, \
         open('/home/jtoma/dbClass/properties.csv', 'w', newline='') as p, \
         open('/mnt/storage/wikidata/items.csv', 'w', newline='') as i:
        writer_p = csv.writer(p, delimiter = '|')
        writer_i = csv.writer(i, delimiter = '|')
        i = 0
        p = 0
        c = 0
        for line in f:
            c += 1
            if c%10000==0:
                print(str(c) + ' lines processed')
            if line == '[\n' or line == '[':
                pass
            elif p < 4000:
                line_dict = json.loads(line[:-2])
                clf = choose_1(line_dict)
                if clf == 'not_chosen':
                    pass
                elif clf == 'item':
                    item, item_id = transform(line_dict)
                    n.write(item + "\n")
                    writer_i.writerow(item_id)
                    i += 1
                elif clf == 'property':
                    prop = get_property(line_dict)
                    writer_p.writerow(prop)
                    p += 1
            else:
                break
    return c, g, g/c*100, p


#lines_processed, items_saved, ratio, props_saved = first_pass()
#print('lines_processed:', lines_processed)
#print('items_saved:', items_saved)
#print('ratio:', ratio)
#print('props_saved:', props_saved)

second_pass()
#def load_data():
#    with open('20141103.json', 'r') as f,
#         open('filtered.json', 'w', newline='') as n,
#         open('properties.csv', 'w', newline='') as p:
#         open('items.csv', 'w', newline='') as i:
#        writer_p = csv.writer(p, delimiter = '|')
#        writer_i = csv.writer(i, delimiter = '|')
#        g = 0
#        c = 0
#        for line in f:
#            c += 1
#            if line == '[\n':
#                pass
#            elif g < 1000:
#                line_dict = json.loads(line[:-2])
#                clf = choose(line_dict)
#                if clf == 'not_chosen':
#                    pass
#                elif clf == 'item':
#                    item, item_id = transform(line_dict)
#                    n.write(item + "\n")
#                    writer_i.writerow(item_id)
#                    g += 1
#                elif clf == 'property':
#                    prop = get_property(line_dict)
#                    writer_p.writerow(prop)
#            else:
#                break
#    return c, g


