import socket

UDP_IP = "127.0.0.1" # endereço IP local
UDP_PORT = 5005      # porta que o servidor vai escutar

# dicionário para traduzir as palavras relacionadas a redes, do português para o inglês
dicio_redes = {'rede':b'network', 'enlace':b'link', 'roteador':b'router', 
	       'comutador':b'switch', 'cliente':b'client', 'servidor':b'server',
	       'hospedeiro':b'host', 'navegador':b'browser', 'endereço IP':b'IP address',
	       'fim-a-fim':b'peer-to-peer'}

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("Servidor de echo UDP iniciado em {}:{}".format(UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # espera por uma mensagem
    if ( dicio_redes.get( str( data, encoding='utf-8') ) is not None ):
        data_traduzida = dicio_redes[ str( data, encoding='utf-8' )]
    print("Mensagem de {}: {}".format(addr, data))

		# envia a mensagem de volta para o endereço que enviou
    sock.sendto(data_traduzida, addr)
