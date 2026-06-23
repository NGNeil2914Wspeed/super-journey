import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Restauraunt Order Managment System")
root.geometry("700x700")
root.config(background="red")

items_and_amounts = {"Pizza": 0, "Burger": 0, "Pasta": 0, "Lemonade": 0, "Sprite": 0, "Sizziler": 0, "Taco": 0, "Sushi": 0, "Noodles": 0, "Fried Rice": 0} 
items_and_prices = {"Pizza": 20, "Burger": 10, "Pasta": 15, "Lemonade": 3, "Sprite": 4, "Sizziler": 20, "Taco": 5, "Sushi": 20, "Noodles": 20, "Fried Rice": 20}

total_price = 0
bill_price = 0

def add_item(item):
    global total_price, bill_price
    total_price += items_and_prices[item]
    bill_price += items_and_prices[item]
    items_and_amounts[item] += 1

def discount(amount):
    global bill_price
    bill_price -= (bill_price*amount)//100

def confirm_payment():
    global total_price, bill_price
    
    toplevel = tk.Toplevel()
    toplevel.config(bg="white")
    
    popup_x = root.winfo_x() + 50
    popup_y = root.winfo_y() + 50
    toplevel.geometry(f"+{popup_x}+{popup_y}")
    
    bill_text = (
        f"Item      Amount bought       Cost (per item)\n\n"
        f"Pizza            {items_and_amounts['Pizza']}            ${items_and_prices['Pizza']}\n"
        f"Burger           {items_and_amounts['Burger']}            ${items_and_prices['Burger']}\n"
        f"Pasta            {items_and_amounts['Pasta']}            ${items_and_prices['Pasta']}\n"
        f"Lemonade         {items_and_amounts['Lemonade']}            ${items_and_prices['Lemonade']}\n"
        f"Sprite           {items_and_amounts['Sprite']}            ${items_and_prices['Sprite']}\n"
        f"Sizziler         {items_and_amounts['Sizziler']}            ${items_and_prices['Sizziler']}\n"
        f"Taco             {items_and_amounts['Taco']}            ${items_and_prices['Taco']}\n"
        f"Sushi            {items_and_amounts['Sushi']}            ${items_and_prices['Sushi']}\n"
        f"Noodles          {items_and_amounts['Noodles']}            ${items_and_prices['Noodles']}\n"
        f"Fried Rice       {items_and_amounts['Fried Rice']}            ${items_and_prices['Fried Rice']}\n\n"
        f"Total Bill: ${bill_price}"
    )
    
    bill = tk.Label(toplevel, text=bill_text, font=("Courier", 12), justify="left", bg="white", fg="black")
    bill.pack(padx=20, pady=20)
    
    toplevel.lift()
    toplevel.attributes("-topmost", True)
    
    if bill_price >= 500:
        messagebox.showinfo("Card Insert Required", "You must swipe your card for any orders that are more than $499")
    else:
        messagebox.showinfo("Card Tap Requires", "You must tap your card for payment")
        
    toplevel.after(10000, toplevel.destroy)
    total_price += bill_price
    bill_price = 0

title_label = tk.Label(root, text="Restaurant Order managment System", fg="yellow", bg="red", font=("Arial", 30))
title_label.pack(pady=10, padx=10)

step1_frame = tk.Frame(root, background="red")
step1_frame.pack(side="left", padx=40, pady=20)

step2_frame = tk.Frame(root, background="red")
step2_frame.pack(side="right", padx=40, pady=20)

title_for_frame_1 = tk.Label(step1_frame, text="Items", bg="red", fg="black", font=("Arial", 20))
title_for_frame_1.grid(column=0, row=0, columnspan=2)

title_for_frame_2 = tk.Label(step2_frame, text="Price finilization", bg="red", fg="black", font=("Arial", 20))
title_for_frame_2.grid(column=0, row=0)

burger_button = tk.Button(step1_frame, text="Burger", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Burger"), height=5, width=10)
burger_button.grid(column=0, row=1, pady=10, padx=10)

pizza_button = tk.Button(step1_frame, text="Pizza", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Pizza"), height=5, width=10)
pizza_button.grid(column=0, row=2, pady=10, padx=10)

pasta_button = tk.Button(step1_frame, text="Pasta", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Pasta"), height=5, width=10)
pasta_button.grid(column=0, row=3, pady=10, padx=10)

sizziler_button = tk.Button(step1_frame, text="Sizziler", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Sizziler"), height=5, width=10)
sizziler_button.grid(column=0, row=4, pady=10, padx=10)

noodles_button = tk.Button(step1_frame, text="Noodles", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Noodles"), height=5, width=10)
noodles_button.grid(column=0, row=5, pady=10, padx=10)

fried_rice_button = tk.Button(step1_frame, text="Fried Rice", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Fried Rice"), height=5, width=10)
fried_rice_button.grid(column=1, row=1, pady=10, padx=10)

taco_button = tk.Button(step1_frame, text="Taco", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Taco"), height=5, width=10)
taco_button.grid(column=1, row=2, pady=10, padx=10)

sushi_button = tk.Button(step1_frame, text="Sushi", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Sushi"), height=5, width=10)
sushi_button.grid(column=1, row=3, pady=10, padx=10)

lemonade_button = tk.Button(step1_frame, text="Lemonade", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Lemonade"), height=5, width=10)
lemonade_button.grid(column=1, row=4, pady=10, padx=10)

sprite_button = tk.Button(step1_frame, text="Sprite", font=("Arial", 10), bg="white", fg="black", command=lambda: add_item("Sprite"), height=5, width=10)
sprite_button.grid(column=1, row=5, pady=10, padx=10)

discount20button = tk.Button(step2_frame, text="20% off", font=("Arial", 10), bg="white", fg="black", command=lambda: discount(20), height=5, width=10)
discount20button.grid(column=0, row=1, pady=10, padx=10)

discount25button = tk.Button(step2_frame, text="25% off", font=("Arial", 10), bg="white", fg="black", command=lambda: discount(25), height=5, width=10)
discount25button.grid(column=0, row=2, pady=10, padx=10)

discount50button = tk.Button(step2_frame, text="50% off", font=("Arial", 10), bg="white", fg="black", command=lambda: discount(50), height=5, width=10)
discount50button.grid(column=0, row=3, pady=10, padx=10)

discount75button = tk.Button(step2_frame, text="75% off", font=("Arial", 10), bg="white", fg="black", command=lambda: discount(75), height=5, width=10)
discount75button.grid(column=0, row=4, pady=10, padx=10)

discount90button = tk.Button(step2_frame, text="90% off", font=("Arial", 10), bg="white", fg="black", command=lambda: discount(90), height=5, width=10)
discount90button.grid(column=0, row=5, pady=10, padx=10)

confirm_payment_btn = tk.Button(step2_frame, text="Confirm Payment", font=("Arial", 10), bg="yellow", fg="black", command=confirm_payment, height=5, width=15)
confirm_payment_btn.grid(column=1, row=3, pady=10, padx=10)

root.mainloop()
