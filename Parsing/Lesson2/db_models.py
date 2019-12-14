from sqlalchemy import (Table, Column, ForeignKey, String, Integer, Float)

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import json


Base = declarative_base()

#===============================================================================
# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True, autoincrement = True)
#===============================================================================

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    pka_id = Column(Integer)
    name = Column(String)
    price_reg__min = Column(Float)
    price_promo__min = Column(Float)
    group_name = Column(String)
    
    def __init__ (self, pka_id, name, price_reg__min, price_promo__min, group_name):
        self.pka_id = pka_id
        self.name = name
        self.price_reg__min = price_reg__min
        self.price_promo__min = price_promo__min
        self.group_name = group_name        

#===============================================================================
#     def get_value_id(self, json5ka):
#         json5ka = json.loads(json5ka)
#         return json5ka["id"]
# 
# 
#     def get_value_name(self, json5ka):
#         json5ka = json.loads(json5ka)
#         return json5ka["name"]
#    
#     def get_value_price_reg__min(self, json5ka):
#         json5ka = json.loads(json5ka)
#         return json5ka["current_prices"]["price_reg__min"]
#     
#     def get_value_price_promo__min(self, json5ka):
#         json5ka = json.loads(json5ka)
#         return json5ka["current_prices"]["price_promo__min"]
#     
#     def get_value_group_name(self, json5ka):
#         json5ka = json.loads(json5ka)
#         return json5ka["product"]["group"]["group_name"]
#===============================================================================
#===============================================================================
# class BlogPost (Base):
#     __tablename__ = 'blogpost'
#     id = Column(Integer, primary_key = True, autoincrement = True)
#     url = Column(String, unique = True)
#     title = Column(String)
#     __writer = Column(Integer, ForeignKey('writer.id'))
#     writer = relationship('Writer', backref='posts')
#      
#     def __init__ (self, title: str, url: str, writer):
#         self.title = title
#         self.url = url
#         self.writer = writer
# 
# class Writer (Base):
#     __tablename__ = 'writer'
#     id = Column(Integer, primary_key = True, autoincrement = True)
#     name = Column(String)
#     url = Column(String, unique = True)
#     
#     def __init__ (self, name: str, url: str):
#         self.name = name
#         self.url = url
# 
#         
# class Tag (Base):
#     __tablename__ = 'tag'
#     id = Column(Integer, primary_key = True, autoincrement = True)
#     name = Column(String, unique = True)
#     
#     def __init__ (self, name: str):
#         self.name = name
#===============================================================================





