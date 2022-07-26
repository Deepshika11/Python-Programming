#2.
class Items:
    
    def __init__(self,n,p,q):
        self.name=n
        self.price=p
        self.quantity=q
    def Purchase(self):
        n=int(input("Enter the number of items to be purchased: "))
        if self.quantity<n:
            print("Not enough items.")
        else:
            self.quantity=self.quantity-n
        
    def increaseStock(self):
        m=int(input("Enter the number of new stocks to be added: "))
        self.quantity=self.quantity+m
    def display(self):
        print("Item Name= ",self.name)
        print("Price= ",self.price)
        print("New Quantity after stock updation= ",self.quantity)
s1=Items('Perfume',350,140)
s1.Purchase()
s1.increaseStock()
s1.display()
