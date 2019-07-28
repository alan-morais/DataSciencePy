import csv

with open('arquivos/conselho_conferencia.csv', encoding ='utf-8') as entrada:
    ler = csv.reader (entrada)
    for linha in ler:
        print (linha)