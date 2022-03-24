from ast import Import
import chunk
from cmath import e
from re import A, I


Pile=[1,3,4]
def empile(elt):
     global Pile
     Pile.append(elt)
empile(5)
print("la pile aprés avoir empilé : ",Pile)
empile(6)
print("la pile aprés avoir empilé : ",Pile)
def depile():
    global Pile
    return Pile.pop(-1)
valeur_dep=depile()
print("la valeur depilée : ",valeur_dep)
print("la pile aprés avoir depilé : ",Pile)
def pile_est_vide():
      if Pile==[]:
          return True
      else:
          return False
test_pile=pile_est_vide()
print(test_pile)
print("#empiler une pile vide")
Pile=[]
empile(5)
empile(7)
empile(2)
empile(4)
print(Pile)
depile()
empile(1)
empile(8)
empile(3)
print(Pile)
valeur_dep=depile()
print(valeur_dep)
print(Pile)
print("#test si un element appartient a une pile ou non? ")
Pile=[12,3,4]
def pile_contient(element):
       if element in Pile:
           return True
       else:
            return False
test_elt=pile_contient(4)
print(test_elt)
print("#sommme des els de la pile")
Pile=[1,3,7,4,5,7]
def sommme_elts():
    return sum(Pile)
s_elts=sommme_elts()
print(s_elts)
print("#suppression de l'avant darnier element ")
Pile=[5]
def avant_dar_elt():
    
        if len(Pile)>1:
            return Pile[-2]
        else:
            return None 
print(avant_dar_elt())
#la methode split()
def ma_chaine(ch,sep):
    b=ch.split(sep)
    print(b)
ma_chaine("asj;ddj;asss",";")
#la méthode join()
def jointure(taille,sep):
    l=[]
    for i in range(taille):
        l.append(input())
    j=sep.join(l)
    print(j)
#jointure(2," ")
#la méthode isdigit()
def chaine_to_entier(ch):
    if ch.isdigit():
        a=int(ch)
        print("le valeur est : ",a)
    else :
          print("la chaine saisie n'est pas un nombre ")
chaine_to_entier("263")
#gare de triage 
def tri_wagons(train): 
    def empiler(elt):
             return Pile.append(elt)
    Pile=[]
    for i in train.split():
        if i.isdigit():
            empiler(i)  
    for i in train.split():
        if not i.isdigit():
            empiler(i)
    train = Pile 
    tri = " ".join([str(wagon) for wagon in train])
    return tri
print(tri_wagons(train=("A 4 C 4 B 14")))

#Calculatrice polonaise 
def operation(x,y,op):
    if op=="+":
        return x+y
    elif op=="*":
        return x*y
    else :
        pass
print(operation(2,3,"*"))
def Calculatrice_polonaise(exp):
    def depile():
           return Pile.pop()
    Pile=[]
    for i in exp.split():
        if i.isdigit():
               Pile.append(i)
        if i=="+" :
                 a=depile()
                 b=depile()
                 res = int(a) + int(b)
                 return res
        if  i=="*":
               a=depile()
               b=depile()
               res = int(a) * int(b)
               return res
    return Pile.append(res)
r=Calculatrice_polonaise("2 3 4 + +")
print(r)




        
    








    

