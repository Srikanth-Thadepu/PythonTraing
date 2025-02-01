class Customer:
    def __init__(self,first_name,last_name,ph_no,email,address,pincode):
        self.first_name=first_name
        self.last_name=last_name
        self.ph_no=ph_no
        self.email=email
        self.address=address
        self.pincode=pincode
    
    def get_coustomer_info(self):
        return {
            "First Name":self.first_name,
            "Last Name":self.last_name,
            "Contact":self.ph_no,
            "Email Address":self.email,
            "Pincode":self.pincode}

class Orders:
    def __init__(self,order_id,customer_id,order_status,order_date,delivery_date,shipped_date,store_id,staff_id):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_status=order_status
        self.order_date=order_date
        self.delivery_date=delivery_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id
    
    def get_order_info(self):
        return {
            "Order Id":self.order_id,
            "Customer Id":self.customer_id,
            "Order Status":self.order_status,
            "Delivery Date":self.delivery_date,
            "Shipped Date":self.shipped_date,
            "Store Id":self.store_id,
            "Staff Id":self.staff_id
        }

class Order_items(Orders):
    def __init__(self,order_id,customer_id,order_status,order_date,delivery_date,shipped_date,store_id,staff_id,item_id,product_id,quantity,price,discount):
        super().__init__(order_id,customer_id,order_status,order_date,delivery_date,shipped_date,store_id,staff_id)
        self.order_id=order_id
        self.item_id=item_id
        self.product_id=product_id
        self.quantity=quantity
        self.price=price
        self.discount=discount
    
    def get_order_item_info(self):
        order_info=self.get_order_info()
        order_info.update({
            "Item Id":self.item_id,
            "Product Id":self.product_id,
            "Quantity": self.quantity,
            "Price": self.price,
            "Discount": self.discount
        })
        return order_info

customer = Customer("Srikanth", "Thadepu", "7********7", "st03@example.com", "123 Street, City", "123456")
order_item = Order_items(101, customer, "Shipped", "2024-01-01", "2024-01-05", "2024-01-03", 1, 10, 1, 202, 2, 500.0, 10.0)

print(order_item.get_order_item_info())