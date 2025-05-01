from validate_docbr import CPF
import create_cpf
import validate_cpf

def main():
    while True:
        create_or_validate_cpf = input('Do you want to create or validate the cpf?\n'
                                       '(Enter "1" to "create" and "2" to "Validate"): ')

        match create_or_validate_cpf:
            case '1':
                ...
                break
            case '2':
                cpf()
            case _:
                print('Invalid Option, Try Again!!')

def cpf():
    cpf = CPF()
    while True:
        formatted_cpf = input('Enter the cpf: ')
        cpf_length = 9

        if not formatted_cpf.isdigit():
            print('Enter a valid value!')
            continue

        if len(formatted_cpf) == cpf_length:
            return cpf.mask(formatted_cpf)
        else:
            print('The cpf must have 9 numbers, try again!')
            continue

main()