import hashlib
import datetime as data

class Bloco:
    def __init__(self, indice, carimbo, dados, hash_anterior):
        self.indice = indice
        self.carimbo = carimbo
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.hash = self.hash_do_bloco()
    def hash_do_bloco(self):
        texto = (str(self.indice) + str(self.carimbo) + str(self.dados) + str(self.hash_anterior))
        sha = hashlib.sha256()
        sha.update(texto.encode('ascii'))
        return sha.hexdigest()


def bloco_genesis():
    return Bloco(0, data.datetime.now(), 'PyBlock Genesis', 0)


def criar_bloco(bloco_anterior):
    indice = bloco_anterior.indice + 1
    carimbo = data.datetime.now()
    dados = 'PyBlock# ' + str(indice)
    hash_anterior = bloco_anterior.hash
    return Bloco(indice, carimbo, dados, hash_anterior)


blockchain = [bloco_genesis()]
bloco_anterior = blockchain[0]

quantidade_blocos_para_adicionar = 20

for i in range(0, quantidade_blocos_para_adicionar):
    bloco_novo = criar_bloco(bloco_anterior)
    blockchain.append(bloco_novo)
    bloco_anterior = bloco_novo

print('\n')

for bloco in blockchain:
    print(f'''
Index        : {bloco.indice}
Timestamp    : {bloco.carimbo}
Data         : {bloco.dados}
Hash         : {bloco.hash}
Previous hash: {bloco.hash_anterior}\n
''')
