#Fonte: https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/09-ExpressoesInfixaPrefixaPosfixa.html
#Data: 27/03/2021
#Aluno: Álef da Silva Fernandes

from pythonds.basic.stack import Stack
import PySimpleGUI as sg

#Função que retorna a notação pós-fixada
def infixadaparaposfixada(expressao):
    dicionary = {}                          #Criação de um dicionário com os pesos de cada caractere
    dicionary["*"] = 3
    dicionary["/"] = 3
    dicionary["+"] = 2
    dicionary["-"] = 2
    dicionary["("] = 1
    pilhao = Stack()                        #uso de uma pilha, estrutura python
    
    listaposfixada = []
    tokenizando = expressao.split()         #transforma a entrada em uma lista
    
    for token in tokenizando:              
        if token in "0123456789":           
            listaposfixada.append(token)    #Se o caracetere for um número adiciona na lista pos-fixada
            
        elif token == '(':
            pilhao.push(token)              #Se for '(' adiciona na pilha
            
        elif token == ')':                  
            topotoken = pilhao.pop()        #Se for ')' adiciona na variavel topotoken e remove da pilha
            
            while topotoken != '(':
                listaposfixada.append(topotoken)
                
                topotoken = pilhao.pop()
                
        else:
            while (not pilhao.isEmpty()) and (dicionary[pilhao.peek()] >= dicionary[token]):
                  listaposfixada.append(pilhao.pop())
                  
            pilhao.push(token)
            

    while not pilhao.isEmpty():
        listaposfixada.append(pilhao.pop())
    return " ".join(listaposfixada)


expressaoinput = sg.popup_get_text('Digite aqui uma expressão matemática:', 'Calculadora')

resultado = expressaoinput.replace(')','')
resultado = resultado.replace('(','')
resultado = eval(resultado)
sg.popup('Expressão pós-fixada', (infixadaparaposfixada(expressaoinput)), '\nResultado:',resultado)
