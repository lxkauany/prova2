# Pesquisa
#
# Funcionamento do try/except no Python
# O try/except é usado para tratar erros (exceções) e evitar
# que o programa pare de funcionar quando algo dá errado.
#
#  try:
#    Contém o código que será testado. Se não houver erro,
#    o programa segue normalmente.
#
#  except:
#    Executado somente se ocorrer erro dentro do try.
#    Pode capturar erros específicos (ex.: ZeroDivisionError)
#    ou de forma genérica (qualquer erro).
#
#  else:
#    Executado apenas se o bloco try não gerar erro.
#    É útil quando você quer rodar algo somente se deu tudo certo.
#
#  finally:
#    Executado sempre, independentemente de ter erro ou não.
#    Muito usado para fechar arquivos, desconectar do banco
#    ou liberar recursos importantes.
#
# Em resumo:
#  try tenta rodar o código.
#  except trata o erro caso aconteça.
#  else roda só quando não há erro.
#  finally roda sempre, com ou sem erro.


# Colocar 2 exemplos de funcionamento usando função + arquivo + try/except

#Exenplo 1

def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")  
        conteudo = arquivo.read()          
        print("Conteúdo do arquivo:\n", conteudo)
    except FileNotFoundError:              
        print("Erro: Arquivo não encontrado!")
    except Exception as erro:              
        print("Ocorreu um erro:", erro)
    finally:
        try:
            arquivo.close()                
        except:
            pass                          

ler_arquivo("dados.txt")



# Exemplo 2

def dividir_numeros(a, b):
    try:
        resultado = a / b                  
    except ZeroDivisionError:             
        print("Erro: Não é possível dividir por zero!")
    except TypeError:                    
        print("Erro: Valores precisam ser números!")
    else:
        print("Resultado da divisão:", resultado)
    finally:
        print("Operação finalizada.\n")  

dividir_numeros(10, 2)
dividir_numeros(10, 0)
dividir_numeros(10, "a")