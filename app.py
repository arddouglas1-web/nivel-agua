from colorama import Fore, Style

mensagens = [   "Nível 1: Muito baixo (crítico)",  "Nível 2: Baixo", "Nível 3: Médio", "Nível 4: Alto",
                "Nível 5: Muito alto (alerta)" ]

def exibir(nivel):
    if nivel == 1:
        print(Fore.RED + mensagens[0])
    elif nivel == 2:
        print(Fore.YELLOW + mensagens[1])
    elif nivel == 3:
        print(Fore.GREEN + mensagens[2])
    elif nivel == 4:
        print(Fore.CYAN + mensagens[3])
    elif nivel == 5:
        print(Fore.BLUE + mensagens[4])

     

print("Lista de níveis para a Água e sua situação: ")
print(exibir(1))   
print(exibir(2)) 
print(exibir(3))   
print(exibir(4))   
print(exibir(5))     

print(Style.RESET_ALL)   