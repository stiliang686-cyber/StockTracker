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

def show_stocks():
    if len(stocks) == 0:
        print("Няма добавени акции.")
    else:
        for stock in stocks:
            print("====================")
            print("Тикер:", stock["tiker"])
            print("Цена:", stock["cena"])
            print("Брой:", stock["broi"])
            print("====================")

def delete_stock():
    stock_number = int(input("Въведи номер на акцията: "))
    index = stock_number  - 1
    
    if index < 0 or index >= len(stocks):
        print("Невалиден номер!")
    else:
        stock = stocks[index]
        stocks.remove(stock)
        print("Акцията беше изтрита!")

def add_stock():
    tiker = input("Въведи тикер: ").strip().upper()
    cena = float(input("Въведи цена на тикера: "))
    broi = int(input("Въведи броят им: "))

    new_stock = {
        "tiker": tiker,
        "cena": cena,
        "broi": broi
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

            print("1. цена")
            print("2. брой")

            edit_choice = int(input("Какво искаш да редактираш?: "))

            if edit_choice == 1:
                edit_cena = float(input("Въведи новата цена: "))
                stock["cena"] = edit_cena 
                print("Акцията беше редактирана успешно!")

            elif edit_choice == 2: 
                edit_broi = int(input("Въведи новият брои: "))
                stock["broi"] = edit_broi
                print("Акцията беше редактирана успешно!")
            else:
                print("Невалиден избор!")
            break



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


while choice != 10:
    print("1. Добави акция")
    print()
    print("2. Покажи акции")
    print()
    print("3. Премахване на акция")
    print() 
    print("4. Редактирай акция")
    print() 
    print("5. Обща стойност")
    print()
    print("6. Търси акция")
    print()
    print("7. Запази портфолиото")
    print()
    print("8. Зареди портфолиото")
    print() 
    print("9. Статус на портфолиото")
    print()
    print("10. Изход")

    choice = int(input("Избери опция: "))

    if choice == 1:
        add_stock()

    elif choice == 2:
        show_stocks() 

    elif choice == 3:
        delete_stock()

    elif choice == 4:
        edit_stock() 

    elif choice == 5:
       total =  portfolio_value()
       print("Обща стойност на портфолиото:", total)

    elif choice == 6:
        search_stock() 
        
    elif choice == 7:
        save_portfolio()

    elif choice == 8:
        load_portfolio()

    elif choice == 9:
        total, status = portfolio_status() 
        print("Стойност:", total) 
        print("Статус:", status)

    elif choice == 10:
        print("Изход")
        break

    else: 
        print("Невалиден избор!")