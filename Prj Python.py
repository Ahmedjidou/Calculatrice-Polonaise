############################## # Piles - Calculatrice polonaise ##############################
############################## # Activité 1 - Opération sur la pile ##############################
# "pile" est une variable globale
## Question 1 ##
def empile(element): #""" Ajoute un élément au sommet de la pile Entrée : un objet Sortie : rien Action : la pile contient un élément en plus """
            global pile # Pour pouvoir modifier la pile
            pile = pile + [element]
            return None
# Test print("--- Empiler ---") pile = [4,5,6] print('Pile avant :',pile) empile(7) print('Pile après :',pile)
## Question 2 ##
def depile(): #""" Lit l'élément au sommet de la pile et l'enlève Entrée : rien Sortie : l'élément du sommet Action : la pile contient un élément de moins """
            global pile
            sommet = pile[len(pile)-1] 
            pile = pile[0:len(pile)-1]
            return sommet
# Test print("--- Dépiler ---") pile = [4,5,6] print('Pile avant :',pile) val = depile() print('Valeur dépilée :',val,'\nPile après :',pile)
## Question 3 ##
def pile_est_vide():
      #""" Détermine si la pile est vide ou pas Entrée : rien Sortie : vrai/faux Action : ne modifie pas la pile """
        if len(pile) == 0: 
            return True 
        else: 
            return False
# Tests print("--- Tester si pile vide ---")
# Test 1 pile = [4,5,6] vide = pile_est_vide() print(pile,'pile vide ?',vide)
# Test 2 pile = [] vide = pile_est_vide() print(pile,'pile vide ?',vide)

############################## # Piles - Calculatrice polonaise ##############################
############################## # Rappels - Activité 1 ##############################
def empile(element): 
    global pile 
    pile = pile + [element] 
    return None
def depile(): 
    global pile 
    sommet = pile[len(pile)-1] 
    pile = pile[0:len(pile)-1] 
    return sommet
def pile_est_vide(): 
    if len(pile) == 0: 
        return True 
    else: 
        return False
############################## # Activité 2 - Manipulation de la pile ##############################
## Question 1 ##
print("--- Manipulation ---") 
pile = []
empile(5) 
empile(7) 
empile(2) 
empile(4) 
print(pile) 
depile() 
empile(8) 
empile(1) 
empile(3) 
print(pile) 
val = depile() 
print('Valeur :',val)
## Question 2 ##
def pile_contient(element): 
      #""" Détermine si la pile contient l'élément Entrée : rien Sortie : vrai/faux Action : modifie la pile """
        while not pile_est_vide(): 
            el = depile() 
            if el == element: 
                return True # Si on trouve l'élément c'est bon
        return False # On arrive au bas sans trouver l'élément
# Tests 
print("--- Test si pile contient 7 ---")
# Test 1 
pile = [4,5,6] 
print(pile,'pile contient 7 ?',pile_contient(7))
# Test 2 pile = [4,7,12,99] print(pile,'pile contient 7 ? ',pile_contient(7))
## Question 3 ##
def somme_pile():
    #""" Calcule la somme de la pile Entrée : rien Sortie : la somme Action : vide la pile """
        somme = 0
        while not pile_est_vide(): 
            element = depile() 
            somme = somme + element
        return somme
    # Test print("--- Somme des valeurs de la pile ---") pile = [4,5,6] print('La somme de',pile,'est ',somme_pile())
## Question 4 ##
def avant_dernier():
    #""" Renvoie l'avant-dernier élément en bas de la pile Entrée : rien Sortie : l'avant-dernier élément Action : vide la pile """
            dernier = None 
            avant_dernier = None
            while not pile_est_vide(): 
                avant_dernier = dernier # Le dernier devient avant-dernier dernier = depile() # Nouveau dernier
            return avant_dernier
# Tests pile = [4,5,6,13] print('L\'avant-dernier élément de',pile,'est',avant_dernier())
pile = [4,6] 
print('L\'avant-dernier élément de',pile,'est',avant_dernier())
pile = [6] 
print('L\'avant-dernier élément de',pile,'est',avant_dernier())
pile = [] 
print('L\'avant-dernier élément de',pile,'est',avant_dernier())

############################## # Piles - Calculatrice polonaise ##############################
############################## # Rappels - Activité 1 ##############################
def empile(element): 
    global pile 
    pile = pile + [element] 
    return None
def depile(): 
    global pile 
    sommet = pile[len(pile)-1] 
    pile = pile[0:len(pile)-1] 
    return sommet
def pile_est_vide(): 
    if len(pile) == 0: 
        return True 
    else: 
        return False
############################## # Activité 3 - La gare de triage ##############################
def tri_wagons(train): 
# """ Trie les wagons rouges/bleus d'un train Entrée : 
# un train avec des wagons bleus (nombre) et rouges (lettres) Sortie : 
# les wagons triés avec les bleus d'abord et les rouges ensuite Action : utilise une pile """
      global pile # Doit être globale pour pouvoir être modifiée 
      pile = []
      nouv_train = ""
      for wagon in train.split(): 
               if wagon.isdigit(): # Wagon bleu directement dans le nouveau train 
                       nouv_train = nouv_train + wagon + " " 
               else: # Wagon rouge en attente 
                         empile(wagon)
# Tous les wagon bleus sont maintenant rangés
# On s'occupe des wagons rouges en attente 
      while not pile_est_vide(): 
            wagon = depile() 
            nouv_train = nouv_train + wagon + " "
      return nouv_train
# Tests print("--- Tri rouge/bleu ---")
train = "A 4 C 12" 
train_trie = tri_wagons(train) 
print(train,' -> ',train_trie)
train = "9 K 8 P 17 L B R 3 10 2 N" 
train_trie = tri_wagons(train) 
print(train,' -> ',train_trie)

############################## # Piles - Calculatrice polonaise ##############################
############################## # Rappels - Activité 1 ##############################
def empile(element): 
    global pile 
    pile = pile + [element] 
    return None
def depile(): 
    global pile 
    sommet = pile[len(pile)-1] 
    pile = pile[0:len(pile)-1] 
    return sommet
def pile_est_vide(): 
    if len(pile) == 0: 
        return True 
    else:
        return False
############################## # Activité 4 - Calculatrice polonaise ##############################
## Question 1 ##
def operation(a,b,op): 
    # Calcule l'opération 'a + b 'ou 'a * b'... Entrée : a,b (nombres) et 'op' un caractère 
    #'+'' ou '*' Sortie : le résultat du calcul """
        if op == '+': 
            return a + b 
        if op == '*': 
            return a * b
# Tests print("--- Opérations ---") a=5 ; b=7 print("La somme de",a,"et",b,"vaut",operation(a,b,'+')) print("Le produit de",a,"et",b,"vaut",operation(a,b,'*'))
## Question 2 ##
def calculatrice_polonaise(expression): 
    # """ Calcule l'expression codée en notation polonaise Entrée : 
    # une expression en notation polonaise Sortie : le résultat du calcul Action : utilise la pile """
    #     global pile 
        pile = []
        liste_expression = expression.split()
        for car in liste_expression: 
            if (car == '+') or (car == '*'): 
                  b = depile() 
                  a = depile() 
                  calcul_partiel = operation(a,b,car) 
                  empile(calcul_partiel) 
            else: 
                  val = int(car) 
                  empile(val)
        return depile()
# Tests print("--- Calculatrice polonaise ---")
exp = "2 3 +" 
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))
exp = "2 3 + 5 *" 
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))
exp = "8 7 3 + *" 
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))
exp = "8 7 3 * +" 
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))

############################## # Piles - Calculatrice polonaise ##############################
############################## # Rappels - Activité 1 ##############################
def empile(element): 
    global pile 
    pile = pile + [element] 
    return None
def depile(): 
    global pile 
    sommet = pile[len(pile)-1] 
    pile = pile[0:len(pile)-1] 
    return sommet
def pile_est_vide(): 
    if len(pile) == 0: 
        return True 
    else: return False
############################## # Activité 5 - Expression bien parenthésée ##############################
## Question 1 ##
def parentheses_correctes(expression): 
     #""" Teste si une expression est bien parenthésée Entrée 
      #: un expression (chaîne de caractère) Sortie : vrai/faux Action : utilise une pile """
            global pile 
            pile = [] # On part d'une pile vide
            for car in expression: 
                if car == "(": 
                    empile(car)
                if car == ")": 
                        if pile_est_vide(): 
                            return False # Problème : il manque une "(" 
                        else: 
                            depile()
        # A la fin : 
                        if pile_est_vide(): 
                            return True 
                        else: 
                            return False
# Test print("--- Expression correctemment parenthésée ---")

expression = "(a+b)^2 = a^2 + (b^2+2(ab))" 
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))
expression = "((a+b)^3 = (a+b)" 
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))
expression = "(a+b)^4) = ((a+b)" 
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))
## Question 2 ##
def crochets_parentheses_correctes(expression):
    #""" Teste si une expression a des crochets et des parenthèses bien placées Entrée : un 
    #expression (chaîne de caractère) Sortie : vrai/faux Action : utilise une pile """
        global pile 
        pile = [] # On part d'une pile vide
        for car in expression: 
            if car == "(" or car == "[": 
                    empile(car)
            if car == ")" or car == "]": 
                    if pile_est_vide(): 
                        return False # Problème : il manque "(" ou "[" 
                    else: 
                         element = depile() 
                    if element == "[" and car == ")": 
                                 return False # Problème du type [) 
                    if element == "(" and car == "]": 
                                      return False # Problème du type (]# A la fin 
        return pile_est_vide()
# Test print("--- Expression avec crochets et parenthèses corrects ---")

expression = "(a+b)^2 = (a^2 + [b^2+[2(ab)]])" 
print("L'expression",expression,"est bien parenthésées et crochetées ?",'→',crochets_parentheses_correctes(expression)) 
expression = "((a+b)]^3 = [a+b]" 
print("L'expression",expression,"est bien parenthésées et crochetées ?",'→',crochets_parentheses_correctes(expression)) 
expression = "[a+b)^4] = (a+b)" 
print("L'expression",expression,"est bien parenthésées et crochetées ?",'→', crochets_parentheses_correctes(expression))

############################## # Piles - Calculatrice polonaise ##############################
#global pile

############################## # Rappels - Activité 1 ##############################
def empile(element): 
    global pile 
    pile = pile + [element] 
    return None
def depile(): 
    global pile 
    sommet = pile[len(pile)-1] 
    pile = pile[0:len(pile)-1] 
    return sommet
def pile_est_vide(): 
    if len(pile) == 0: 
        return True 
    else: return False
############################## # Rappels - Activité 4 ##############################
def operation(a,b,op): 
    if op == '+': 
        return a + b 
    if op == '*': 
        return a * b
def calculatrice_polonaise(expression): 
                global pile 
                pile = []
                liste_expression = expression.split()
                for car in liste_expression: 
                    if (car == '+') or (car == '*'): 
                        b = depile() 
                        a = depile() 
                        calcul_partiel = operation(a,b,car) 
                        empile(calcul_partiel) 
                    else: 
                         val = int(car) 
                         empile(val)
                return depile()
############################## # Activité 6 - Conversion vers l'écriture polonaise ##############################
def ecriture_polonaise(expression): 
#""" Convertit une expression classique en notation polonaise
#Entrée : une expression classique Sortie : 
#l'expression en notation polonaise Action : utilise une pile """
            global pile 
            pile = []
            liste_expression = expression.split()
            polonaise = "" # L'écriture polonaise
            for car in liste_expression: 
                if car.isdigit(): 
                    polonaise = polonaise + car + " "
                if car == "(": 
                    empile(car)
                if car == "*": 
                    empile(car)
                if car == "+": 
                    while not pile_est_vide(): 
                        element = depile() 
                        if element == "*": 
                            polonaise = polonaise + element + " " 
                        else: 
                            empile(element) # Remettre l'élément 
                            break 
                empile(car)
                if car == ")": 
                    while not pile_est_vide(): 
                        element = depile() 
                        if element == "(": 
                            break 
                        else: 
                            polonaise = polonaise + element + " "
                while not pile_est_vide(): 
                        element = depile() 
                        polonaise = polonaise + element + " "
                return polonaise
            # Tests print("--- Conversion en écriture polonaise ---")
exp = "2 + 3" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "2 * 3" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "( 2 + 3 ) * 4" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "4 * ( 2 + 3 )" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "2 + 4 * 5" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "2 * 4 * 5" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
exp = "( 2 + 3 ) * ( 4 + 8 )" 
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))
## # Automatisation des tests et des vérifications
def test_polonaise(expression): 
    classique = eval(expression) 
    print("---\n",classique) 
    conversion = ecriture_polonaise(expression)
    print(conversion) 
    polonaise = calculatrice_polonaise(conversion) 
    print(polonaise) 
    return classique == polonaise
exp = "2 + 3" 
print(exp, "OK ?",test_polonaise(exp))
exp = "2 * 3 * 7" 
print(exp, "OK ?",test_polonaise(exp))
exp = "( 2 + 3 ) * ( 4 + 8 )" 
print(exp, "OK ?",test_polonaise(exp))
exp = "( ( 2 + 3 ) * 11 ) * ( 4 + ( 8 + 5 ) )" 
print(exp, "OK ?",test_polonaise(exp))
exp = "( 17 * ( 2 + 3 ) ) + ( 4 + ( 8 * 5 ) )" 
print(exp, "OK ?",test_polonaise(exp))