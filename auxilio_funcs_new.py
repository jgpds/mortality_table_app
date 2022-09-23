import pandas as pd
import numpy as np

standard = ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']

class Tables:
    """
    Parameter: w(int) -> The last age of the table, in other words (rows-1)
    Parameter: columns(list) -> List with the columns names in order. By Default this parameter is set to  ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']
    """
    #standard = ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']
    def __init__(self, w, columns = standard):
        self.w = w
        self.columns = columns
    def create(self):
        """
        Method that effectively create and returns the data frame.
        """
        self.df = pd.DataFrame(0, index=np.arange(self.w), columns=self.columns)
        self.df['x'] = self.df['x'].apply(lambda x: int(x))
        for row in range(self.w+1):
            self.df.at[row, 'x'] = row
            row += 1
        return self.df

def retorna_nome_arquivo(filepath):
    """
    Função que recebe o filepath e retorna o nome do ultimo arquivo. (Se passar de 17 caracteres insere reticências no final)
    """
    reverse_filepath = filepath[::-1]
    aux = []
    for i in reverse_filepath:
        if i != '/':
            aux.append(i)
        else:
            break
    nomeArquivo = ''.join(aux)[::-1]
    return nomeArquivo 

def completarTabela(filepath):
    """
    Função que recebe como argumento um data frame 'q_x', e com essa informação completa o resto da tabela.
    """
    df = pd.read_excel(filepath)

    feature_list = ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']
    #w = 117 # a ultima idade da tabua, ou seja, omega.
    w = len(df.index)-1
    df2 = pd.DataFrame(0, index=np.arange(w+1), columns=feature_list)   

    df2['q_x'] = df['q_x'] 

    df2['x'] = df2['x'].apply(lambda x: int(x))

    for row in range(w+1):
        df2.at[row, 'x'] = row
        row += 1
    
    # raiz = int(input("Quai a raiz da tabela? (primeiro valor de l_x) "))
    df2.at[0, 'l_x'] = 10000 #em vez de mil colocar raiz
    df2['l_x'] = df2['l_x'].apply(lambda x: float(x))
    i = 1
    while i < w+1:
        df2.at[i-1, 'd_x'] = df2.at[i-1, 'l_x']*df2.at[i-1, 'q_x']
        df2.at[i, 'l_x'] = df2.at[i-1, 'l_x'] - df2.at[i-1, 'd_x']
        i += 1

    df2['d_x'] = df2['l_x']*df2['q_x']

    df2['q_x'] = df2['d_x']/df2['l_x']

    df2['p_x'] = 1 - df2['q_x']
    
    df2['L_x'] = df2['L_x'].apply(lambda x: float(x))
    i = 0
    while i <= w:
        if i < w:
            df2.at[i, 'L_x'] = (df2.at[i, 'l_x'] + df2.at[i+1, 'l_x'])/2
            i += 1
        else:
            df2.at[i, 'L_x'] = (df2.at[i, 'l_x'])/2
            i += 1

    df2['T_x'] = df2['T_x'].apply(lambda x: float(x)) # <- i've tried this, but didn't work
    i = 0
    while i <= w:
        df2.at[i, 'T_x'] = df2.loc[i:w, 'L_x'].sum() # w = index of the last row
        i += 1

    df2['e_x'] = df2['T_x']/df2['l_x']

    df2['u_x'] = df2['u_x'].apply(lambda x: float(x))
    i = 1
    while i <= w:
        df2.at[i, 'u_x'] = (df2.at[i-1, 'd_x'] + df2.at[i, 'd_x'])/2*(1/df2.at[i, 'l_x'])
        i += 1
    
    df2['m_x'] = df2['d_x']/df2['L_x']

    return(df2)
