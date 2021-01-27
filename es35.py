#Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo.
#Fornito poi il numero del conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
conti = ["IT 95 A 21378 93490 324958210348", "IT 55 B 45785 98487 853704248930",  "IT 05 C 78423 73891 845285963849"]
saldi = ["12 €", "6000000 €", "550000"]
d = {}

for n in range(len(conti)):
    d[conti[n]] = saldi[n]

conto = input("Inserire il numero di conto: ")

if conto in conti:
    print("Il saldo su questo conto è di", d[conto])
else:
    print("ERRORE: conto non presente nella mappa")
