from classe import Elevador
from colors import Cores
import os
c = Cores()

LOGO = f'''{c.bcyan}╭━━━╮╭╮╱╱╱╭━━━╮╭╮╱╱╭╮╭━━━╮╭━━━╮╭━━━╮╭━━━╮
{c.bgreen}┃╭━━╯┃┃╱╱╱┃╭━━╯┃╰╮╭╯┃┃╭━╮┃╰╮╭╮┃┃╭━╮┃┃╭━╮┃
{c.bpurple}┃╰━━╮┃┃╱╱╱┃╰━━╮╰╮┃┃╭╯┃┃╱┃┃╱┃┃┃┃┃┃╱┃┃┃╰━╯┃
{c.byellow}┃╭━━╯┃┃╱╭╮┃╭━━╯╱┃╰╯┃╱┃╰━╯┃╱┃┃┃┃┃┃╱┃┃┃╭╮╭╯
{c.bred}┃╰━━╮┃╰━╯┃┃╰━━╮╱╰╮╭╯╱┃╭━╮┃╭╯╰╯┃┃╰━╯┃┃┃┃╰╮
{c.bblue}╰━━━╯╰━━━╯╰━━━╯╱╱╰╯╱╱╰╯╱╰╯╰━━━╯╰━━━╯╰╯╰━╯
{c.bgreen}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
{c.bcyan}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
                        {c.bgreen}Iago_linux'''

print(LOGO)

Elev = Elevador(terreo=0,andares=0,quantidade=0)

while True:
    #print(f'\n\t{bcyan}Limpe a tela com o comando {bgreen}clear{C}\n\t{bcyan}Digite{C} {bgreen}exit {bcyan}para sair{C}')
    print(f'\n\t{c.bpurple}[1]{c.C} - {c.bcyan}Entrar no elevador')
    print(f'\t{c.bpurple}[2]{c.C} - {c.bcyan}Sair do elevador')
    print(f'\t{c.bpurple}[3]{c.C} - {c.bcyan}Subir/Descer')
    print(f'\t{c.bpurple}[4]{c.C} - {c.bcyan}Consultar andar e quantidade de pessoas no elevador{c.C}')
    op = input(f'\t{c.code_result}{c.bred}O que deseja fazer:{c.C}')
    if op == '1':
        Elev.Entrar()
        
    elif op == '2':
        Elev.Sair()
        
    elif op == '3':
        Elev.andaresop()
        
        Elev.andarSET = int(input('\tAndar:')) 
        if Elev.andarSET > 4:
            Elev.andarSET = 4
            print('\n\tO predio possui só 4 andares')
        else:  
            Elev.Subir_Descer()
        
    elif op == '4':
        print('\tAndar:',Elev.andar)
        print(f'\tQuantidade: {Elev.quantidade}')
    elif op == 'clear':
        os.system('clear')
    elif op == 'EXIT'.lower():
        exit()