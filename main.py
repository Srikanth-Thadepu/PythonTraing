from customerinfo import Customer
from orderinfo import OrderItems

customer = Customer("Srikanth", "Thadepu", "7********7", "st03@example.com", "123 Street, City", "123456")
order_item = OrderItems(101, customer, "Shipped", "2024-01-01", "2024-01-05", "2024-01-03", 1, 10, 1, 202, 2, 500.0, 10.0)

print(order_item.get_order_item_info())