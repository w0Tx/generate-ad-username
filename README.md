# Why ?

This script has been made for quick creation of usernames to use against AD when you only have the names and surnames for OSCP, Labs... 

It's not perfect, feel free to modify it.

Naming convention can be found there : https://book.hacktricks.xyz/windows/active-directory-methodology#cheat-sheet

```
NameSurname
Name.Surname
NamSur (3letters of each)
Nam.Sur
NSurname
N.Surname
SurnameName
Surname.Name
SurnameN
Surname.N
```

# How ?

Input names should be seperated by ','.

```
test,test2
test3,test4
```

Then : `python3 ADGenerator.py names.txt`

Example of output : 

```
metodijelizabeta
metodij-elizabeta
metodij.elizabeta
meteli
met-eli
met.eli
melizabeta
m-elizabeta
m.elizabeta
elizabetametodij
elizabeta-metodij
elizabeta.metodij
elimet
eli-met
eli.met
emetodij
e-metodij
e.metodij
elizabetam
elizabeta-m
elizabeta.m
```