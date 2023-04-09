# Verificador de Status do Servidor

Este é um  programa Python que verifica o status de um servidor da web e envia alertas caso ele esteja indisponível. Ele também inclui recursos para verificação manual e periódica do status do servidor.

## Como funciona

O programa usa a biblioteca `requests` do Python para enviar solicitações HTTP para o servidor especificado e verificar se ele está respondendo com sucesso. Se o servidor estiver inativo, o programa exibe um alerta na tela para notificar o usuário.

O programa possui uma GUI criada com a biblioteca `PySimpleGUI`, que permite ao usuário inserir a URL do servidor a ser verificado, iniciar uma verificação manual e agendar verificações automáticas em intervalos de tempo especificados.

O programa usa a biblioteca `threading` do Python para executar verificações de status do servidor em segundo plano em intervalos regulares de tempo. Ele também usa a biblioteca `time` para aguardar o intervalo de tempo especificado antes de iniciar a próxima verificação.

## Tecnologias e conceitos utilizados

- Python
- Bibliotecas: `requests`, `PySimpleGUI`, `threading`
- GUI
- Verificação manual e periódica do status do servidor
- Threads e eventos de parada
- Tratamento de exceções

<h2>Exemplo</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/50200471/230754162-50cfa742-94c8-48b5-beb9-078f5b7f7c8c.png" width="350" title="hover text">
  <img src="https://user-images.githubusercontent.com/50200471/230754175-88a080bd-6cbb-4b05-9e61-452ecc0feb51.png" width="350" alt="accessibility text">
</p


## Como usar

1. Clone ou baixe este repositório para o seu computador.
2. Instale as bibliotecas necessárias (PySimpleGUI e requests) usando o pip: `pip install PySimpleGUI requests`
3. Abra o arquivo `statuschecker.py` em um editor de código.
4. Execute o arquivo a partir do terminal ou prompt de comando: `python statuschecker.py`
5. Baixe o programa .exe em Releases para verificação contínua

## Como contribuir

Sinta-se à vontade para contribuir com este projeto, fazendo um fork deste repositório e enviando um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
