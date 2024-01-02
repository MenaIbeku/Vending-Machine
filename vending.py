# # Author   : Mena Ibeku
# # Email    : cibeku@umass.edu
# # Spire ID : 34151261

class VendingMachine:
    def __init__(self):
        self.snacks = {}  
        self.customer_balance=0.0
        self.total_sales=0.0
        self.sales_history=[]
        


    def list_items(self):
        available_snacks=[]
        for i in self.snacks:
            if self.snacks[i]['quantity']>=1:
                available_snacks.append(i)
            else:
                continue
        if len(available_snacks)==0:
            print("No items in the vending machine")
        else:
            print('Available items:')
            sorted_dict=sorted(self.snacks.keys())
            for snack_name in (sorted_dict):
                price= self.snacks[snack_name]['price'] 
                quantity=self.snacks[snack_name]['quantity']
                print(f"{snack_name} (${price}): {quantity} available")
            # print(empty_str.strip())

    def add_item(self, name, price, quantity):
        if name in self.snacks:
            self.snacks[name]['price'] = price
            self.snacks[name]['quantity'] += quantity
        else:
            self.snacks[name]= {'price': price, 'quantity': quantity}
        
        print(f"{quantity} {name}(s) added to inventory")
    
    def insert_money(self,dollar_amount):
        if dollar_amount==1 or dollar_amount==2 or dollar_amount==3:
            self.customer_balance+=dollar_amount
            print(f'Balance: {self.customer_balance:.2f}')
        else:
            print('Invalid amount')

    def purchase(self, snack_name):
        if snack_name not in self.snacks:
            print('Invalid item')
        elif self.snacks[snack_name]['quantity']==0:
            print(f'Sorry {snack_name} is out of stock')
        elif self.customer_balance<self.snacks[snack_name]['price']:
            print(f'Insufficient balance. Price of {snack_name} is {self.snacks[snack_name]["price"]}')
        else:
            self.snacks[snack_name]['quantity']-=1
            self.customer_balance = round(self.customer_balance- self.snacks[snack_name]['price'], 2)
            self.total_sales = round(self.total_sales + self.snacks[snack_name]['price'], 2)
            sales={}
            sales[snack_name]=self.snacks[snack_name]['price']
            self.sales_history.append(sales)
            print(f'Purchased {snack_name}\nBalance: {self.customer_balance}')

    def display_change(self):
        if self.customer_balance>0:
            print(f'Change: {self.customer_balance}')
            self.customer_balance=0.0
        else:
            print('No change')
    
    def get_item_price(self, name):
        if name in self.snacks:
            return self.snacks[name]['price']
        else:
            print('Invalid item')
    
    def empty_inventory(self):
        self.snacks={}
        print ('Inventory cleared')

    def get_total_sales(self):
        return self.total_sales
    
    def get_item_quantity(self, snack_name):
        if snack_name in self.snacks:
            return self.snacks[snack_name]['quantity']
        else:
            print('Invalid item')
    
    def remove_item(self, snack_name):
        if snack_name in self.snacks:
            del self.snacks[snack_name]
            print(f'{snack_name} removed from inventory')
        else:
            print('Invalid item')

    def stats(self,N):
        if len(self.sales_history)==0:
            print('No sale history in the vending machine')
        else:
            if len(self.sales_history)>=N:
                recent_sales=self.sales_history[-N:]
                new_list=[]
                for i in recent_sales:
                    for key in i:
                        new_list.append(key)
                sorted_sales=((sorted(new_list)))
                print(f'Sale history for the most recent {N} purchase(s):')
                
                empty_dict={}
                for i in sorted_sales:
                    if i in empty_dict:
                        empty_dict[i]+=1
                    else:
                        empty_dict[i]=1
                for i, num in empty_dict.items():
                    for m in self.sales_history:
                        for j in m:
                            if i==j:
                                total_sales=num*m[j]
                    print(f'{i}: ${total_sales} for {num} purchase(s)')

            elif len(self.sales_history)<N:
                N=len(self.sales_history)
                recent_sales=self.sales_history[-N:]
                new_list=[]
                for i in recent_sales:
                    for key in i:
                        new_list.append(key)
                sorted_sales=((sorted(new_list)))
                print(f'Sale history for the most recent {N} purchase(s):')
                
                empty_dict={}
                for i in sorted_sales:
                    if i in empty_dict:
                        empty_dict[i]+=1
                    else:
                        empty_dict[i]=1
                for i, num in empty_dict.items():
                    for m in self.sales_history:
                        for j in m:
                            if i==j:
                                total_sales=num*m[j]
                    print(f'{i}: ${total_sales} for {num} purchase(s)')



# # Create a new vending machine
# vending_machine = VendingMachine()

# # Add some items to the inventory
# vending_machine.add_item('Soda', 1.50, 5)
# vending_machine.add_item('Chips', 0.75, 10)
# vending_machine.add_item('Candy', 0.50, 15)

# # Show the available items
# vending_machine.list_items()

# # Insert some coins
# vending_machine.insert_money(1.00)
# vending_machine.insert_money(1.00)

# # Purchase an item
# vending_machine.purchase('Soda')

# # Get the price of an item
# print(vending_machine.get_item_price('Chips'))

# # Purchase another item
# vending_machine.purchase('Chips')

# # Get the total sales
# print(vending_machine.get_total_sales())

# # Insert some coins
# vending_machine.insert_money(3.00)
# vending_machine.insert_money(3.00)
# vending_machine.insert_money(3.00)

# # Purchase another item
# vending_machine.purchase('Chips')
# vending_machine.purchase('Chips')
# vending_machine.purchase('Chips')
# vending_machine.purchase('Candy')
# vending_machine.purchase('Candy')

# # print stats
# vending_machine.stats(3)
# vending_machine.stats(5)
# vending_machine.stats(10)

# # Remove an item
# vending_machine.remove_item('Candy')

# # Show the available items again
# vending_machine.list_items()

# # Get the quantity of an item
# print(vending_machine.get_item_quantity('Gum'))

# # Empty the inventory
# vending_machine.empty_inventory()

# # Show the available items again
# vending_machine.list_items()
vm = VendingMachine()
vm.add_item("Rfndcur", 0.71, 20)
vm.add_item("Pcibna", 1.11, 25)
vm.add_item("Jmkfn", 1.52, 30)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.purchase("Jmkfn")
vm.purchase("Jmkfn")
vm.purchase("Rfndcur")
vm.purchase("Jmkfn")
vm.purchase("Jmkfn")
vm.purchase("Pcibna")
vm.purchase("Rfndcur")
vm.purchase("Rfndcur")
vm.purchase("Rfndcur")
vm.purchase("Rfndcur")
vm.purchase("Pcibna")
vm.purchase("Jmkfn")
vm.purchase("Rfndcur")
vm.purchase("Pcibna")
vm.purchase("Rfndcur")
vm.purchase("Pcibna")
vm.purchase("Rfndcur")
vm.purchase("Jmkfn")
vm.purchase("Rfndcur")
vm.purchase("Pcibna")
vm.empty_inventory()
vm.stats(5)



   
               



    








            

