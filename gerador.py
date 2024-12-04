import random
import string

def gerar_senha(tamanho=12, letras=True, numeros=True, especiais=True):
    caracteres = ''
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione ao menos um tipo de caractere!")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas!")
    tamanho = int(input("Digite o comprimento da senha: "))
    incluir_letras = input("Incluir letras? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    try:
        senha = gerar_senha(tamanho, incluir_letras, incluir_numeros, incluir_especiais)
        print(f"Sua senha gerada é: {senha}")
    except ValueError as e:
        print(f"Erro: {e}")
python gerador.py
