from colors import Cores
c = Cores()
class Elevador():
    
    def __init__(self, terreo, andares, quantidade):
        self._terreo     = terreo
        self._andares    = andares
        self._quantidade = quantidade
        
        
    def Entrar(self):
        if self._quantidade < 10:
            self._quantidade+=1
            print(f'\n\t{c.bgreen}{self._quantidade} pessoa(s) no elevador{c.C}')
        else:
            print('\n\tElevador cheio')
            

    def Sair(self):
        if self._quantidade > 0:
            self._quantidade-=1
            print(f'\n\t{self._quantidade} pessoa(s) no elevador')
        else:
            print('\n\tElevador vazio')
            
            
    def Subir_Descer(self):
        if self._andares <= 4:
            print(f'\n\tElevador indo para o andar {self.andar}')
        

    
    def andaresop(self):
        if self._andares == 0:
            print('\n\tVoçê está no terreo')
            print('\n\t[1 -andar]')
            print('\t[2 -andar]')
            print('\t[3 -andar]')
            print('\t[4 -andar]')
        elif self._andares == 1:
            print('\n\tVoçê está no 1° andar')
            print('\n\t[0 -andar]')
            print('\t[2 -andar]')
            print('\t[3 -andar]')
            print('\t[4 -andar]')
            
        elif self._andares == 2:
            print('\n\tVoçê está no 2° andar')
            print('\n\t[0 -andar]')
            print('\t[1 -andar]')
            print('\t[3 -andar]')
            print('\t[4 -andar]')
            
        elif self._andares == 3:
            print('\n\tVoçê está no 3° andar')
            print('\n\t[0 -andar]')
            print('\t[1 -andar]')
            print('\t[2 -andar]')
            print('\t[4 -andar]')
            
        elif self._andares == 4:
            print('\n\tVoçê está no 4° andar')
            print('\n\t[0 -andar]')
            print('\t[1 -andar]')
            print('\t[2 -andar]')
            print('\t[3 -andar]')
            
            
    #GET E SET
    @property
    def terreo(self):
        return self._terreo
    
    @terreo.setter
    def terreoSET(self,terreo):
        self._terreo = terreo
    
    
    @property
    def andar(self):
        return self._andares
    
    @andar.setter
    def andarSET(self,andares):
        self._andares = andares
        
        
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidadeSET(self,quantidade):
        self._quantidade = quantidade
        
        
