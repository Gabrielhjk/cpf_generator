from validate_docbr import CPF
from create_cpf import formatted
from validate_cpf import *

def main():
    while True:
        create_or_validate_cpf = input('Do you want to create or validate the cpf?\n'
                                       '(Enter "1" to "create" and "2" to "Validate"): ')

        match create_or_validate_cpf:
            case '1':
                print(f'This is your new CPF: {formatted}')
                break
            case '2':
                user_cpf = input('Enter the cpf (only numbers): ')
                Cpf(user_cpf).enter_cpf()
                validator = Validation(user_cpf)
                print(validator.validate_user_cpf()) 
                break
            case _:
                print('Invalid Option, Try Again!!')


if __name__ == '__main__':
    main()
