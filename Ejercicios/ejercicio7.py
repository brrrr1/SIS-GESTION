def ganador(jugada1, jugada2):
    if jugada1 == jugada2:
        return "Tie"  # Empate
    elif (jugada1 == "R" and jugada2 == "S") or (jugada1 == "S" and jugada2 == "P") or (jugada1 == "P" and jugada2 == "R"):
        return "Player 1"  # Player 1 gana
    else:
        return "Player 2"  # Player 2 gana

def quien_gana(partidas):
    player1_gana = 0
    player2_gana = 0
    empate = 0
    
    for partida in partidas:
        resultado = ganador(partida[0], partida[1])
        if resultado == "Player 1":
            player1_gana += 1
        elif resultado == "Player 2":
            player2_gana += 1
        else:
            empate += 1
    
    # Determinamos el ganador general
    if player1_gana > player2_gana:
        return "Player 1"
    elif player2_gana > player1_gana:
        return "Player 2"
    else:
        return "Tie"

partidas = [("R", "S"), ("S", "R"), ("P", "S")]
resultado = quien_gana(partidas)
print(resultado) 
