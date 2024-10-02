import pandas as pd
from pathlib import Path




script_location = Path(__file__).absolute().parent
archive_location = f'{script_location}/archive'

filenames = {
    "customers" : "olist_customers_dataset.csv", #Information about customers and their geographic data.
    "geolocation" : "olist_geolocation_dataset.csv",
    "order_items" : "olist_order_items_dataset.csv", #Details about each item in an order, including price, freight value, and the connection between orders and products.
    "order_payments" : "olist_order_payments_dataset.csv", #Payment information associated with each order.
    "order_reviews" : "olist_order_reviews_dataset.csv", #Customer reviews and ratings for orders.
    "orders" : "olist_orders_dataset.csv", #Contains order information such as order status, purchase date, and delivery date.
    "products" : "olist_products_dataset.csv", #Contains product-related information.
    "sellers" : "olist_sellers_dataset.csv", #Details about sellers and their geographic information.
    "product_category_name_translation" : "product_category_name_translation.csv",
}

print("Reading files as df")
# Read files as pandas df
customers_df = pd.read_csv(f'{archive_location}/{filenames["customers"]}')
geolocation_df = pd.read_csv(f'{archive_location}/{filenames["geolocation"]}')
order_items = pd.read_csv(f'{archive_location}/{filenames["order_items"]}')
order_payments_df = pd.read_csv(f'{archive_location}/{filenames["order_payments"]}')
order_reviews = pd.read_csv(f'{archive_location}/{filenames["order_reviews"]}')
orders_df = pd.read_csv(f'{archive_location}/{filenames["orders"]}')
products = pd.read_csv(f'{archive_location}/{filenames["products"]}')
sellers = pd.read_csv(f'{archive_location}/{filenames["sellers"]}')
product_category_name_translation = pd.read_csv(f'{archive_location}/{filenames["product_category_name_translation"]}')


#drop_dublicates
print("customers_df")
print(len(customers_df.index))
print(customers_df)
customers_df.drop_duplicates(inplace=True)
customers_df.reset_index(inplace=True , drop=True)
print(len(customers_df.index))
print(customers_df)

print("geolocation_df")
print(len(geolocation_df.index))
geolocation_df.drop_duplicates(inplace=True)
geolocation_df.reset_index(inplace=True , drop=True)
print(len(geolocation_df.index))

print("order_items")
print(len(order_items.index))
order_items.drop_duplicates(inplace=True)
order_items.reset_index(inplace=True , drop=True)
print(len(order_items.index))

print("order_payments_df")
print(len(order_payments_df.index))
order_payments_df.drop_duplicates(inplace=True)
order_payments_df.reset_index(inplace=True , drop=True)
print(len(order_payments_df.index))

print("order_reviews")
print(len(order_reviews.index))
order_reviews.drop_duplicates(inplace=True)
order_reviews.reset_index(inplace=True , drop=True)
print(len(order_reviews.index))

print("orders_df")
print(len(orders_df.index))
orders_df.drop_duplicates(inplace=True)
orders_df.reset_index(inplace=True , drop=True)
print(len(orders_df.index))

print("products")
print(len(products.index))
products.drop_duplicates(inplace=True)
products.reset_index(inplace=True , drop=True)
print(len(products.index))

print("sellers")
print(len(sellers.index))
sellers.drop_duplicates(inplace=True)
sellers.reset_index(inplace=True , drop=True)
print(len(sellers.index))

print("product_category_name_translation")
print(len(product_category_name_translation.index))
product_category_name_translation.drop_duplicates(inplace=True)
product_category_name_translation.reset_index(inplace=True , drop=True)
print(len(product_category_name_translation.index))


# #fill_na

# # print(orders_df[orders_df["order_approved_at"].isna()])
# orders_df["order_delivered_carrier_date"] = orders_df["order_delivered_carrier_date"].fillna(pd.NaT)
# orders_df["order_approved_at"] = orders_df["order_approved_at"].fillna(pd.NaT)
# orders_df["order_delivered_customer_date"] = orders_df["order_delivered_customer_date"].fillna(pd.NaT)
# # print(orders_df[orders_df["order_approved_at"] == pd.NaT])


# print(products[products["product_category_name"].isna()])
# products["product_category_name"].fillna(0,inplace=True)
# products["product_description_lenght"].fillna(0,inplace=True)
# products["product_photos_qty"].fillna(0,inplace=True)
# products["product_weight_g"].fillna('',inplace=True)
# products["product_length_cm"].fillna('',inplace=True)
# products["product_photos_qty"].fillna('',inplace=True)
# products["product_width_cm"].fillna('',inplace=True)
# print(products[products["product_category_name"] == 0])


# print(order_reviews[order_reviews["review_comment_message"].isna()])
# order_reviews["review_comment_title"].fillna('',inplace=True)
# order_reviews["review_comment_message"].fillna('',inplace=True)
# print(order_reviews[order_reviews["review_comment_message"] == ''])


# #Creating Calculated columns

# order_items["total_price"] = order_items["freight_value"] +  order_items["price"]
# print(order_items)


# orders_df["delivery_time"] = pd.to_datetime(orders_df["order_delivered_customer_date"]) - pd.to_datetime(orders_df["order_purchase_timestamp"])
# print(orders_df[orders_df["order_id"] == "136cce7faa42fdb2cefd53fdc79a6098"])

# payments_count = order_payments_df.groupby('order_id').size().reset_index(name='payments_count')
# orders_df = orders_df.merge(payments_count, on='order_id', how='left')
# orders_df['payments_count'].fillna(0, inplace=True)
# orders_df['payments_count'] = orders_df['payments_count'].astype(int)

# orders_df["payments_count"] = 0
# for index, row in orders_df.iterrows():
#     if row["order_id"] in order_payments_df["order_id"].tolist():
#         orders_df.loc[index, 'payments_count'] = (order_payments_df["order_id"] == row["order_id"]).sum()

# print(orders_df)

# #tbc on negative values
# order_items["profit_margin"] = order_items["price"] - order_items["freight_value"]
# print(order_items.sort_values(by=["freight_value"],ascending=False))




# #A running total of product price for each customer partitioned by Customer ID
# orders_with_price_df = pd.merge(orders_df, order_items[['order_id', 'price']], on='order_id', how='left')

# orders_with_price_df['running_total'] = orders_with_price_df.groupby('customer_id')['price'].expanding().sum().reset_index(level=0, drop=True)

# orders_with_price_df.to_csv("orders_with_price_df.csv")
# print(orders_with_price_df)


# orders_df['delivery_time'] = pd.to_numeric(orders_df['delivery_time'], errors='coerce')

# orders_with_productId_df = pd.merge(orders_df, order_items[['order_id', 'product_id']], on='order_id', how='left')
# print(orders_with_productId_df)
# orders_with_product_category_df = pd.merge(orders_with_productId_df, products[['product_id', 'product_category_name']], on='product_id', how='left')
# print(orders_with_product_category_df)

# orders_with_product_category_df['rolling_avg_delivery_time'] = orders_with_product_category_df.groupby('product_category_name')['delivery_time'].rolling(window=2).mean().reset_index(level=0, drop=True)

# orders_with_product_category_df['delivery_time'] = pd.to_timedelta(orders_with_product_category_df['delivery_time'])
# orders_with_product_category_df['rolling_avg_delivery_time'] = pd.to_timedelta(orders_with_product_category_df['rolling_avg_delivery_time'])

# orders_with_product_category_df.to_csv("orders_with_product_category_df.csv")
