from random import choice

name_string = input("Give me everybody's names, seperated by a comma: ")
name_list = name_string.split(",")
bill_payer = choice(name_list)
print(f'{bill_payer} is paying the bill')