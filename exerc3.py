
# Importar o módulo de expressões regulares
import re

# Abrir o arquivo FASTA para leitura
arquivo = open("Python_07.fasta", "r")

# Ler todo o conteúdo do arquivo
texto = arquivo.read()

# Fechar o arquivo
arquivo.close()

# Encontrar todas as linhas que começam com >
cabecalhos = re.findall(r"^>.*", texto, re.MULTILINE)

# Imprimir os cabeçalhos encontrados
for cabecalho in cabecalhos:
    print(cabecalho)
