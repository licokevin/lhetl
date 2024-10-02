from main import *

def checkDataDensity(masterDf):

    rows_count = len(masterDf.index)
    columns = masterDf.columns
    message = f'rows count : {rows_count}\n'
    for column in columns:
        nan_count = masterDf[column].isna().sum()
        if nan_count > 0:
            message += (f'{column} has {nan_count} nan {'row' if nan_count == 1 else 'rows'} - {round(nan_count*100/rows_count,2)}%') + '\n'
    if message != f'rows count : {rows_count}\n':
        return message
    else:
        return message + 'No empty cells\n'





print("customers_df " + checkDataDensity(geolocation_df))
print("geolocation_df " + checkDataDensity(geolocation_df))
print("order_items " + checkDataDensity(order_items))
print("order_payments_df " + checkDataDensity(order_payments_df))
print("order_reviews " + checkDataDensity(order_reviews))
print("orders_df " + checkDataDensity(orders_df))
print("sellers " + checkDataDensity(sellers))
print("products " + checkDataDensity(products))
print("product_category_name_transla " + checkDataDensity(product_category_name_transla))
