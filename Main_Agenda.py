from agend import Agenda
from colors import Cores
import os
c = Cores()

def clear():
    if os == "Windows":
       os.system("cls")
    elif os == "Linux":
       os.system("clear")
    else:
        os.system("clear")




A = Agenda(Nome ='',Idade = 0,Altura = 0.0)

logo = f'''\t{c.bcyan}╭━━━╮╭━━━╮╭━━━╮╭━╮╱╭╮╭━━━╮╭━━━╮
\t{c.bred}┃╭━╮┃┃╭━╮┃┃╭━━╯┃┃╰╮┃┃╰╮╭╮┃┃╭━╮┃
\t{c.byellow}┃┃╱┃┃┃┃╱╰╯┃╰━━╮┃╭╮╰╯┃╱┃┃┃┃┃┃╱┃┃
\t{c.bblue}┃╰━╯┃┃┃╭━╮┃╭━━╯┃┃╰╮┃┃╱┃┃┃┃┃╰━╯┃
\t{c.bpurple}┃╭━╮┃┃╰┻━┃┃╰━━╮┃┃╱┃┃┃╭╯╰╯┃┃╭━╮┃
\t{c.bgreen}╰╯╱╰╯╰━━━╯╰━━━╯╰╯╱╰━╯╰━━━╯╰╯╱╰╯
\t{c.bcyan}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
\t{c.bblue}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
                            {c.bgreen}Iago-Linux{c.C}'''
print(logo)
while True:
    print(f'\n\t{c.code_details} {c.blue}Digite {c.byellow}[exit]{c.C} {c.blue}para sair{c.C}')
    print(f'\t{c.code_details} {c.blue}Digite {c.byellow}[clear]{c.C} {c.blue}para limpar a tela{c.C}\n\n')
    A.menu()
    op = input(f'\n\t{c.code_result}{c.bpurple}O que deseja fazer:{c.C}')
    
    
    if op == '1':
        A.armazenaPessoa()
    elif op == '2':
        A.RemoverPessoa()
    elif op == '3':
        A.BuscarPessoa()
    elif op == '4':
        A.imprimirAgenda()
    elif op == 'clear':
        clear()
    elif op == 'exit':
        print(f'\n\t{c.bred}Saindo...')
        exit()
        