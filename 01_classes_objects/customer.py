class Customer:
    """Represent an e-commerce customer"""

    store_name="THE XYZ STORE"

    def __init__(self,name: str, email: str, phone_no: str, address: str)-> None:
        name= name.strip();
        email= email.strip().lower();
        phone_no= phone_no.strip();
        address= address.strip();

        if not name:
            raise ValueError("Cutomer name cannot be empty")
        if not email or "@" not in email:
            raise ValueError("A valid address is required")
        if not phone_no or len(phone_no)!=11:
            raise ValueError("A valid phone no is required")
        if not address:
            raise ValueError("Cutomer address cannot be empty")

        self.name=name
        self.email=email
        self.phone_no=phone_no
        self.address=address


def display_customer_info(self)->str:
    return f"Name:{self.name} Email<{self.email} Phone:<{self.phone_no} Address:<{self.address}"

def update_email(self,new_email: str)->None:
    email=new_email.strip().lower()

    if not email or "@" not in email:
        raise ValueError("A valid new email is required")

    self.email=email

    def __str__(self)->str:
        return self.display_customer_info()

def update_customer_info(self,name: str,  phone_no: None, address: None)->None:
    name= name.strip();
    phone_no= phone_no.strip();
    address= address.strip();
    
    if not name:
       raise ValueError("Cutomer name cannot be empty")
    if not phone_no or len(phone_no)!=11:
        raise ValueError("A valid phone no is required")
    if not address:
        raise ValueError("Cutomer address cannot be empty")
        

