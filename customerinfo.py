class Customer:
    def __init__(self, first_name, last_name, ph_no, email, address, pincode):
        self.first_name = first_name
        self.last_name = last_name
        self.ph_no = ph_no
        self.email = email
        self.address = address
        self.pincode = pincode
    
    def get_customer_info(self):
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Contact": self.ph_no,
            "Email Address": self.email,
            "Pincode": self.pincode
        }