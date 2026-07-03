from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Date
from database.db import Base


class Sales(Base):

    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    order_date = Column(Date)
    product_name = Column(String)
    sku = Column(String)
    city = Column(String)
    darkstore = Column(String)
    warehouse = Column(String)
    units_sold = Column(Integer)
    revenue = Column(Float)


class Product(Base):

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    sku = Column(String, unique=True)
    product_name = Column(String)
    category = Column(String)
    brand = Column(String)


class Region(Base):

    __tablename__ = "regions"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    warehouse = Column(String)
    availability = Column(Float)


class Alert(Base):

    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    priority = Column(String)
    title = Column(String)
    message = Column(String)
    status = Column(String)