import csv

filmes = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("filmes.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',)
    for lista in filmes:
        spamwriter.writerow(lista)