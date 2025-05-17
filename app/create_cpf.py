from validate_docbr import CPF  # Importa a classe CPF da biblioteca externa 'validate-docbr' para validação de CPF
import random  # Importa o módulo para gerar números aleatórios

# Criação dos 11 dígitos do cpf e retorna ele formatado
class Create:
    def __init__(self):
        self.cpf = ''
        self.first_digit = ''
        self.second_digit = ''

    # Gera os 9 primeiros dígitos do CPF de forma aleatória
    def create_cpf(self):
        for i in range(0, 9):
            cpf_int = random.randint(0, 9)
            cpf_str = str(cpf_int)
            self.cpf += cpf_str
        return self.cpf

    # Calcula o primeiro dígito verificador com base nos 9 primeiros dígitos
    def first_digit_cpf(self):
        sum_numbers = 0
        multiple_cpf = 10

        for i in self.cpf:
            sum_numbers += multiple_cpf * int(i)
            multiple_cpf -= 1
        
        digit = (sum_numbers * 10) % 11
        self.first_digit = digit if digit <= 9 else 0
        return self.first_digit

    # Calcula o segundo dígito verificador com base nos 9 dígitos + primeiro dígito
    def second_digit_cpf(self):
        cpf_11_digits = str(self.cpf) + str(self.first_digit)
        sum_numbers = 0
        multiple_cpf = 11

        for i in cpf_11_digits:
            sum_numbers += multiple_cpf * int(i)
            multiple_cpf -= 1
        
        digit = (sum_numbers * 10) % 11
        self.second_digit = digit if digit <= 9 else 0
        return self.second_digit

    # Junta os 9 dígitos com os dois dígitos verificadores para formar o CPF completo
    def full_cpf(self):
        self.create_cpf()
        self.first_digit_cpf()
        self.second_digit_cpf()
        return f'{self.cpf}{self.first_digit}{self.second_digit}'

    # Formata o CPF usando a biblioteca externa
    def formatted_cpf(self):
        format_cpf = CPF()
        full_cpf = self.full_cpf()
        return f'This is your new CPF: {format_cpf.mask(full_cpf)}'
