#!/usr/bin/env python3
# coding: utf-8

import pymongo
from datetime import datetime,timedelta
import dateutil.parser
import sys

class Mongo:

    host="localhost"
    port=27017
    database_name="test"
    collection_name="test"

    def __init__(self):
        self.client=pymongo.MongoClient(self.host, self.port)
        self.change_database()

    def change_database(self):
        exec("self.collection=self.client."+self.database_name+"."+self.collection_name)

    def insert(self,data):
        data["date"]=datetime.now()
        self.collection.insert_one(data)

    def view(self):
        return self.collection.find()

    def view_and(self,data):
        return self.collection.find({'$and':data})

    def view_or(self,data):
        return self.collection.find({'$or':data})

    def count_oneweek(self):
        return self.count_date(datetime.now()+timedelta(weeks=-1),datetime.now())

    def count_date(self,startdate,stopdate):
        return self.count_date_with_condition(startdate,stopdate,{})

    def count_date_with_condition(self,startdate,stopdate,condition):
        date={
                "$gte" : self.convert_to_date(startdate),
                "$lte" : self.convert_to_date(stopdate)
            }
        condition.update({'date':date})
        return self.collection.find(condition).count()

    def convert_to_date(self,time):
        if isinstance(time,str):
            return dateutil.parser.parse(time)
        elif isinstance(time,datetime):
            return time
        else:
            sys.exit(1)

    def disconnect(self):
        self.collection.disconnect()

