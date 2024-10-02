import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Float
import urllib

# Sample data
data = {
    'order_id': ['00010242fe8c5a6d1ba2dd792cb16214', '00018f77f2f0320c557190d7a144bdd3'],
    'order_item_id': [1, 1],
    'product_id': ['4244733e06e7ecb4970a6e2683c13e61', 'e5f2d52b802189ee658865ca93d83a8f'],
    'seller_id': ['48436dade18ac8b2bce089ec2a041202', 'dd7ddc04e1b6c2c614352b383efe2d36'],
    'shipping_limit_date': ['2017-09-19 09:45', '2017-05-03 11:05'],
    'price': [58.9, 239.9],
    'freight_value': [13.29, 19.93],
    'total_price': [58.9, 59.9]
}

# Create DataFrame
df = pd.DataFrame(data)

# SQL Server connection details (use Windows Authentication)
server = 'localhost'
database = 'LH'

# Properly format the connection string
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=" + server + ";"
    "DATABASE=" + database + ";"
    "Trusted_Connection=yes;"
)

conn_str = f"mssql+pyodbc:///?odbc_connect={params}"

# Create SQLAlchemy engine
engine = create_engine(conn_str)

# Define table schema using SQLAlchemy
metadata = MetaData()

orders_table = Table('orders', metadata,
    Column('order_id', String(50), primary_key=True),
    Column('order_item_id', Integer),
    Column('product_id', String(50)),
    Column('seller_id', String(50)),
    Column('shipping_limit_date', String(50)),
    Column('price', Float),
    Column('freight_value', Float),
    Column('total_price', Float)
)

# Create the table if it doesn't exist
metadata.create_all(engine)

# Insert data from the DataFrame into the table
df.to_sql('orders', engine, if_exists='append', index=False)

print("Data inserted successfully!")
