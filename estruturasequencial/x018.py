# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = int(input("Insira o tamanho do arquivo para download [em MB]: "))
velocidade_internet = int(input("Insira a velocidade de um link de Internet [em Mbps]: "))

Megabits_equivalente = tamanho_arquivo * 8

tempo_download = Megabits_equivalente / velocidade_internet

if tempo_download < 60:
  print("Para baixar um arquivo de {}MB com uma internet de {}Mbps, será baixado aproximadamente {:.0F} segundos".format(tamanho_arquivo, velocidade_internet, tempo_download))
elif 3.600 < tempo_download >= 60:
  print("Para baixar um arquivo de {}MB com uma internet de {}Mbps, será baixado aproximadamente {:.0F} minutos".format(tamanho_arquivo, velocidade_internet, tempo_download/60))
else:
  print("Para baixar um arquivo de {}MB com uma internet de {}Mbps, será baixado aproximadamente {:.0F} horas".format(tamanho_arquivo, velocidade_internet, tempo_download/3.600))