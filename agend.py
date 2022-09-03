from colors import Cores
c = Cores()

class Agenda():
    
    def __init__(self,Nome,Idade,Altura):
        self._Nome    = Nome
        self._Idade   = Idade
        self._Altura  = Altura
        self._Agenda0 = {}
        self._Agenda1 = {}
        
    def menu(self):  
        print(f'''\n\t[1] - {c.bcyan}Armazenar Pessoa na agenda{c.C}\n\t[2] - {c.bcyan}Remover pessoa da agenda{c.C}
        [3] - {c.bcyan}Buscar pessoa na agenda{c.C}\n\t[4] - {c.bcyan}Imprimir agenda{c.C}''')
        
        
        
    def armazenaPessoa(self): #// Não permitir armazenar mais de 10 pessoas
        print(f'\t{c.byellow}Quantidade de pessoas na agenda:{c.C}',len(self._Agenda1.keys()))
        if len(self._Agenda1.keys()) < 10:
            self._Nome    = input(f'\n\t{c.code_result}{c.blue}Digite o nome:{c.C}')
            self._Idade   = int(input(f'\t{c.code_result}{c.blue}Digite a idade:{c.C}'))
            self._Altura  = float(input(f'\t{c.code_result}{c.blue}Digite a altura:{c.C}'))
            
            self._Agenda0 = {self._Nome:[self._Idade,self._Altura]}
            self._Agenda1.update(self._Agenda0)
            print(f'\n\t{c.bgreen}Pessoa cadastrada com sucesso!{c.C}')
        else:
            print(f'\n\t{c.bred}Agenda cheia{c.C}') 
            
            
            
            
    def RemoverPessoa(self): #// Pelo nome
        pessoa = input('\n\tDigite o nome da pessoa que deseja remover:')
        if len(self._Agenda1.keys()) > 0 and pessoa in self._Agenda1:
            self._Agenda1.pop(pessoa)
            print(f'\n\t{c.bgreen}Pessoa removida com sucesso!{c.C}')
        else:
            print(f'\n\t{c.bred}Agenda vazia ou pessoa não está na agenda{c.C}')
            
            
            
            
            
    def BuscarPessoa(self):  #// Busca pelo nome e imprime os dados da pessoa
        busca = input(f'\n\t{c.code_result} Digite o nome da pessoa que deseja buscar:')
        if busca in self._Agenda1:
            print(f'\n\t{c.bblue}---------------------------------{c.C}')
            print(f'\n\tDados do {busca}')
            print(f'\tIdade: {self._Agenda1[self._Nome][0]}')
            print(f'\tAltura: {self._Agenda1[self._Nome][1]}')
            
            print(f'\n\t{c.bblue}---------------------------------{c.C}')
        else:
            print(f'\n\t{c.bred}Pessoa não está na agenda{c.C}')     
       
    
    
    
    
    
    def imprimirAgenda(self):  #// imprime os dados de todas as pessoas da agenda
        if self._Agenda1 == {}:
            print(f'\n\t{c.bred}Agenda vazia')
        for chave ,valor in self._Agenda1.items():
            print('\n\t----------------AGENDA---------------')
            print(f'\n\tNome: {chave}')
            print(f'\tIdade: {valor[0]}')
            print(f'\tAltura: {valor[1]}\n')
            print('\n\t--------------------------------------')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    