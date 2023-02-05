
from functools import reduce, cache, lru_cache
import os
import copy


def IzaberiPrviPotez() -> bool:
    tip:str = ""
    while tip != "x" and tip != "o":
        os.system('cls||clear')
        tip = input("Izaberite da li cete igrati prvi ili drugi\n( x -> prvi |  o -> drugi) \nUnos: " )
        if tip != "x" and tip != "o":
             input("Invalidan izbor !!\n(Pritisnite Enter da pokusate opet)\n")

    if(tip == "x"):
        return True
    else:
        return False

def InicijalizujMatricu() -> list:
    DimenzijeMatrice = VratiVelicinuPolja()
    n = DimenzijeMatrice[0]
    m = DimenzijeMatrice[1]
    return [[" " for x in range(0,n)] for y in range(0,m)]

def VratiVelicinuPolja() -> list:
    n:int = 0
    m:int = 0
    while n < 3 and m < 3:
        os.system('cls||clear')
        m = try_parse_int(input("Unesite velicinu polja (Maksimum je 8x8):\nn:" ))
        n = try_parse_int(input("\nm: " ))
        
        if((n == -1 or m == -1) or (n > 8 or m > 8)):
            input("Invalidan unos dimenzija\n(Pritisnite Enter da pokusate opet)\n")
            n = m = 0
            
            
    return [n,m]

def try_parse_int(text):
    try:
        return int(text)
    except:
        return -1

def Display(Polje:list,stanje:int,potez:bool):
    n:int = len(Polje)
    m:int = reduce(lambda acc,val: acc+1 ,Polje[n-1] ,0)
    ln:str = "Trenutno na potezu:"
    #os.system('cls||clear')

    if(potez):
     ln+=" X"
    else:
     ln+=" O"
    print(ln)

    ln = PomocnaCrtanja(m,False)
    ln += PomocnaCrtanja(m,True)
    for i in range(0,n):    
        ln += "\n  "+str(i)+"\t||" 
        for j in range(0,m):
            ln +=" "+str( Polje[i][j] )+" |"
        ln +="|\t"+str(i)
        ln += PomocnaCrtanja(m,True)
    ln += PomocnaCrtanja(m,False)

    print(ln)

    
    if stanje != 0:
     ln = "\n\nPobedio je igrac"
     if stanje == 1:
        ln += ": X"
     else:
        ln += ": O"
     input(ln+"\n\nPritisni Enter za izlaz .....")
     return

def PomocnaCrtanja(n:int,SymOrNum:bool) -> str:
    ln:str = ""
    ln += "\n\t"
    if SymOrNum:
        ln += "--"
        for i in range(0,n):
            ln += "----"
        ln += "-"
    else:
        ln += " "
        for i in range(0,n):
           ln += "  "+str(i)+" "
        ln += ""
    
    return ln

def kraj(polje:list):
    Xp = len(ListaMogucihPoteza(polje,True))
    Op = len(ListaMogucihPoteza(polje,False))
    if Xp== 0:
        return -10
    elif Op == 0:
        return 10
    else:
        return 0

def ValidnostPoteza(Polje:list,na_potezu:bool,i:int,j:int )->bool: 
    if i < 0 or j < 0 :
        return False

    n:int = len(Polje)
    m:int = reduce(lambda acc,val: acc+1 ,Polje[n-1] ,0)

    if(i>=n or j>=m): 
        return False

    if na_potezu==False:
        if j <= m-2 and  Polje[i][j] == ' ' and Polje[i][j+1] == ' ':
            return True
        else:
            return False
    elif na_potezu==True: 
        if i <= n-2 and Polje[i][j] == ' ' and Polje[i+1][j] == ' ':
            return True
        else:
            return False

def Odigraj(Polje:list,na_potezu:bool,i:int,j:int) -> list:
    local_polje = copy.deepcopy(Polje)    
    if na_potezu:
        local_polje[i][j] = local_polje[i+1][j] = "X"   
    else:
        local_polje[i][j] = local_polje[i][j+1] = "O"
    
    return local_polje

def StampajMogucePoteze(na_potezu:bool,listaVertikalno:list,listaHorizontalno:list, Polje:list):
    listaPoteza = ListaMogucihPoteza(Polje,na_potezu)
    if na_potezu:
         print(listaPoteza)
    else:
        print(listaPoteza)

def VratiMogucaStanja(na_potezu:bool,listaVertikalno:list,listaHorizontalno:list,polje:list) -> list:
    listaPoteza = ListaMogucihPoteza(polje,na_potezu)
    Svi_Potezi = []   
    i:int 
    j:int 
    if na_potezu:
        for potez in listaPoteza:
            mylist = copy.deepcopy(polje)
            (i,j) = potez
            mylist[i][j] = mylist[i+1][j] = "X"   
            Svi_Potezi.append(mylist)
    else:
        for potez in listaPoteza:
            mylist = copy.deepcopy(polje)
            (i,j) = potez
            mylist[i][j] = mylist[i][j+1] = "O"
            Svi_Potezi.append(mylist)

    return Svi_Potezi 

def ListaSafePoteza(lista_poteza:list,polje:list ,na_potezu:bool) -> list:
    
    n = len(polje)
    m:int = reduce(lambda acc,val: acc+1 ,polje[len(polje)-1] ,0)
    RetList:list = []
    for potez in lista_poteza:
        (x,y) = potez
        if na_potezu:
            if  y > 0 and x < n and y < m-1:
                if  (polje[x][y-1] == " "  and polje[x+1][y-1] == " ") or (polje[x][y+1] == " "  and polje[x+1][y+1] == " "):
                    if (y - 2 < 0 or y + 2 >= m) or (polje[x][y-2] != " "  and polje[x+1][y-2] != " ") or (polje[x][y+2] != " "  and polje[x+1][y+2] != " ") :
                        RetList.append([x,y])   
        else:
            if  x > 0 and x < n-1 and y < m-1:
                if  (polje[x-1][y] == " "  and polje[x-1][y+1] == " ") or (polje[x+1][y] == " "  and polje[x+1][y+1] == " "):
                    if (y - 2 < 0 or y + 2 >= m) or (polje[x][y-2] != " "  and polje[x+1][y-2] != " ") or (polje[x][y+2] != " "  and polje[x+1][y+2] != " ") :                    
                        RetList.append([x,y])  
    return RetList

def ListaMogucihPoteza(polje:list,na_potezu:bool):
    n = len(polje)
    m:int = reduce(lambda acc,val: acc+1 ,polje[len(polje)-1] ,0)
    RetList:list = [(i,j) for i in range(0,n) for j in range(0,m) if ValidnostPoteza(polje,na_potezu,i,j)]
    return RetList

def Heuristic(polje:list):
    Xp = ListaMogucihPoteza(polje,True)
    Op = ListaMogucihPoteza(polje,False)
    Xs = len(ListaSafePoteza(Xp,polje,True))
    Os = len(ListaSafePoteza(Op,polje,False))

    Xp = len(Xp)
    Op = len(Op)
    return (+ Xp - Op + Xs - Os) / 1.5

def full(polje:list):
    counter = 0
    n = len(polje)
    m:int = reduce(lambda acc,val: acc+1 ,polje[len(polje)-1] ,0)
    for i in range(0,n):
        for j in range(0,m):
            if polje[i][j] == " ":
                counter = counter + 1
    if counter == 0:
        return True
    else:
        return False

def FreeSpace(polje:list) -> int:
    counter = 0
    n = len(polje)
    m:int = reduce(lambda acc,val: acc+1 ,polje[len(polje)-1] ,0)
    for i in range(0,n):
        for j in range(0,m):
            if polje[i][j] == " ":
                counter = counter + 1
    return counter

def max_value(stanje,dubina,alpha,beta,potez:list = None):
    if abs(kraj(stanje) == -10 or full(stanje)):
        return(potez,kraj(stanje))
    lista_poteza = ListaMogucihPoteza(stanje,True)
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez,Heuristic(stanje))
    else:
        for LP in lista_poteza:
            (x,y) = LP
            alpha = max(alpha,min_value(Odigraj(stanje,True,x,y),dubina-1,alpha,beta,LP if potez is None else potez),key=lambda x:x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha

def min_value(stanje,dubina,alpha,beta,potez:list = None):
    if abs(kraj(stanje) == 10 or full(stanje)):
        return(potez,kraj(stanje))
    lista_poteza = ListaMogucihPoteza(stanje,False)
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez,Heuristic(stanje))
    else:
        for LP in lista_poteza:
            (x,y) = LP
            beta = min(beta,max_value(Odigraj(stanje,False,x,y),dubina-1,alpha,beta,LP if potez is None else potez),key=lambda x:x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta

def minimax_alpha_beta(stanje, dubina, na_potezu, alpha=(None, -10), beta=(None, 10)):
    if na_potezu:
        return max_value(stanje, dubina, alpha, beta)
    else:
        return min_value(stanje, dubina, alpha, beta)
