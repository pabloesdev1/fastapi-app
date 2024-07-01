from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Product(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(...)
    price: float = Field(...)
    category_id: int = Field(default=None, foreign_key="category.id")
    category: Category = Relationship()
