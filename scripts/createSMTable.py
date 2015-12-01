#!/bin/python
#-!- encoding:utf8 -!-

# !define SOM_ConduireRdv ConduireRdv(idContact)\n: void # LINE TO PARSE EXAMPLE

# PRINT HEAD
print("");
print("\\begin{table}[H]");
print("\t\\centering");
print("\t\\resizebox{\\columnwidth}{!}{");
print("\t\t\\begin{tabular}{p{1cm}|p{5cm}p{6cm}p{6cm}}");
print("\t\t\tNuméro SM & Nom & Arguments & Valeur de retour \\\\ \\hline");
# PRINT CONTENT
COUNTER=0;
with open('../diagram/variables.puml', 'r') as f:
    for l in f:
        if "!define SM_" in l:
            print("\t\t\t%s & %s & %s & %s \\\\ \\hline" % (COUNTER, l.split(' ')[2].split('(')[0].replace("\\n", ""), l.split('(')[1].split(')')[0].replace("\\n", " "), l.split(':')[1].replace('\n','').replace("\\n", "")));
            COUNTER+=1;
# PRINT END
print("\t\t\\end{tabular}");
print("\t}");
print("\t\\caption{Tableau de synthèse des SMA}");
print("\\end{table}");
print("");

