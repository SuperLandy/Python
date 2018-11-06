#coding:utf-8
import pymongo
from bson import json_util as jsonb

def pool():
    client = pymongo.MongoClient(host='192.168.91.52', port=27017)
    client.admin.authenticate('root', 'root', mechanism='MONGODB-CR')
    db = client['db_test']
    collection = db['t_developer']
    return collection

def select():
    collection = pool()
    bason_data = jsonb.dumps(list(collection.find({})))
    return bason_data


def insert(db='db_test'):
    collection = pool()
    spon = collection.insert({"name": "sunjiajia", "tel": "13799360072", "pwd": "340020779", "uid": "2"})
    if spon:
        return 0
    else:
        return 1

