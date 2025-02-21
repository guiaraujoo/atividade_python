tempo_evento = int(input("Digite o tempo do evento em segundos: "))

minutos_evento = tempo_evento // 60

segundos_evento = tempo_evento % 60

horas_evento = minutos_evento // 60

print(f"O evento dura {horas_evento} horas, {minutos_evento % 60} minutos e {segundos_evento} segundos.")