import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '?',]

print("Welcome to the PyPassword Generator!")
rg_letters = int(input("How many letters would you like in your password?\n"))
rg_numbers = int(input("How many numbers would you like?\n"))
rg_symbols = int(input("How many symbols would you like?\n"))

letter_mix = random.sample(letters, rg_letters)
number_mix = random.sample(numbers, rg_numbers)
symbol_mix = random.sample(symbols, rg_symbols)
combo_mix = letter_mix + number_mix + symbol_mix
random.shuffle(combo_mix)
generation = "".join(combo_mix)

print("Your new password is: ", generation)
