num = input("Bir eded daxil et: ")

# ededi tərsinə çeviririk
reversed_num = num[::-1]

# Nəticəni çap edirik
print("Tərsinə çevrilmiş eded:", reversed_num)

# Əgər eded palindromdursa, bildiririk
if num == reversed_num:
    print("Bu eded palindromdur!")
else:
    print("Bu eded palindrom deyil.")
