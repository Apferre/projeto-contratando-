#projeto individual 2 M2
#Uma empresa de recrutamento recebeu muitos currículos
#para determinadas vagas e agora precisa classificar
#quantos candidatos tem o perfil necessário e quantos
#candidatos estão concorrendo a cada vaga específica.
#As palavras-chave das vagas são:
#◼ Vaga 1: Python, Programação, Desenvolvimento;
#◼ Vaga 2: Análise de dados, Dados, SQL
#⇨ Nosso código deve ficar pedindo para qual vaga a pessoa se inscreveu e o resumo de
#cada participante em loop (só deve parar quando inserir o número 0 na pergunta davaga).
# O texto do resumo/minibio vai ser informado pelo usuário (como desafio extra você
#pode tentar ler esse texto de arquivos txt em uma pasta e eliminar essa etapa de pedir
#os textos em loop) e então vamos checar se temos as palavras-chave necessárias e
#marcar como um candidato válido para a vaga.
#minibio=txt
#ler texto (txt) busca
#vaga= {1:(python,progama,desem)}
s=""
Candidatos=[]
Curriculo=[]
palavra_chave = ['python, desenvolvedor']
perfil_vagas=[]
key={}
while (s == 'sim'):
    
        Pergunta= input("Deseja continuar?")
        candidatos= str.title(input("Digite seu nome e sobrenome"))
        resume= input(("Digite sua profissão"))
        Curriculo.append([Candidatos,resume])
        #Pergunta= input("Deseja continuar?")
        Vagas={1:"Python"or"desenvolvedor" or "programação",
               2: "Analise de dados" or "dados" or "SQL"}
        x = Curriculo.split(',')

        def analise(i):# Cria uma lista vazia para armazenar as palavras-chave encontradas no currículo# Percorre o dicionário de vagas
                
                if (Vagas == '1') and (i in Vagas[1]) and (x.index(i) == 0): #observa a primeira habilidade do candidato                    print("Palavra encontrada!")
                    print("palavra encontrada!")
                

    
analise(i)  

  
    
    
    
    
#if Curriculo in Vagas:{1:[0],2:[1]}
   # print("Palavra encontrada!") # Verifica se alguma das palavras-chave da vaga está presente no currículo


  
  
#analise()
  
  
  
'''     
 for key in key:
            if key.lower() in resume.lower():
                # Adiciona a palavra-chave encontrada à lista de palavras-chave encontradas
                palavra_chave.append(key)
    
    # Retorna a lista de palavras-chave encontradas no currículo
    return palavra_chave

analise_resumo()

    
    
    
    
    
    




#if Pergunta=='Sim':

if 'dados'or 'programação' in resume:
    print("Palavra encontrada!")

else:
    print("não")
    
    if Curriculo 
# break
#def analise_resumo(minbio,vagas):
# Cria uma lista vazia para armazenar as palavras-chave encontradas no currículo
'''