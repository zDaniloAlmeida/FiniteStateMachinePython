"Aluno:Danilo Alecrim Almeida"

""" Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá determinar se uma string de
entrada faz parte da linguagem 𝐿 definida por 𝐿 = {𝑥 | 𝑥 ∈ {𝑎, 𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏}
segundo o alfabeto Σ = {𝑎, 𝑏, 𝑐}.

    O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
  
    3
    abbaba
    abababb
    bbabbaaab
    
    Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será
representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
    
    abbaba: não pertence.
    
    A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. 

    Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor."""
  
#Desculpe se ficou meio confuso professor, não tive muita criatividade na hora de escolher o nome das def, mas são def A,B,C,D e E.

def A(string, cont):
    if (len(string) == cont):
        print(string + ": Pertence")
    else:
        if (string[cont] == 'b'):
          A(string, cont + 1)
        elif(string[cont] == 'c'):
          C(string)
        elif (string[cont] == 'a'):
          B(string, cont + 1)

def B(string, cont):
    if (len(string) == cont):
        print(string + ": Não Pertence")
    else:
        if (string[cont] == 'c' or string[cont] == 'a'):
            C(string)
        elif (string[cont] == 'b'):
            D(string, cont + 1)
        
def C(string):
    print(string + ": Não Pertence")

def D(string, cont):
    if (len(string) == cont):
        print(string + ": Não Pertence")
    else:
        if (string[cont] == 'c' or string[cont] == 'a'):
            C(string)
        elif (string[cont] == 'b'):
            E(string, cont + 1)
        
def E(string, cont):
    if (len(string) == cont):
        print(string + ": Pertence")
    else:
        if (string[cont] == 'b'):
            E(string, cont + 1)
        elif(string[cont] == 'c'):
          C(string)
        elif (string[cont] == 'a'):
            B(string, cont + 1)
        
def go(texto):
    if (isinstance(texto, str)):
        A(texto, 0)
    else:
        print("Não é uma String")

g = [open("test1.txt"), open("test2.txt"), open("test3.txt")]

for j in range(3):
  print("\nExecutando teste: ", j+1);
  cont = 0
  texto = []
  for line in g[j]:
      if (cont == 0):
          cont += 1
      else:
          texto.append(line.split("\n")[0].split(" ")[0])
  for i in range(len(texto)):
      go(texto[i])

print("\n\n\Fim!")