SELECT 
    products.product_category_name,
    SUM(orders.total_price) AS total_sales_per_category
FROM 
    LH.dbo.db_products products
JOIN 
    LH.dbo.db_order_items orders
ON 
    products.product_id = orders.product_id
GROUP BY 
    products.product_category_name;