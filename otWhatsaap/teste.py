with open("./funcoes_e_Dados/Lista1.csv",'r') as file:
    for c in file:

        if c =='112,67923,Dance With Me\n':
            print('ok')
        else:
            pass
    file.close()