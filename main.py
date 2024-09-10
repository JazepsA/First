#print("hello!")
'''
Saraksts=["Anna", "Bruno", "Centis", "Dace"]
a=str(input("Ievadiet vardu ,ko pielikt sarakstam: "))
print(a)
Saraksts.append(a)
print(Saraksts)
Saraksts.remove("Dace")
print(f'Saraksts bez atteikusas personas {Saraksts}')
'''
Vardi=["ANASTASIJA", "VIKTORIJA", "ANNA", "LAURA", "EVELĪNA", "ALISE", "MARTA", "KATRĪNA", "SAMANTA", "ELIZABETE", "PAULA", "ELĪNA", "AMANDA", "DANIELA", "MARIJA", "SOFIJA", "NIKOLA", "DIĀNA", "DARJA", "KSENIJA", "LINDA", "PATRĪCIJA", "ALEKSANDRA", "MADARA", "EMĪLIJA", "KRISTĪNE", "ANNIJA", "VERONIKA", "ELĪZA", "ESTERE", "KRISTIĀNA", "VALĒRIJA", "LĪVA", "IEVA", "SANIJA", "MEGIJA", "KRISTA", "KARĪNA", "ANETE", "JEKATERINA", "SINTIJA", "SABĪNE", "JŪLIJA", "JANA", "ARINA", "ALĪNA", "ANCE", "MILANA", "AGNESE", "KEITA", "LUĪZE", "SANTA", "JEĻIZAVETA", "ELZA", "KITIJA", "LORETA", "KATE", "BEĀTE", "TĪNA", "SINDIJA", "EVA", "LĪGA", "POĻINA", "VALERIJA", "JUSTĪNE", "ALISA", "DANA", "ZANE", "RŪTA", "VANESA", "REBEKA", "LIĀNA", "MONTA", "DĀRTA", "ĒRIKA", "GABRIELA", "RENĀTE", "LIENE", "BEATRISE", "ENIJA", "AGATE", "EVIJA", "ADRIANA", "MARGARITA", "EVITA", "RĒZIJA", "UNA", "ALEKSA", "ALINA", "ANŽELIKA", "MELĀNIJA", "SIMONA"]
b=input('Ievadiet meitenes vardu: ')
x=b.upper()
if x in Vardi:
    print(f"Vārds {x} ir sarakstā ")
else:
    print("Vārda nav saraksta!")
index = Vardi.index(x)
print(f"Vards {x} ir TOP {index}")