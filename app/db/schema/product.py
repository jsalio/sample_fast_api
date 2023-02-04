from typing import Union
from ..generic import Generic
from ...models.product import Product



class ProductsDb:
    def __init__(self):
        """
        define the schema and collection for products 
        """
        self.generic = Generic(self.schema, "products")
        self.schema = self.generic.schema
        
    def insert(self, document:dict):
        """_summary_

        Args:
            document (dict): product document representation

        Returns:
            _type_: Product
        """
        return self.to_model(self.generic.insert(document))
    
    def search_by_id(self, id:str):
        return self.to_model(self.generic.search_by_id(id))
    
    def get_all_products(self):
        data_set= self.generic.get_all()
        if not data_set:
            return []
        return [self.to_model(document) for document in data_set]
    
    def update(self, id:str, document:dict):
        return self.generic.update(id, document)
    
    def update_field(self, id:str, key:str, value:Union[str,any]):
        return self.generic.update_field(id, key, value)
    
    def search(self, key:str, value:Union[str,any]):
        return self.to_model(self.generic.search(key, value))
    
    def delete(self, id:str):
        return self.generic.delete(id)
        
    def schema(self, document):
        return {
            "id": str(document["_id"]),
            "name": document["name"],
            "description": document["description"],
            "price": document["price"],
            "stock": document["stock"],
            "image": document["image"],
            "category": document["category"],
            "created_at": document["created_at"],
            "updated_at": document["updated_at"]
        }
        
    def to_model(self, document:dict):
        return Product(**document)       