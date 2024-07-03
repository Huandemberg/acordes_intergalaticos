from collections import Counter
def encontrar_maior_frequencia(lista):
    # Conta a frequência de cada elemento na lista
    contagem = Counter(lista)

    # Encontrar o elemento com a maior frequência
    elemento_mais_frequente = max(contagem, key=lambda x: (contagem[x], x), default=None)

    return elemento_mais_frequente
def updates(nums,a, b,mfreq):
    for c in range(a, b+1):
        nums[c]+= mfreq
        if (nums[c] >= 9):
            nums[c]-= 9

    
frequecia = ([])
nums = []
acords = []
N = 0
Q = 0
a = 0
b = 0
while True:
    N = int(input('Digite o numero de teclas do piano:'))
    Q = int(input('Digite o numero de acordes:'))
    if (2 <= N <= 100000) and (1 <= Q <= 100000):
        break
for c in range(0, N):
    nums.append(1)

for c in range(Q):
    while True:
        a = int(input('Digite a primeira tecla:'))
        b = int(input('Digite a segunda tecla:'))
        
        if (0 <= a < b < N):
            break
        else:
            print('Valor de entrada invalido, tente novamente')
    tnums = tuple(nums)
    lnums = list(tnums[a:b+1])
    tnums = tuple(lnums)
    maiorfreq = encontrar_maior_frequencia(tnums)
    updates(nums,a, b, maiorfreq)
    acords.append(maiorfreq)
print(nums)
print(acords)
