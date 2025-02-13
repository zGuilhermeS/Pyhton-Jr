import asyncio
import time

async def chamada_rede(id):  
    await asyncio.sleep(2)  # Simula uma chamada de rede de 2 segundos
    return f'Chamada {id} concluída'

async def main():
    inicio = time.time()
    resultados = await asyncio.gather(chamada_rede(1), chamada_rede(2), chamada_rede(3))  # Executa as chamadas em paralelo
    tempo_total = time.time() - inicio
    return resultados, tempo_total

if __name__ == '__main__':
    print(asyncio.run(main()))