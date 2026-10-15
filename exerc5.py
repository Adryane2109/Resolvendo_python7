
# Importar o módulo de expressões regulares
import re

# Abrir o arquivo FASTA para leitura
arquivo = open("Python_07.fasta", "r")

# Ler todo o conteúdo do arquivo
texto = arquivo.read()

# Fechar o arquivo
arquivo.close()

# Encontrar os cabeçalhos e as sequências correspondentes
registros = re.findall(r"^>(\S+).*?\n(.*?)(?=^>|\Z)",
                       texto, re.MULTILINE | re.DOTALL)

# Percorrer os registros encontrados
for id, seq in registros:

    # Remover as quebras de linha da sequência
    seq = seq.replace("\n", "")

    # Imprimir o identificador e a sequência
    print("id:", id)
    print("seq:", seq)
