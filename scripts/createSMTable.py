#!/bin/python
#-!- encoding:utf8 -!-

# !define SM_ConduireRdv SM1 - ConduireRdv(idContact)\n: void # LINE TO PARSE EXAMPLE

# PRINT HEAD
print("");
print("\\begin{table}[H]");
print("\t\\noindent\\resizebox{15cm}{!}{");
print("\t\t\\begin{tabular}{P{0.8cm}P{5.5cm}P{6cm}P{6cm}}");
print("\\hline Num & Nom & Arguments & Valeur de retour \\\\ \\hline");
# PRINT CONTENT
COUNTER=0;
with open('../diagram/variables.puml', 'r') as f:
    for l in f:
        if "!define SM_" in l:
            print("\t\t\t%s & %s & %s & %s \\\\ \\arrayrulecolor{lightgray}\\hline" % (COUNTER, l.split(' ')[4].split('(')[0].replace("\\n", ""), l.split('(')[1].split(')')[0].replace("\\n", " "), l.split(':')[1].replace('\n','').replace("\\n", "")));
            COUNTER+=1;
# PRINT END
print("\\arrayrulecolor{black}\\hline")
print("\t\t\\end{tabular}");
print("\t}");
print("\t\\caption{Tableau de synthèse des SMA}");
print("\\end{table}");
print("");

