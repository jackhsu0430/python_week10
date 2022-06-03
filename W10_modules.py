import datetime

# stock
class Stock():

    def __init__(self, stock_id, investor_id, stocksymb, share_num, purchase_price, current_value, year, month, date):
        self.stock_id = stock_id
        self.investor_id = investor_id
        self.stocksymb = stocksymb
        self.share_num = share_num
        self.purchase_price = round(purchase_price, 2)
        self.current_value = round(current_value, 2)
        self.purchase_date = datetime.datetime(year, month, date)
        ####
        self.profit = (self.current_value - self.purchase_price ) * self.share_num



    def print_data(self):
        print("{:<15} {:<10} {:<10} {:<10} ${:<10} ${:<10} {}".format(self.investor_id,
                                                                        self.stock_id,
                                                                        self.stocksymb,
                                                                        self.share_num,
                                                                        self.purchase_price,
                                                                        self.current_value,
                                                                        self.purchase_date.strftime("%m/%d/%Y")))
# investor
class Investor():
    def __init__(self, investor_id, firstname, lastname, street, city, state, zip, phone):
        self.investor_id = investor_id
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone

    def print_data(self):
        print("-" * 100)
        print("Investor Information: ")
        print("-" * 100)
        print(f"{self.firstname} {self.lastname}")
        print(f"{self.street}, {self.city}, {self.state} ,{self.zip}")
        print(f"{self.phone}")
        print(f"Investor Id: {self.investor_id}")
        print("-" * 100)

# bond
class Bond(Stock):
    def __init__(self, stock_id, investor_id, stocksymb, share_num, purchase_price, current_value, year, month, date, coupon, yield_rate):
        super().__init__(stock_id, investor_id, stocksymb, share_num, purchase_price, current_value, year, month, date)
        self.coupon = coupon
        self.yield_rate = yield_rate
    
    def print_data(self):
        print("{:<15} {:<10} {:<10} {:<10} {:<10} ${:<10} {:<15} ${:<10} {}%".format( self.investor_id, 
                                                                            self.stock_id,
                                                                            self.stocksymb,
                                                                            self.share_num,
                                                                            self.coupon,
                                                                            self.purchase_price,
                                                                            self.purchase_date.strftime("%m/%d/%Y"),
                                                                            self.current_value,
                                                                            self.yield_rate))

class StockTable():
    def __init__(self):
        self.table = []
    
    def add(self, stock):
        self.table.append(stock)

    def print_data(self):
        print("Stock Holdings: ")
        print("-"* 100)
        print ("{:<15} {:<10} {:<10} {:<10} {:<10}  {:<10} {:<10} ".format("Investor_id", "Stock_id", 'Stock','Share','Purchase' , "Current", 'Purchase'))
        print ("{:<15} {:<10} {:<10} {:<10} {:<10}  {:<10} {:<10} ".format("", "", 'Symbol','#','Price', "Value", "Date"))
        print("-"* 100)

        for stock in self.table:
            stock.print_data()

        print("-" * 100)


        
class BondTable(StockTable):
    def __init__(self):
        super().__init__()

    def print_data(self):
        print("Bond Holdings: ")
        print("-" * 120)

        print ("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {}".format("Investor_id", "Bond_id", 'Bond','Quantity', 'Coupon' , "Purchase", 'Purchase', "Current", "Yield"))
        print ("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {}".format("", "", 'Symbol','','', "Price", "Date", "Price", "Rate"))

        print("-" * 120)

        for bond in self.table:
            bond.print_data()

        print("-" * 120)