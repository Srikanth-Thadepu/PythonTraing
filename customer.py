class Customer:
    def __init__(self,first_name,last_name,ph_no,email,address,pincode):
        self.first_name=first_name
        self.last_name=last_name
        self.ph_no=ph_no
        self.email=email
        self.address=address
        self.pincode=pincode
    
    def display_coustomer_info(self):
        print("Coustomer Name: {self.first_name}")

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

class Order_items:
    def __init__(self,order_id,item_id,product_id,quantity,price,discount):
        self.order_id=order_id
        self.item_id=item_id
        self.product_id=product_id
        self.quantity=quantity
        self.price=price
        self.discount=discount