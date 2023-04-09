# Encurtador de URL

Este projeto é um encurtador de URL simples e eficiente que permite aos usuários encurtar URLs longas usando o serviço TinyURL e copiar o resultado para a área de transferência do sistema. A aplicação foi desenvolvida em Python com o auxílio das bibliotecas pyshorteners e tkinter.

## Tecnologias e Conceitos

- Python
- Biblioteca pyshorteners para interagir com serviços de encurtamento de URL
- Biblioteca tkinter para criar interfaces gráficas
- GUI (Interface Gráfica do Usuário) usando a biblioteca tkinter
- APIs de encurtamento de URL com a biblioteca pyshorteners

## Como funciona

- O usuário insere a URL longa no campo de entrada.
- Ao clicar no botão “Encurtar URL”, a aplicação chama a função shorten_url.
- A função shorten_url usa a biblioteca pyshorteners para gerar uma URL encurtada usando o serviço TinyURL.
- A URL encurtada é exibida em um rótulo abaixo do campo de entrada.
- O usuário pode clicar no botão “Copiar URL” para copiar a URL encurtada para a área de transferência do sistema.

## Exemplo

<p align="center">
  <img src="https://user-images.githubusercontent.com/50200471/230754162-50cfa742-94c8-48b5-beb9-078f5b7f7c8c.png" width="350" title="hover text">
  <img src="https://user-images.githubusercontent.com/50200471/230754175-88a080bd-6cbb-4b05-9e61-452ecc0feb51.png" width="350" alt="accessibility text">
</p>

## Modificações e aplicações úteis

Este projeto pode ser adaptado para diversas aplicações. Algumas modificações possíveis incluem:

- Suportar outros serviços de encurtamento de URL, como bit.ly ou goo.gl, simplesmente modificando a chamada à biblioteca pyshorteners.
- Implementar recursos adicionais, como histórico de URLs encurtadas ou compartilhamento direto do resultado nas redes sociais.
- Integrar a funcionalidade de encurtamento de URL em outras aplicações ou sistemas.
- Contribuição Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue no GitHub ou enviar um pull request com suas sugestões e melhorias. Por favor, siga as diretrizes de contribuição e o código de conduta do projeto.

## Licença
Este projeto está licenciado sob a Licença MIT que permite o uso, cópia, modificação e distribuição livre do código-fonte, desde que a licença original seja incluída e os direitos autorais sejam respeitados.
