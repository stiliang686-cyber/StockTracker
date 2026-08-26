import json
import os

print("===== STOCK TRACKER =====")
print()

choice = 0
stocks = []

def save_portfolio():
    with open("portfolio.json", "w") as file:
        json.dump(stocks, file)

    print("Портфолиото беше запазено успешно!")

def load_portfolio():
    global stocks

    if os.path.exists("portfolio.json"):
        with open("portfolio.json", "r") as file:
            stocks = json.load(file)

        print("Портфолиото беше заредено успешно!")
    else:
        print("Все още няма запазено портфолио.")


def portfolio_value():
    total = 0

    for stock in stocks:
        stock_value = stock["cena"] * stock["broi"]
    
        total += stock_value 

    return total 

def portfolio_profit():
    total_earnings = 0 
    total_invested = 0 

    for stock in stocks:
        profit_per_share = stock["cena"] - stock["buy_price"]
        total_earnings += profit_per_share * stock["broi"]
        total_invested += stock["buy_price"] * stock["broi"]

    if total_invested == 0: 
        profit_percent = 0
    else:
        profit_percent = (total_earnings / total_invested) * 100

    return total_earnings, profit_percent

def portfolio_summary():
    total = portfolio_value()
    profit, profit_percent = portfolio_profit()
    positions = len(stocks)

    return total, profit, profit_percent, positions

def sell_stock(): 
    tiker = input("Въведи тикер: ").strip().upper() 
    found = False 
    for stock in stocks: 
        if stock["tiker"] == tiker:
            found = True 

            while True: 
                try:
                    sell_amount = int(input("Колко акции искаш да продадеш?: "))
                    if sell_amount <= 0:
                        print("Невалидно количество")
                        continue 

                    elif sell_amount > stock["broi"]:
                        print("Нямаш достатъчно акции! Въведеното количество е по-голямо от наличното.")

                    else:  
                        stock["broi"] -= sell_amount 
                        print("Акциите бяха продадени успешно!")
                        break 
                except:
                    print("Моля, въведете валидно количество!")
                

    if not found:
        print( "Акцията не беше намерена!")



def buy_stock():
    tiker = input("Въведи тикер: ").strip().upper()
    found = False 
    for stock in stocks:
        if stock["tiker"] == tiker:
            found = True 

            while True: 
                try:
                    buy_amount = int(input("Колко акции искаш да купиш?: "))
                    if buy_amount <= 0: 
                        print("Моля, въведете валидно количество!")
                        continue  
                except:
                    print("Моля, въведете валидно количество!")

                stock["broi"] += buy_amount
                print("Акциите бяха добавени успешно!")
                break 
            
    if not found:
        print("Акцията не беше намерена!")




def show_stocks():
    if len(stocks) == 0:
        print("Няма добавени акции.")
    else:
        for stock in stocks:
            print("====================")
            print("Тикер:", stock["tiker"])
            print("Цена:", stock["cena"])
            print("Цена на покупка:", stock["buy_price"])
            print("Брой:", stock["broi"])
            print("====================")

def delete_stock():
    while True:
        try:
            stock_number = int(input("Въведи номер на акцията: "))
            break
        except:
            print("Моля, въведете валиден номер!")

    index = stock_number  - 1
    
    if index < 0 or index >= len(stocks):
        print("Невалиден номер!")
        return 
    else:
        stock = stocks[index]
    while True:
        confirmation = input("Сигурни ли си? (да/не): ").strip().lower()
        if confirmation == "да" or confirmation == "yes": 
            stocks.remove(stock)
            print("Акцията беше изтрита!")
            break 
        elif confirmation == "не" or confirmation == "no":
            print("Изтриването беше отменено!")
            break
        else: 
            print("Моля, въведете 'да' 'не' 'yes' или 'no' .")


def add_stock():
    tiker = input("Въведи тикер: ").strip().upper()

    while True:
        try:
            cena = float(input("Въведи цена на тикера: "))
            break 
        except:
            print("Моля, въведете цена!")

    while True:
        try:
            buy_price = float(input("Въведи цена на покупка: "))
            break
        except:
            print("Моля, въведете валидна покупна цена!")

    while True:
            try:
                broi = int(input("Въведи броят им: "))
                if broi <= 0:
                    print("Невалидно количество!")
                    continue 
                break
            except:
                print("Моля, въведете брой!")

    new_stock = {
        "tiker": tiker,
        "cena": cena,
        "buy_price": buy_price,
        "broi": broi,
    }

    found = False 
    
    for stock in stocks: 
        if stock["tiker"] == tiker: 
            print("Този тикер вече съществува")
            found = True 
            break 
    
    if not found: 
        stocks.append(new_stock)
        print("Акцията е добавена!")

def edit_stock():
    edit_tiker = input("Коя акция искаш да редактираш?: ").strip().upper()
    found = False

    for stock in stocks:
        if stock["tiker"] == edit_tiker:
            found = True 

            print("1. Цена")
            print("2. Цена на покупка")
            print("3. Брой")
            
            while True:
                try:
                    edit_choice = int(input("Какво искаш да редактираш?: "))
                    if edit_choice == 1 or edit_choice == 2 or edit_choice == 3:
                        break 
                    else:
                        print("Невалиден избор!")
                except:
                    print("Моля, въведете валиден избор!")

            if edit_choice == 1:
                while True:
                    try:
                        edit_cena = float(input("Въведи новата цена: "))
                        break 
                    except:
                        print("Моля, въведете валидна цена!")
                    
                stock["cena"] = edit_cena 
                print("Акцията беше редактирана успешно!")

            elif edit_choice == 2:
                            while True:
                                try:
                                    edit_buy_price = float(input("Въведи новата цена на покупката: "))
                                    break
                                except:
                                    print("Моля, въведете валидна цена на покупката!")
                            stock["buy_price"] = edit_buy_price
                            print("Акцията беше редактирана успешно!")
            

            elif edit_choice == 3:

                while True:
                    try:
                        edit_broi = int(input("Въведи новият брои: "))
                        break
                    except:
                        print("Моля, въведете валиден брой!")

                stock["broi"] = edit_broi
                print("Акцията беше редактирана успешно!")

            
    if not found:
        print("Акцията не беше намерена.")

def portfolio_status():
    total = portfolio_value() 

    if len(stocks) == 0: 
        return 0, "Няма добавени акции."

    if total > 10000:
        status = "Портфолиото е над 10 000!"
    else:
        status = "Портфолиото е под или равно на 10 000!"

    return total, status

def search_stock():
    search_tiker = input("Въведи тикер за търсене: ").strip().upper()
    found = False

    for stock in stocks:
        if stock["tiker"] == search_tiker:
            found = True

            print("====================")
            print("Тикер:", stock["tiker"])
            print("Цена:", stock["cena"])
            print("Брой:", stock["broi"])
            print("====================")

            break

    if not found:
        print("Акцията не беше намерена.")


while choice != 12:
    print("1. Добави акция")
    print()
    print("2. Купи акции")
    print()
    print("3. Продай акции")
    print()
    print("4. Покажи акции")
    print()
    print("5. Премахване на акция")
    print() 
    print("6. Редактирай акция")
    print() 
    print("7. Преглед на портфолиото")
    print()
    print("8. Търси акция")
    print()
    print("9. Запази портфолиото")
    print()
    print("10. Зареди портфолиото")
    print() 
    print("11. Статус на портфолиото")
    print()
    print("12. Изход")

    while True:
        try:
            choice = int(input("Избери опция: "))
            break
        except:
            print("Моля, въведете валиден избор!")

    if choice == 1:
        add_stock()

    elif choice == 2:
        buy_stock()

    elif choice == 3:
        sell_stock() 

    elif choice == 4:
        show_stocks() 

    elif choice == 5:
        delete_stock()

    elif choice == 6:
        edit_stock() 

    elif choice == 7:
        total, profit, profit_percent, positions = portfolio_summary() 
        print("Обща стойност на портфолиото:", total)
        print("Обща Печалба/загуба %:", profit)
        print(f"Процентна печалба: {profit_percent:.2f}%")
        print("Брой позиции:", positions)
        
    elif choice == 8:
        search_stock() 
        
    elif choice == 9:
        save_portfolio()

    elif choice == 10:
        load_portfolio()

    elif choice == 11:
        total, status = portfolio_status() 
        print("Стойност:", total) 
        print("Статус:", status)

    elif choice == 12:
        print("Изход")
        break

    else: 
        print("Невалиден избор!")