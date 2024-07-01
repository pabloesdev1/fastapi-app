from fastapi import APIRouter
from sqlmodel import Session, select
from config import engine
from models.product import Product, Category

router = APIRouter(tags=["Products"], prefix="/products")

@router.post("/categories")
def create_category(category: Category):
    with Session(engine) as session:
        session.add(category)
        session.commit()
    return "Category created"

@router.get("/")
def list_products() -> list[Product]:
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        return [product.model_dump() for product in results]

@router.post("/")
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
    return "Product created"

@router.put("/{id}")
def update_product(id: int, product: Product):
    with Session(engine) as session:
        statement = select(Product).where(Product.id == id)
        result = session.exec(statement).one()
        result.name = product.name
        result.price = product.price
        session.add(result)
        session.commit()
    return "Product updated"


@router.delete("/{id}")
def remove_product(id: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.id == id)
        result = session.exec(statement).one()
        session.delete(result)
        session.commit()
    return "Product deleted"
