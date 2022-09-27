#este arquivo não é usado pelo site, apenas fou ultilizado durante sua criação para acelerar e automatizar processos
#nos métodos a seguir fora usado tanto arquivo aves quanto o répteis
'''
este script se baseia na ideia de abrir um arquivo onde foi colado o nome de todas as imagens dentro de um
diretório para que assim se crie de forma automática uma tabela html contendo tais imagens e seus respectivos nomes
ps: ninguém aguenta cadastrar 70 animais manualmente na tabela!
'''

def imagens():
    with open('aves.txt', 'r') as arq:
        linhas=arq.readlines()
        imagens=[]
        for linha in linhas:
            Nlinha = linha.split()
            imagens.append(Nlinha[-1])
        return imagens

def nomeCerto(nome):
    Nnome = ''
    nome = nome.split('.')[0]
    for i in range(len(nome)-1):
        Nnome+=nome[i]
        if nome[i+1].isupper():
            Nnome+=' '
    Nnome+=nome[-1]
    Nnome =Nnome.capitalize()
    return Nnome
                
def html():
    html = '<table class="animais" cellspaciing="20px">\n'
    ordem = True
    for imagem in imagens():
        nome = nomeCerto(imagem)
        if ordem:
            html+=f'\t<tr>\n\t\t<td class="img" style="background-image:url(imagens/{imagem})"></td>\n\t\t<td>{nome}</td>\n\t</tr>\n'
            ordem = False
        else:
            html+=f'\t<tr>\n\t\t<td>{nome}</td>\n\t\t<td class="img" style="background-image:url(imagens/{imagem})"></td>\n\t</tr>\n'
            ordem = True
    html+='</table>'
    return html
