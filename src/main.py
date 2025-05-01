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

        if not formatted_cpf.isdigit():
            print('Enter a valid value!')
            continue

        if len(formatted_cpf) > 9:
            print('The cpf have more than 9 numbers, try again!')
            continue
        elif len(formatted_cpf) < 9:
            print('The cpf have less than 9 numbers, try again!')
            continue
        
        return cpf.mask(formatted_cpf)

main()