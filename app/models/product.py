
from typing import Union
from pydantic import BaseModel

class Product(BaseModel):
    id:Union[str,None]=None
    name:str
    description:Union[str,None]=None
    price:float
    stock:Union[int,None]=None
    category:Union[str,None]=None
    image:Union[str,None]=None
    created_at:Union[str,None]=None
    updated_at:Union[str,None]= None
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
            "image": self.image,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }