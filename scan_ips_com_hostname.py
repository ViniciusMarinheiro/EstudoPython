import socket
from timeit import default_timer as timer

# Colocar IP de acordo com o range de IP da rede (alterar apenas o valor 15 caso necessário)
ip = '192.168.15.'
portas = [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 445]

def scan():

    # Incrimenta o final do IP de 0 a 255
    final_ip = list(range(255))
    for final in final_ip:
        ip_certo = f'{ip}{final}'

        for porta in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.1)
            codigo = cliente.connect_ex((ip_certo, porta))
            
            
            # Printa IPs com portas da lista abertas
            if codigo == 0:
                try:
                    output = socket.gethostbyaddr(str(ip_certo))
                    hostname = str(output).split("'")[1::2][0]
                except:
                    hostname = 'Sem hostname'
                print(f'Testando: {ip_certo}:{porta} -> Aberta | {hostname}')
    print('Scan Finalizado!')
    

start = timer()
scan()
print('Tempo: ', timer()-start)


