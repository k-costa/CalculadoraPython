import os

def solicitando_numeros():
    print('\n')
    num1 = float(input('Digite o 1° número: '))
    num2 = float(input('Digite o 2° número: '))
    return num1, num2

def somar(num1, num2):
    return num1 + num2    

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2!= 0:
        return num1 / num2
    else:
        return "Erro! Divisão por zero."
    
def encerrar_calculadora():
    os.system('cls')
    print('Encerrando calculadora')

def opcao_invalida():
    os.system('cls')
    print('\nOpção inválida!')
    input('\nPressione a tecla "enter" para voltar ao menu principal ')
    main()

def menu():
    print('ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕕𝕠𝕣𝕒 ℙ𝕪𝕥𝕙𝕠𝕟')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Encerrar')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida in [1, 2, 3, 4]:
            num1, num2 = solicitando_numeros()

            if opcao_escolhida == 1:
                resultado = somar(num1, num2)               

            elif opcao_escolhida == 2:
                resultado = subtrair(num1, num2) 

            elif opcao_escolhida == 3:
                resultado = multiplicar(num1, num2)

            elif opcao_escolhida == 4:
                resultado = dividir(num1, num2)
            
            elif opcao_escolhida == 5:
                encerrar_calculadora()
        
            print(f'\nResultado: {resultado}')
            continuar = input('\nDeseja continuar? (S/N): ').strip().lower()

            if continuar == 's':
                main()
            elif continuar == 'n':
                print('Encerrando programa')
            else:
                opcao_invalida()

        elif opcao_escolhida == 5:
            encerrar_calculadora()
        else:
            opcao_invalida()        
    except:
        opcao_invalida()


def main():
    #LIMPA TELAS
    os.system('cls')
    menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
