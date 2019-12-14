from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Product
import requests
import time 
from req5_ka import (get_value_id, 
                    get_value_name, 
                    get_value_price_reg__min,
                    get_value_price_promo__min,
                    get_value_group_name)


LINK5KA = "https://5ka.ru/api/v2/special_offers/"

class PkaDb:
    
    def __init__(self, base, db_url):
        engine = create_engine(db_url)
        base.metadata.create_all(engine)
        session_db = sessionmaker(bind=engine)
        self.__session = session_db()
        
    @property
    def session(self):
        return self.__session
            
        
if __name__ == '__main__':      
    db_url = 'sqlite:///Pka.sqlite' 
    db =  PkaDb(Base, db_url) 

    import os
    import json
    
    #req = requests.get("https://api.github.com/users/astavnichiy/repos")
    
    for i in range(25594,25694):
        req = requests.get(LINK5KA + str(i) + "/")
        if i % 25 == 0:
            print (i,"   ", time.time())
        
        a1 = get_value_id(req.text)
        if a1 != "pka_null":
            a2 = get_value_name(req.text)
            a3 = get_value_price_reg__min(req.text)
            a4 = get_value_price_promo__min(req.text)
            a5 = get_value_group_name(req.text)

    #Cохранения данных
            temp = Product(a1,a2 ,a3 ,a4 ,a5 )
            db.session.add(temp)
            db.session.commit()
    
    #Пример запроса
#    temp1 = db.session.query(BlogPost).filter_by(id=1).all() 
#    temp2 = db.session.query(BlogPost).filter_by(id=1).first() 