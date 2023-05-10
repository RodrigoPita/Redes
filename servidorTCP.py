import socket

HOST = ''    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5005  # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
sock = socket.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
sock.bind( ( HOST, PORTA ) )

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
sock.listen(5) 

# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
novoSock, endereco = sock.accept() # retorna um novo socket e o endereco do par conectado
print ( 'Conectado com: ', endereco )

# dicionário para traduzir as palavras relacionadas a redes, do português para o inglês
dicio_redes = {'rede':b'network', 'enlace':b'link', 'roteador':b'router', 
	       'comutador':b'switch', 'cliente':b'client', 'servidor':b'server',
	       'hospedeiro':b'host', 'navegador':b'browser', 'endereço IP':b'IP address',
	       'fim-a-fim':b'peer-to-peer'}

while True:
	# depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE))
	msg = novoSock.recv(1024) # argumento indica a qtde maxima de dados
	if not msg: break 
	else: print(str(msg,  encoding='utf-8'))
	if ( dicio_redes.get( str( msg, encoding='utf-8' ) ) is not None ): msg_traduzida = dicio_redes[str( msg, encoding='utf-8' )]
	# envia mensagem de resposta
	novoSock.send( msg_traduzida ) 

# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close()
