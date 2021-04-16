from SerwisPlatnosci import SerwisPlatnosci

class Przelew(SerwisPlatnosci):
    def __init__(self):
        self.from_customer_id=None
        self.from_customer_individual_number = None
        self.from_customer_bank = None
        self.from_customer_value_to_send = None
        self.to_customer_id = None
        self.to_customer_individual_number = None
        self.to_customer_bank = None
        self.to_customer_value_to_send = None
        self.isPossible=None

