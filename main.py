#print("hello!")

Saraksts=["Anna", "Bruno", "Centis", "Dace"]
a=str(input("Ievadiet vardu ,ko pielikt sarakstam: "))
print(a)
Saraksts.append(a)
print(Saraksts)
Saraksts.remove("Dace")
print(f'Saraksts bez atteikusas personas {Saraksts}')