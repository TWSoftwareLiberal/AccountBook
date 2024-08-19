class AccountBook:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.categories = []
        self.categories_balance = []

    def record_income(self, amount):
        self.balance += amount
        self.display_categories()
        category_choice = int(input("\n請選擇收入分類: "))
        if(category_choice > len(self.categories)):
            print("無此分類")

        self.transactions.append((amount, self.categories[category_choice-1], 'income'))
        self.categories_balance[category_choice-1] += amount
        print("已記錄!")

    def record_expense(self, amount):
        self.balance -= amount
        self.display_categories()
        category_choice = int(input("\n請選擇支出分類: "))
        if(category_choice > len(self.categories)):
            print("無此分類")

        self.transactions.append((amount, self.categories[category_choice-1], 'expense'))
        self.categories_balance[category_choice-1] -= amount
        print("已記錄!")

    def display_balance(self):
        print(f"當前餘額: {self.balance}")

    def display_transactions(self):
        print("記帳記錄:")
        for transaction in self.transactions:
            amount, category, type_ = transaction
            print(f"{type_}: {amount} 分類：{category}")

    def display_categories_balance(self):
        print("記帳分類:")
        i = 0
        for category in self.categories :
            print("%d. %s : %.2f" % (i + 1, category, self.categories_balance[i]))
            i += 1

    def display_categories(self):
        print("記帳分類:")
        i = 1
        for category in self.categories:
            print("%d. %s" % (i, category))
            i += 1

    def add_new_category(self):
        category = input("請輸入要新增的記帳分類: ")
        self.categories.append(category)
        self.categories_balance.append(0)
        print(self.categories_balance)

def main():
    account_book = AccountBook()

    while True:
        print("\n操作目錄:")
        print("1. 記錄收入")
        print("2. 記錄支出")
        print("3. 顯示餘額")
        print("4. 顯示記帳紀錄")
        print("5. 依分類顯示金額")
        print("6. 顯示分類")
        print("7. 新增分類")
        print("8. 退出")

        choice = input("請輸入操作編號: ")

        if choice == '1':
            amount = float(input("請輸入收入金額: "))
            account_book.record_income(amount)
            

        elif choice == '2':
            amount = float(input("請輸入支出金額: "))
            account_book.record_expense(amount)

        elif choice == '3':
            account_book.display_balance()

        elif choice == '4':
            account_book.display_transactions()

        elif choice == '5':
            account_book.display_categories_balance()

        elif choice == '6':
            account_book.display_categories()

        elif choice == '7':
            account_book.add_new_category()

        elif choice == '8':
            print("BYE！")
            

if __name__ == "__main__":
    main()
