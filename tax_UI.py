import tkinter as tk


#FUNTIONS
#calculation function
def calc_tax(stay_price, stay_length, minor_count, adult_count):

	#defining daily prices
	daily_price = stay_price/stay_length
	daily_price_per_capita = daily_price/(minor_count+adult_count)

	#making sure per capita price doesn't exceed 2.53 euros
	per_adult_tax = (0.03*daily_price_per_capita)*(1.1)
	if per_adult_tax>2.53:
		per_adult_tax = 2.53
	else:
		per_adult_tax=int(per_adult_tax)
	#calculating the full price of the tax for the stay
	total_tax = int(adult_count*per_adult_tax)
	print(total_tax, per_adult_tax)
	return per_adult_tax, total_tax*stay_length

def give_result():
	#fetching user input
	stay_price = stay_price_var.get()
	stay_length = stay_length_var.get()
	minor_count = minor_count_var.get()
	adult_count = adult_count_var.get()
	#making sure values are legal
	can_calc=True
	if stay_price == 0:
		stay_price_label["fg"] = "red"
		can_calc=False
	else: stay_price_label["fg"] = "black"

	if stay_length ==0:
		stay_length_label["fg"] = "red"
		can_calc=False
	else: stay_length_label["fg"] = "black"

	if adult_count ==0:
		adult_count_label["fg"] = "red"
		can_calc=False
	else: adult_count_label["fg"] = "black"

	if can_calc==False:return



	global total_tax_var
	global per_adult_tax_var
	print(total_tax_var.get(), per_adult_tax_var.get())
	tax1, tax2 = calc_tax(stay_price, stay_length, minor_count, adult_count)
	per_adult_tax_var.set("{}€".format(tax1))
	total_tax_var.set("{}€".format(tax2))
	print(total_tax_var.get(), per_adult_tax_var.get())



#DEFINING GLOBAL VARIABLES
TITLE = "Outil de calcul pour la taxe de séjour."

#SETTING UP THE WINDOW
main_window = tk.Tk()
main_window.title(TITLE)
main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0, weight=1)

#DEFINING WIDGETS
#title_label = tk.Label(main_window, text=TITLE)
#defining stay vars
stay_length_var= tk.IntVar()
adult_count_var= tk.IntVar()
minor_count_var = tk.IntVar()
stay_price_var = tk.DoubleVar()
per_adult_tax_var = tk.StringVar()
total_tax_var = tk.StringVar()
#making labels
stay_length_label = tk.Label(main_window, text="Durée du séjour")
adult_count_label = tk.Label(main_window, text="Nombre d'adultes")
minor_count_label = tk.Label(main_window, text="Nombre d'enfants")
stay_price_label  = tk.Label(main_window, text="Prix du séjour", fg="black")
per_adult_tax_name_label = tk.Label(main_window, text="Prix unitaire par jour")
total_tax_name_label = tk.Label(main_window, text="Prix total pour le séjour")
per_adult_tax_label = tk.Label(main_window, textvariable=per_adult_tax_var)
total_tax_label = tk.Label(main_window, textvariable=total_tax_var)
#making entries
stay_length_entry = tk.Entry(main_window, textvariable=stay_length_var, width=5)
adult_count_entry = tk.Entry(main_window, textvariable=adult_count_var, width=5)
minor_count_entry = tk.Entry(main_window, textvariable=minor_count_var, width=5)
stay_price_entry  = tk.Entry(main_window, textvariable=stay_price_var, width=5)
#making buttons
validate_button = tk.Button(text="Calculer", command=give_result)
quit_button = tk.Button(text="Quitter", command=main_window.quit)

#CREATING WIDGETS
#packing labels
#title_label.grid(row=1, column=1)
stay_length_label.grid(row=2, column=1, padx=30, pady=5)
adult_count_label.grid(row=3, column=1, padx=30, pady=5)
minor_count_label.grid(row=4, column=1, padx=30, pady=5)
stay_price_label.grid(row=5, column=1, padx=30, pady=5)
per_adult_tax_name_label.grid(row=6, column=1, padx=30, pady=5)
total_tax_name_label.grid(row=6, column=2, padx=30, pady=5)
per_adult_tax_label.grid(row=7, column=1, padx=30, pady=5)
total_tax_label.grid(row=7, column=2, padx=30, pady=5)
#packing entries
stay_length_entry.grid(row=2, column=2, padx=30, pady=5)
adult_count_entry.grid(row=3, column=2, padx=30, pady=5)
minor_count_entry.grid(row=4, column=2, padx=30, pady=5)
stay_price_entry.grid(row=5, column=2, padx=30, pady=5)
#packing buttons
validate_button.grid(row=8, column=1)
quit_button.grid(row=8, column=2)

#RUNNING THE APP
main_window.mainloop()