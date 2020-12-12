import secrets
import string
import uuid

def passwd_words(tamanho):
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters) for i in range(tamanho))
    return password

def passwd_words_numbers(tamanho):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(password_characters) for i in range(tamanho))
    return password

def passwd_words_numbers_simbols(tamanho):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for i in range(tamanho))
    return password

def passwd_hex(tamanho):
    password = secrets.token_hex(tamanho)
    return password

def passwd_uuid():
    password = uuid.uuid4
    return password


if __name__ == "__main__":
    pass
  
    print('Programa gerador de senhas')
    print('Escolha o tipo de senha:')
    print('1 - Somente letras')
    print('2 - Letras e numeros')
    print('3 - Letras, numeros e caracteres especiais')
    print('4 - Hexadecimal')
    print('5 - UUID')
    escolha = int(input('Entre com a senha opcao desejada: '))
    if escolha == 1:
        tamanho = int(input('Digite o tamanho da senha desejada: '))
        print(passwd_words(tamanho))
    elif escolha == 2:
        tamanho = int(input('Digite o tamanho da senha desejada: '))
        print(passwd_words_numbers(tamanho))
    elif escolha == 3:
        tamanho = int(input('Digite o tamanho da senha desejada: '))
        print(passwd_words_numbers_simbols(tamanho))
    elif escolha == 4:
        tamanho = int(input('Digite o tamanho da senha desejada: '))
        print(passwd_hex(tamanho))
    elif escolha == 5:
        print(passwd_uuid())
    else:
        print('Opcao invalida!')
