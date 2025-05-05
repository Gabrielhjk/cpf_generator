from validate_docbr import CPF
import random

def create_cpf():
    cpf = ''
    for i in range(0, 9):
        cpf_int = random.randint(0, 9)
        cpf_str = str(cpf_int)
        cpf += cpf_str
    return cpf

def first_digit_cpf(cpf):
    multiplication_sum = 0
    multiple_cpf = 10

    for i in cpf:
        multiplication_sum += multiple_cpf * int(i)
        multiple_cpf -= 1
    
    multiplication_sum *= 10
    multiplication_sum %= 11
    first_digit_cpf = multiplication_sum if multiplication_sum <= 9 else 0
    return first_digit_cpf

def second_digit_cpf(cpf, first_digit):
    cpf_11_digits = cpf + str(first_digit)
    multiplication_sum = 0
    multiple_cpf = 11

    for i in cpf_11_digits:
        multiplication_sum += multiple_cpf * int(i)
        multiple_cpf -= 1
    
    multiplication_sum *= 10
    multiplication_sum %= 11
    second_digit_cpf = multiplication_sum if multiplication_sum <= 9 else 0
    return cpf_11_digits + str(second_digit_cpf)

def formatted_cpf(second_digit):
    formatted_cpf = CPF()
    return formatted_cpf.mask(second_digit)

cpf = create_cpf()
first_digit = first_digit_cpf(cpf)
second_digit = second_digit_cpf(cpf, first_digit)
formatted = formatted_cpf(second_digit)