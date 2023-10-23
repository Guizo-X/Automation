import pyautogui as pa
import time

try:
    pa.press('win')
    pa.write('opera')
    pa.PAUSE = 2
    pa.press('enter')

    # Aguarda a janela do Opera abrir
    pa.PAUSE = 4  # Ajuste o tempo de pausa conforme necessário

    pa.hotkey("ctrl", "e")
    pa.write("https://www.leagueofgraphs.com/pt/summoner/br/Ghost%20Rid3r")
    pa.press('enter')

    # Aguarda o carregamento da página (você pode verificar elementos específicos aqui)
    time.sleep(5)  # Ajuste o tempo de espera conforme necessário

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    pa.PAUSE = 1  # Restaura o tempo de pausa padrão
