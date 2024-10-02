SELECT
    [seller_id],
    AVG(CAST([delivery_time] AS FLOAT)) AS average_delivery_time_per_seller
FROM 
    [LH].[dbo].[db_order_items]
WHERE
	[delivery_time] > 0
GROUP BY
    [seller_id];