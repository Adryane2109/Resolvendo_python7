
# Abrir o arquivo original para leitura
arquivo = open("Python_07_nobody.txt", "r")

# Ler todo o conteúdo do arquivo
texto = arquivo.read()

# Fechar o arquivo original
arquivo.close()

# Substituir todas as ocorrências de Nobody por Michael
texto = texto.replace("Nobody", "Michael")

# Criar um novo arquivo para escrever o texto modificado
saida = open("Michael.txt", "w")

# Escrever o texto no novo arquivo
saida.write(texto)

# Fechar o arquivo de saída
saida.close()
