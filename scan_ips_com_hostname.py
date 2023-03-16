import ipaddress
import socket
from timeit import default_timer as timer


network = ipaddress.ip_network('192.168.15.0/24')
portas = [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 445]


def scan():
    for ip in network:
        
        

        for porta in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.1)
            codigo = cliente.connect_ex((str(ip), porta))
            
            
            # Printa IPs com portas da lista abertas
            if codigo == 0:
                try:
                    output = socket.gethostbyaddr(str(ip))
                    hostname = str(output).split("'")[1::2][0]
                except:
                    hostname = 'Sem hostname'
                print(f'Testando: {ip}:{porta} -> Aberta | {hostname}')
    print('Scan Finalizado!')

start = timer()
scan()
tempo = timer()-start
print(f'Tempo: {tempo:.2f} segundos')
