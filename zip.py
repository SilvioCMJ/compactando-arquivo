import zipfile

# puxando arquivo
arquivo = 'arquivo_exemplo.py'
# nome do arquivo final
nome_zip = 'exemplo.zip'

# Criar um objeto ZipFile em modo de escrita
with zipfile.ZipFile(nome_zip, 'w') as zipf:

    zipf.write(arquivo)

print(f'{arquivo} foi compactado em {nome_zip}')
