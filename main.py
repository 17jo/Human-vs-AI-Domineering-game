import time
import func;
import os;

def StartGame():
    stanje_igre:int = 0
    Raspored:bool = func.IzaberiPrviPotez()  # true - X (prvi), false  - O (drugi)
    Player = Raspored
    AI = not Raspored
    na_potezu:bool = True # true - x , false - o
    Polje:list = func.InicijalizujMatricu()
    EndMessage:str = "Pobedio je igrac "
    depth:int = 0

    while stanje_igre == 0:
         stanje_igre:int = func.kraj(Polje)
         if(stanje_igre == - 10):
                EndMessage += "O"
                break

         elif stanje_igre == 10:
                EndMessage += "X"
                break

         os.system('cls||clear')
         func.Display(Polje,stanje_igre,na_potezu)

         if na_potezu == Player:
            i = func.try_parse_int(input("Unesite koordinatu 1:\n"))
            j = func.try_parse_int(input("Unesite koordinatu 2:\n"))

            while(func.ValidnostPoteza(Polje,na_potezu,i,j) == False):
                os.system('cls||clear')
                func.Display(Polje,stanje_igre,na_potezu)
                #func.StampajMogucePoteze(na_potezu, listaVertikalno,listaHorizontalno) da li ostaviti kao helper ??
                i = func.try_parse_int(input("Unesite koordinatu 1:\n"))
                j = func.try_parse_int(input("Unesite koordinatu 2:\n"))
             
            Polje = func.Odigraj(Polje,na_potezu,i,j)
            
         elif na_potezu == AI:
            if(depth == 0 and na_potezu == True):
                (i,j) = (0,1) 
                depth = 1         
            else:
                FreeSpace = func.FreeSpace(Polje) # dinamicka dodela dubine
                depth = 3
                if FreeSpace < 48:
                    depth = 4
                
                                  
                Result = func.minimax_alpha_beta(Polje,depth,na_potezu)[0]
                while(Result == None):
                   depth = depth-1
                   Result = func.minimax_alpha_beta(Polje,depth,na_potezu)[0]
                (i,j) = Result
            Polje = func.Odigraj(Polje,na_potezu,i,j)
                        
         na_potezu = not na_potezu          
         os.system('cls||clear')
         func.Display(Polje,stanje_igre,na_potezu)
    
    print("\n"+EndMessage)
   

StartGame()