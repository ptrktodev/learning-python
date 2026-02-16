dict = [{
    'pergunta': 'Qual é a capital da França?',
    'resposta': 'Paris',
    'opções': ['Londres', 'Berlim', 'Madrid', 'Paris']
    },
    {
    'pergunta': 'Qual é a capital da Itália?',
    'resposta': 'Roma',
    'opções': ['Veneza', 'Milão', 'Florença', 'Roma']
    }
]

print(dict[0]['pergunta'])

print(f"A) {dict[0]['opções'][0]}")
print(f"B) {dict[0]['opções'][1]}")
print(f"C) {dict[0]['opções'][2]}")
print(f"D) {dict[0]['opções'][3]}")

while True:
    resposta_usuario = input("Digite a letra da sua resposta: ").strip().upper()

    # strip = remove espaços em branco
    # upper = transforma em maiúsculo

    if resposta_usuario == 'D':
        print("Resposta correta!")

        while True:
            print()
            print(dict[1]['pergunta'])
            print()
            print(f"A) {dict[1]['opções'][0]}")
            print(f"B) {dict[1]['opções'][1]}")
            print(f"C) {dict[1]['opções'][2]}")
            print(f"D) {dict[1]['opções'][3]}")
            
            resposta_usuario = input("Digite a letra da sua resposta: ").strip().upper()

            if resposta_usuario == 'D':
                print("Resposta correta!")
                break
            else:
                print("Resposta incorreta.")
        break
    else:
        print("Resposta incorreta.")