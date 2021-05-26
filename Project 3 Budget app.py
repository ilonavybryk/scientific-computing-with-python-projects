class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description = None):
        if description == None:
            self.ledger.append({"amount": float(amount), "description": ""})
        else:
            self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount, description = None):
        if self.check_funds(amount) ==True:
            if description == None:
                self.ledger.append({"amount": -(float(amount)), "description": ""})
            else:
                self.ledger.append({"amount": -(float(amount)), "description": description})
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_balance(self):
        current_balance = 0
        for items in self.ledger:
            current_balance = current_balance + items["amount"]
        return current_balance

    def transfer(self, amount, d_bud_category):
        if self.check_funds(amount) ==True:
            self.withdraw(amount, f"Transfer to {d_bud_category.category}")
            d_bud_category.deposit(amount, f"Transfer from{self.category}")
            return True
        else:
            return False
    def __str__(self):
        category = self.category
        title = category.center(30,"*")
        for items in self.ledger:
            try:
                left = items['description'][0:23]
            except:
                left = ""
            right = str("{:.2f}".format(items['amount']))
            title += f"\n{left:<23}{right:>7}"
        title += "\nTotal: "+ str(self.get_balance())
        return title

def create_spend_chart(categories):
    category_names = []
    spend = []
    spend_percentages =[]

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total = total- item['amount']
    spend.append(round(total, 2))
    category_names.append(category.category)
    
    for amount in spend:
        spend_percentages.append(round(amount / sum(spend), 2)*100)
    
    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)
    
    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spend_percentages:
            if percent >= label:
                graph += "o  " 
            else:
                graph += "   "
        graph += "\n"
    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "
    
    longest_name_length = 0
    
    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    
    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length-1:
            graph += "\n     "
    return(graph)

