#  Problema 1222
# https://www.beecrowd.com.br/judge/pt/problems/view/1222

from math import ceil

out = ''
while True:
  try:  
    nro_palavras, linhas_por_pag, carac_por_linha = [int(i) for i in input().split()]
    txt = input()
    list_txt_caracteres = list(txt)
    list_txt_palavras = txt.split()
    gasto = 0
    lin = 1
    for i in list_txt_palavras:
        if(len(i)+gasto+1 < carac_por_linha):
            gasto += len(i)+1
        else:
            gasto=0
            lin+=1
    out+= str(ceil(lin/linhas_por_pag))+'\n'
  except EOFError:
    print(out,end='')
    break