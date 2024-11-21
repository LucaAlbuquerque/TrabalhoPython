import os
os.system("cls")
import random

opc=0
quantT=0
quantC=0
quantMT=0
quantMC=0
total_corridoT=[]
total_corridoC=[]
T={}
C={}
MDT={}
MDC={}
distanciaM={}
tempoM={}
distanciaPaceT=[]
tempoPaceT=[]
distanciaPaceC=[]
tempoPaceC=[]

def Fadd():
    if addT_C=="T":
        try:
            arquivotxt=open('treinos.txt','w',encoding='utf8')
            try:
                data = input("Digite a data do treino (formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (em Km): "))
                distanciaPaceT.append(distancia)
                tempo = float(input("Digite o tempo de duração (em horas): "))
                tempoPaceT.append(tempo)
                localizacao = input("Digite a localização do treino: ")
                condicoes_climaticas = input("Digite a condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                T[quantT]=(f"{quantT}º TREINO-> |Data: {data} |Distância: {distancia}Km |Tempo de duração: {tempo}h |Localização: {localizacao} |Condição climática: {condicoes_climaticas}\n")
                for i in T:
                    arquivotxt.write(T[i])
                print("Treino registrado com sucesso!\n")
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            arquivotxt.close()
        except FileNotFoundError:
            print("Arquivo não encontrado.\n")

    elif addT_C=="C":
        try:
            arquivotxt=open('competicoes.txt','w',encoding='utf8')
            try:
                data = input("Digite a data da competição (formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (em Km): "))
                distanciaPaceC.append(distancia)
                tempo = float(input("Digite o tempo de duração (em horas): "))
                tempoPaceC.append(tempo)
                localizacao = input("Digite a localização da competição: ")
                condicoes_climaticas = input("Digite a condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                C[quantC]=(f"{quantC}ª COMPETIÇÃO-> |Data: {data} |Distância: {distancia}Km |Tempo de duração: {tempo}h |Localização: {localizacao} |Condição climática: {condicoes_climaticas}\n")
                for i in C:
                    arquivotxt.write(C[i])
                print("Competição registrada com sucesso!\n")
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            arquivotxt.close()
        except FileNotFoundError:
            print("Arquivo não encontrado.\n")
    
    else:
        print("Opção inválida.\n")

def Fvisu():
    if vizuT_C=="T":
        if not T:
            print("Não há treinos registrados.")
        else:
            with open('treinos.txt', 'r', encoding='utf8') as arquivotxt:
                    treinos = arquivotxt.readlines()
                    print("".join(treinos).strip())
    elif vizuT_C=="C":
        if not C:
            print("Não há competições registradas.")
        else:
            with open('competicoes.txt', 'r', encoding='utf8') as arquivotxt:
                    competicoes = arquivotxt.readlines()
                    print("Competições registradas: ")
                    print("".join(competicoes).strip())
    else:
        print("Opção inválida.\n")

def Fupdt():    
    if updtT_C=="T":
        if not T:
            print("Não há treinos registrados.")
        else:
            with open('treinos.txt', 'r', encoding='utf8') as arquivotxt:
                    treinos = arquivotxt.readlines()
                    print("Treinos registrados: ")
                    print("".join(treinos).strip())
            try:
                numUpdt = int(input("Digite o número do treino que você quer atualizar: "))
                nova_data = input("Digite a nova data do treino (Formato DD-MM-YYYY): ")
                nova_distancia = float(input("Digite a nova distância percorrida (em km): "))
                novo_tempo = float(input("Digite o novo tempo de duração (em horas): "))
                nova_localizacao = input("Digite a nova localização do treino: ")
                nova_condicoes_climaticas = input("Digite a nova condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                T[numUpdt]=(f"{numUpdt}º TREINO-> |Data: {nova_data} |Distância: {nova_distancia}Km |Tempo de duração: {novo_tempo}h |Localização: {nova_localizacao} |Condição climática: {nova_condicoes_climaticas}\n")
            except ValueError:
                print("Alguma informação digitada é inváida.\n")        
            try:
                with open('treinos.txt','w',encoding='utf8') as arquivotxt:
                    for i in T:
                        arquivotxt.write(T[i])
                print("Treino atualizado com sucesso.\n")
            except FileNotFoundError:
                print("Arquivo não encontrado.\n")

    elif updtT_C=="C":
        if not C:
            print("Não há competições registradas.")
        else:
            with open('competicoes.txt', 'r', encoding='utf8') as arquivotxt:
                    competicoes = arquivotxt.readlines()
                    print("Competições registradas: ")
                    print("".join(competicoes).strip())
            try:
                numUpdt = int(input("Digite o número da competição que você quer atualizar: "))
                nova_data = input("Digite a nova data da competição (formato DD-MM-YYYY): ")
                nova_distancia = float(input("Digite a nova distância percorrida (em Km): "))
                novo_tempo = float(input("Digite o novo tempo de duração (em horas): "))
                nova_localizacao = input("Digite a nova localização da competição: ")
                nova_condicoes_climaticas = input("Digite a nova condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                C[numUpdt]=(f"{numUpdt}ª COMPETIÇÃO-> |Data: {nova_data} |Distância: {nova_distancia}km |Tempo de duração: {novo_tempo}h |Localização: {nova_localizacao} |Condição climática: {nova_condicoes_climaticas}\n")
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            try:
                with open('competicoes.txt','w',encoding='utf8') as arquivotxt:
                    for i in C:
                        arquivotxt.write(C[i])
            except FileNotFoundError:
                print("Arquivo não encontrado.\n")
            print("Competição atualizada com sucesso!\n")
    
    else:
        print("Opção inválida.\n")

def Fexc():
    if excT_C=="T":
        if not T:
            print("Não há treinos registrados.")
        else:
            try:
                with open('treinos.txt', 'r', encoding='utf8') as arquivotxt:
                    treinos = arquivotxt.readlines()
                    print("Treinos registrados: ")
                    print("".join(treinos).strip())
                    try:
                        numExc = int(input("Digite o número do registro de treino que você quer excluir: "))
                    except ValueError:
                        print("Digite um valor inteiro!\n")
                    if 1<=numExc<=len(T):
                        del T[numExc]
                        
                with open('treinos.txt','w',encoding='utf8') as arquivotxt:
                    for i in T:
                        arquivotxt.write(T[i])
            except FileNotFoundError:
                print("Arquivo não encontrado.\n")

            print("Treino excluído com sucesso!\n")

    elif excT_C=="C":
        if not C:
            print("Não há competições registradas.")
        else:
            try:
                with open('competicoes.txt', 'r', encoding='utf8') as arquivotxt:
                    competicoes = arquivotxt.readlines()
                    print("Competições registradas: ")
                    print("".join(competicoes).strip())
                    try:
                        numExc = int(input("Digite o número do registro de competição que você quer excluir: "))
                    except ValueError:
                        print("Digite um valor inteiro!\n")
                    if 1<=numExc<=len(C):
                        del C[numExc]
                    
                with open('competicoes.txt','w',encoding='utf8') as arquivotxt:
                    for i in C:
                        arquivotxt.writelines(C[i])
            except FileNotFoundError:
                print("Arquivo não encontrado.\n")

            print("Competição excluída com sucesso!\n")

    else:
        print("Opção inválida.\n")

def FaddMeta():
    if addMetaT_C=="T":
        medida_tempo_meta=input("Sua meta será semanal, mensal ou anual? (S / M / A): ").upper()
        try:
            if medida_tempo_meta=="S":
                tempo_meta=int(input("Digite em quantas semanas você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="semanas"
                else:
                    s_m_a="semana"
            elif medida_tempo_meta=="M":
                tempo_meta=int(input("Digite em quantos meses você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="meses"
                else:
                    s_m_a="mês"
            elif medida_tempo_meta=="A":
                tempo_meta=int(input("Digite em quantos anos você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="anos"
                else:
                    s_m_a="ano"
            else:
                print("Opção inválida.\n")
        except ValueError:
            print("Digite um valor inteiro!\n")

        distancia_meta = input(f"Digite a distância que você quer correr em {tempo_meta} {s_m_a} (em Km): ")
        distanciaM[quantMT] = distancia_meta
        MDT[quantMT]=(f"{quantMT}ª META DE TREINO-> {distancia_meta}km em {tempo_meta} {s_m_a}")
        print("Meta de treino registrada com sucesso!\n")

    elif addMetaT_C=="C":
        medida_tempo_meta = input("Sua meta será semanal, mensal ou anual? (S / M / A): ").upper()
        try:
            if medida_tempo_meta=="S":
                tempo_meta = int(input("Digite em quantas semanas você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="semanas"
                else:
                    s_m_a="semana"
            elif medida_tempo_meta=="M":
                tempo_meta = int(input("Digite em quantos meses você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="meses"
                else:
                    s_m_a="mês"
            elif medida_tempo_meta=="A":
                tempo_meta = int(input("Digite em quantos anos você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="anos"
                else:
                    s_m_a="ano"
            else:
                print("Opção inválida.\n")
        except ValueError:
            print("Digite um valor inteiro!\n")
   
        distancia_meta = input(f"Digite a distância que você quer correr em {tempo_meta} {s_m_a} (em Km): ")
        distanciaM[quantMC] = distancia_meta
        MDT[quantMC] = (f"{quantMC+1}ª META DE COMPETIÇÃO-> {distancia_meta}km em {tempo_meta} {s_m_a}")
        print("Meta de competição registrada com sucesso!\n")

    else:
        print("Opção inválida.\n")

def FupdtMeta():
    if updtMetaT_C=="T":
        if not MDT:
            print("Não há metas de treino registradas.")
        else:
            total_corridoT=0
            print("Metas e desafios de treino disponíveis para atualização: ")
            for i in MDT:
                print(f"{i}: {MDT[i]}")
            try:
                numUpdtMeta = int(input("Digite o número da meta de treino que você quer atualizar o progresso: "))
                km_corridos = float(input("Digite a distância já corrida (em Km): "))
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            total_corridoT+=km_corridos
            distancia_faltando = int(distanciaM[numUpdtMeta])-total_corridoT
            distanciaM[numUpdtMeta] = distancia_faltando
            if (distancia_faltando)>0:
                print("Progresso em meta de treino atualizado com sucesso!")
                print(f"Ainda faltam {distancia_faltando}km para bater a meta\n")
            else:
                print(f"Parabéns! Você bateu a {numUpdtMeta}ª meta de treinos!\n")
                del MDT[numUpdtMeta]
    
    elif updtMetaT_C=="C":
        if not MDC:
            print("Não há metas de competição registradas.")
        else:
            total_corridoC=0
            print("Metas e desafios de competição disponíveis para atualização: ")
            for i in MDT:
                print(f"{i}: {MDT[i]}")
            try:
                numUpdtMeta = int(input("Digite o número da meta de competição que você quer atualizar o progresso: "))
                km_corridos = float(input("Digite a distância já corrida (em Km): "))
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            total_corridoC+=km_corridos
            distancia_faltando = int(distanciaM[numUpdtMeta])-total_corridoC
            distanciaM[numUpdtMeta-1] = distancia_faltando
            if (distancia_faltando)>0:
                print("Progresso de meta de competição atualizado com sucesso!")
                print(f"Ainda faltam {distancia_faltando}km para bater a meta\n")
            else:
                print(f"Parabéns! Você bateu a {numUpdtMeta}ª meta de competições!\n")
                del MDC[numUpdtMeta]
        
    else:
        print("Opção inválida.\n")

def Fextra():
    if paceT_C=="T":
        if not T:
            print("Não há treinos registrados.")
        else:
            with open('treinos.txt', 'r', encoding='utf8') as arquivotxt:
                    treinos = arquivotxt.readlines()
                    print("Treinos registrados: ")
                    print("".join(treinos).strip())
            try:
                numPace = int(input("Digite o número do treino que você quer calcular o pace: "))
                if tempoPaceT[numPace-1]!=0:
                    pace = int(distanciaPaceT[numPace-1])/int(tempoPaceT[numPace-1])
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            print(f"O pace do {numPace}º treino é {pace}km/h\n")

    elif paceT_C=="C":
        if not C:
            print("Não há competições registradas.")
        else:
            with open('competicoes.txt', 'r', encoding='utf8') as arquivotxt:
                    competicoes = arquivotxt.readlines()
                    print("Competições registradas: ")
                    print("".join(competicoes).strip())
            try:     
                numPace = int(input("Digite o número da competição que você quer calcular o pace: "))
                if tempoPaceC[numPace-1]!=0:
                    pace = int(distanciaPaceC[numPace-1])/int(tempoPaceC[numPace-1])
            except ValueError:
                print("Alguma informação digitada é inválida.\n")
            print(f"O pace da {numPace}ª competição é {pace}km/h\n") 

    else:
        print("Opção inválida.\n")  

def Ffiltrar():
    if filtT_C == "T":
        if not T:
            print("Não há treinos registrados.")
        else:
            try:
                with open('treinos.txt', 'r', encoding='utf8') as arquivotxt:
                    treinos = arquivotxt.readlines()
                    print("Treinos registrados: ")
                    print("".join(treinos).strip())
                    dis_ou_temp = input("\nQuer filtrar os treinos por distância ou por tempo? (D \ T): ").upper()
                    if dis_ou_temp == "D":
                        distancia = float(input("Digite a distância para ser filtrada (Em Km): "))
                        filtrados = [treino for treino in treinos if str(distancia) in treino]
                        if filtrados:
                            print("\nTreinos filtrados por distância:")
                            for treino in filtrados:
                                print(treino.strip())
                        else:
                            print("\nNenhum treino encontrado.")
                    elif dis_ou_temp == "T":
                        tempo = float(input("Digite o tempo para ser filtrado (Em horas): "))
                        filtrados = [treino for treino in treinos if str(tempo) in treino]
                        if filtrados:
                            print("\nTreinos filtrados por tempo: ")
                            for treino in filtrados:
                                print(treino.strip())
                        else:
                            print("\nNenhum treino encontrado.")
                    else:   
                        print("Opção inválida.")
            except FileNotFoundError:
                print("\nArquivo não encontrado.")

    elif filtT_C == 'C':
        if not C:
            print("Não há competições registradas.")
        else:
            try:
                with open('competicoes.txt', 'r', encoding='utf8') as arquivotxt:
                    competicoes = arquivotxt.readlines()
                    print("Competições registradas: ")
                    print("".join(competicoes).strip())
                    dis_ou_temp = input("\nQuer filtrar as competições por distância ou tempo (D \ T)?: ").upper()
                    if dis_ou_temp == "D":
                        distancia = float(input("Digite a distância para ser filtrada (Em Km): "))
                        filtrados = [competicao for competicao in competicoes if str(distancia) in competicao]
                        if filtrados:
                            print("\nCompetições filtradas por distância:")
                            for competicao in filtrados:
                                print(competicao.strip())
                        else:
                            print("\nNenhuma competição encontrada.")
                    elif dis_ou_temp == "T":
                        tempo = float(input("Digite o tempo para ser filtrado (em horas): "))
                        filtrados = [competicao for competicao in competicoes if str(tempo) in competicao]
                        if filtrados:
                            print("\nCompetições filtradas por tempo:")
                            for competicao in filtrados:
                                print(competicao.strip())
                        else:
                            print("\nNenhuma competição encontrada.")
                    else:
                        print("Opção inválida")
            except FileNotFoundError:
                    print("\nArquivo não encontrado.")

    else:
        print("\nOpção inválida.")

def Falea():
    dist=[2.5, 5, 8, 10, 15, 20, 21, 42]
    pace=[3.5, 4, 5, 5.5, 6]
    dist_sugestao=random.choice(dist)
    pace_sugestao=random.choice(pace)
    if pace_sugestao == 3.5 or pace_sugestao == 4:
        if dist_sugestao == 42:
            print(f"TREINO SUGERIDO-> TREINO DE VELOCIDADE EM MARATONA |Distância: {dist_sugestao}Km |Pace: {pace_sugestao}Km/h")
        elif dist_sugestao == 21:
            print(f"TREINO SUGERIDO-> TREINO DE VELOCIDADE EM MEIA MARATONA| Distância: {dist_sugestao}Km| Pace: {pace_sugestao}Km/h")
        else:
            print(f"TREINO SUGERIDO-> TREINO DE VELOCIDADE| Distância: {dist_sugestao}Km| Pace: {pace_sugestao}Km/h")
    elif pace_sugestao == 5 or pace_sugestao == 5.5 or pace_sugestao == 6:
        if dist_sugestao == 42:
            print(f"TREINO SUGERIDO-> TREINO DE RESISTÊNCIA EM MARATONA| Distância: {dist_sugestao}")
        elif dist_sugestao == 21:
            print(f"TREINO SUGERIDO-> TREINO DE RESISTÊNCIA EM MEIA MARATONA| Distância: {dist_sugestao}")
        else:
            print(f"TREINO SUGERIDO-> TREINO DE RESISTÊNCIA| Distância: {dist_sugestao}")
    
while opc!=10:
    print("1. Fazer um registro")
    print("2. Visualizar os registros")
    print("3. Atualizar os registros")
    print("4. Excluir um registro")
    print("5. Registrar metas e desafios")
    print("6. Atualizar o progresso das metas e desafios")
    print("7. Calcular o seu pace")
    print("8. Filtrar os registros")
    print("9. Sugestão de treino aleatório")
    print("10. Parar")
    opc=int(input("\nDigite o que você quer fazer: "))
    
    if opc==1:
        addT_C = input("Quer registrar um treino ou uma competição?: (T \ C): ").upper()
        if addT_C=="T":
            quantT+=1
        elif addT_C=="C":
            quantC+=1
        Fadd()
        
    elif opc==2:
        vizuT_C = input("Quer visualizar os registros dos treinos ou das competições? (T \ C): ").upper()
        Fvisu()

    elif opc==3:
        updtT_C = input("Quer atualizar os registros dos treinos ou das competições? (T \ C): ").upper()
        Fupdt()

    elif opc==4:
        excT_C = input("Quer excluir um registro de treino ou de competição? (T \ C): ").upper()
        Fexc()
    
    elif opc==5:
        addMetaT_C = input("Quer registrar uma meta de treino ou de competição? (T \ C): ").upper()
        if addMetaT_C=="T":
            quantMT+=1
        elif addMetaT_C=="C":
            quantMC+=1
        FaddMeta()

    elif opc==6:
        updtMetaT_C = input("Quer atualizar o progresso de uma meta de treino ou de competição? (T \ C): ").upper()
        FupdtMeta()
        
    elif opc==7:
        paceT_C = input("Quer calcular o pace de um treino ou de uma competição? (T \ C): ").upper()
        Fextra()

    elif opc==8:
        filtT_C = input("Quer filtrar um registro de treino ou de competição? (T \ C): ").upper()
        Ffiltrar()

    elif opc==9:
        Falea()

    elif opc==10:
        print("Encerrando...")

            
