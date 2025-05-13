from validate_docbr import CPF

# Recebe a entrada do usuário e só permite números com 11 dígitos
class Cpf:
    def __init__(self, cpf=''):
        self.cpf = cpf    

    def enter_cpf(self):
        while True:
            self.cpf = input('Enter the cpf (only numbers): ')

            if not self.cpf.isdigit():
                print('Enter a valid value!')
                continue

            if len(self.cpf) == 11:
                return self.cpf
            else:
                print('The cpf must have 11 numbers, try again!')
                continue

# Valida se o cpf é valido ou inválido e retorna o cpf formatado
class Validation(Cpf):
    def __init__(self, cpf=''):
        super().__init__(cpf=cpf)
        self.first_digit = ''
        self.second_digit = ''

    def first_digit_cpf(self):
        sum_numbers = 0
        multiple_cpf = 10

        for i in self.cpf[:9]:
            sum_numbers += multiple_cpf * int(i)
            multiple_cpf -= 1
        
        digit = (sum_numbers * 10) % 11
        self.first_digit = digit if digit <= 9 else 0
        return self.first_digit

    def second_digit_cpf(self):
        cpf_11_digits = str(self.cpf[:9]) + str(self.first_digit)
        sum_numbers = 0
        multiple_cpf = 11

        for i in cpf_11_digits:
            sum_numbers += multiple_cpf * int(i)
            multiple_cpf -= 1
        
        digit = (sum_numbers * 10) % 11
        self.second_digit = digit if digit <= 9 else 0
        return self.second_digit
    
    def formatted_cpf(self):
        format_cpf = CPF()
        return format_cpf.mask(self.cpf)

    def validate_user_cpf(self):
        self.enter_cpf()
        self.first_digit_cpf()
        self.second_digit_cpf()
        format_cpf = self.formatted_cpf()
        if self.cpf[-2:] == f'{str(self.first_digit)}{str(self.second_digit)}':
            return f'The cpf {format_cpf} is valid!'
        else:
            return f'The cpf {format_cpf} is invalid!'

