# Importa a classe CPF da biblioteca externa 'validate-docbr' para validação de CPF
from validate_docbr import CPF
from create_cpf import Create
from validate_cpf import Validation

# Função principal do programa
def main():
    while True:
        create_or_validate_cpf = input('Do you want to create or validate the cpf?\n'
                                       '(Enter "1" to "create" and "2" to "Validate"): ')

        # Estrutura match-case para tratar a escolha do usuário
        match create_or_validate_cpf:
            # se a opção for 1, cria um novo cpf
            case '1':
                create_cpf = Create().formatted_cpf()
                print(create_cpf)
                break
            # Se a opção for 2, valida o CPF inserido pelo usuário
            case '2':
                validate = Validation().validate_user_cpf()
                print(validate) 
                break
            case _:
                # Caso a entrada seja inválida, exibe aviso
                print('Invalid Option, Try Again!!')

if __name__ == '__main__':
    main()
