from fastapi import APIRouter, HTTPException, status

from ..models.product import Product
from ..db.schema.product import ProductsDb

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/", response_model=list[Product], status_code=status.HTTP_200_OK)
async def get_products() -> list[Product]:
    db = ProductsDb()
    return db.get_all_products()

@router.get("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def get_product(product_id: str) -> Product:
    """Get a product by id."""
    db = ProductsDb()
    return db.search_by_id(product_id)

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Create a new product in the database."""
    try:
        db = ProductsDb()
        new_product = db.insert(product.to_dict())
        return new_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.put("/{product_id}", response_model=Product, status_code=status.HTTP_201_CREATED)
async def update_product(product_id: str, product: Product):
    """Update a product in the database."""
    try:
        db = ProductsDb()
        found = db.update(product_id, product.to_dict())
        if not found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not modified")
        else :
            return product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str):
    """Delete a product from the database."""
    try:
        db = ProductsDb()
        removed = db.delete(product_id)
        if not removed:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not deleted")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get("/search/{product_name}", response_model=Product, status_code=status.HTTP_200_OK)
async def search_product(product_name: str) -> Product:
    """Search for a product by name."""
    db = ProductsDb()
    return db.search("name",product_name)

@router.put("/{product_id}/price", response_model=bool, status_code=status.HTTP_201_CREATED)
async def update_product_price(product_id: str, price: float):
    try:
        db = ProductsDb()
        found = db.update_field(product_id,"price", price)
        if not found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not modified")
        else :
            return found
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))