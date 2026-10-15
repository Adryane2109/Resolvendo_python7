
# Importar o módulo de expressões regulares
import re

# Abrir o arquivo FASTA para leitura
arquivo = open("Python_07.fasta", "r")

# Ler todo o conteúdo do arquivo
texto = arquivo.read()

# Fechar o arquivo
arquivo.close()

# Procurar linhas que seguem o formato de cabeçalho FASTA
cabecalhos = re.findall(r"^>(\S+)\s*(.*)", texto, re.MULTILINE)

# Imprimir o identificador e a descrição
for id, desc in cabecalhos:
    print('id:"' + id + '" desc:"' + desc + '"')
