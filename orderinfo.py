class Orders:
    def __init__(self, order_id, customer_id, order_status, order_date, delivery_date, shipped_date, store_id, staff_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id
    
    def get_order_info(self):
        return {
            "Order Id": self.order_id,
            "Customer Id": self.customer_id,
            "Order Status": self.order_status,
            "Order Date": self.order_date,
            "Delivery Date": self.delivery_date,
            "Shipped Date": self.shipped_date,
            "Store Id": self.store_id,
            "Staff Id": self.staff_id
        }

class OrderItems(Orders):
    def __init__(self, order_id, customer_id, order_status, order_date, delivery_date, shipped_date, store_id, staff_id, item_id, product_id, quantity, price, discount):
        super().__init__(order_id, customer_id, order_status, order_date, delivery_date, shipped_date, store_id, staff_id)
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discount = discount
    
    def get_order_item_info(self):
        order_info = self.get_order_info()
        order_info.update({
            "Item Id": self.item_id,
            "Product Id": self.product_id,
            "Quantity": self.quantity,
            "Price": self.price,
            "Discount": self.discount
        })
        return order_info