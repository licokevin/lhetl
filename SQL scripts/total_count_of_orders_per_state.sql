
SELECT 
    customers.[customer_state],
    COUNT(orders.order_id) AS total_count_of_orders_per_state
FROM 
    LH.dbo.[db_customers_df] customers
JOIN 
    LH.dbo.db_order_items orders
ON 
    customers.[customer_id] = orders.[customer_id]
GROUP BY 
    customers.[customer_state];
