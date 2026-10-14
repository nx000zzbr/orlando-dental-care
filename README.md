# Orlando Dental Care · proposta de site novo

Site de cinco páginas para substituir o atual (odcare.com), feito para a apresentação ao cliente.
Abra `index.html` em qualquer navegador ou sirva a pasta com um servidor estático.

## Versão 2 (atual): limpa, separada por menu

- **Páginas:** Início (`index.html`), Serviços (`services.html`), Dra. Santos (`doctor.html`), Depoimentos (`testimonials.html`), Contato (`contact.html`). Menu fixo no topo, menu de celular, link ativo marcado.
- **Barrinhas de cor:** cada seção começa com uma barrinha na sua cor; cada família de serviço tem a sua (céu, verde, laranja, azul-petróleo); o logo é feito de quatro barrinhas; a "primeira visita" é uma barra dividida por tempo.
- **Idiomas:** botão Español / English no topo traduz todas as páginas e fica salvo entre elas. Espanhol em "usted"; inglês em ortografia americana.
- **Contato:** formulário que abre o e-mail com a mensagem pronta (sem backend ainda), mapa estático do OpenStreetMap com o pino no consultório, perguntas frequentes.
- **Geração:** as páginas são geradas por `python3 build.py` a partir de um só cabeçalho e rodapé. Edite `build.py` e rode de novo; ou edite os `.html` direto se preferir (nesse caso não rode o build).
- A versão 1 (página única, capítulos de cor) ficou guardada em `v1/`.

## A ideia (versão 1, mantida como referência)

**Toda a sua sonrisa, um só endereço.** O site atual diz, em texto pequeno, a coisa mais forte do consultório: uma só dentista faz tudo, da limpeza ao implante, e atende em inglês e espanhol. O novo site faz disso a estrutura da página:

- **Capítulos de cor.** Cada seção é um campo de cor inteiro, como as salas de um mesmo consultório. As cores vêm de Orlando: o céu, o lago Eola (que também é o azul-petróleo do logo atual), a areia dos postais antigos, a palmeira, a laranja de Orange County.
- **O título cortado pela linha d'água.** O hero é céu em cima, lago embaixo, e a frase atravessa a linha entre os dois.
- **Serviços como fichas que empilham.** As quatro famílias de serviço (estética, geral, restauradora, avançada) são quatro folhas de cor que deslizam uma sobre a outra ao rolar, cada uma com a lista completa do site atual e um desenho grande do assunto.
- **A primeira visita como uma barra.** Quatro segmentos, cada um do tamanho do tempo que a etapa leva. Vem direto da promessa do site atual de apresentar mais de um plano de tratamento.
- **De Bogotá a Orlando.** Postais antigos das duas cidades, impressos pela mesma gráfica (Tichnor Bros.) com décadas de diferença. Conta a história da Dra. Santos sem precisar de foto dela (que o cliente deve fornecer).
- **O telefone é o rodapé.** O número em tamanho de manchete, como uma só ação final.

**A coisa viva:** o botão "Español / English" no topo troca a página inteira de idioma, inclusive o aviso de "aberto agora" ao lado do horário, calculado no fuso de Orlando.

## Ideias para apresentar ao cliente (além do que já está na página)

1. **Agendamento online de verdade.** Trocar o `mailto:` por um sistema de agenda (Zocdoc, NexHealth, ou o que o consultório já usa). O botão "Book a visit" já está no lugar.
2. **Formulário de novo paciente em espanhol e inglês**, preenchido antes da visita, com assinatura digital. Reduz tempo de recepção.
3. **Página de Google Business atualizada**, com link para o site e as avaliações reais do Google puxadas para a seção de depoimentos.
4. **Fotos profissionais** da Dra. Santos, da equipe e do consultório. O site atual usa banco de imagens; fotos reais são o maior ganho de confiança possível. Os postais podem continuar como identidade visual ao lado delas.
5. **Texto em espanhol revisado por falante nativo colombiano** (a tradução atual é minha e deve ser revisada).
6. **Seção de seguros aceitos** com a lista real (o site atual não diz quais planos aceita).
7. **WhatsApp / SMS** como canal de contato, muito usado pela comunidade latina de Orlando.
8. **Domínio e e-mail profissionais**: hoje o contato é um Gmail. `hola@odcare.com` custa pouco e passa outra impressão.
9. **SEO local**: título e descrição já estão prontos; falta cadastrar o site no Google Search Console, adicionar marcação `LocalBusiness` (schema.org) e criar páginas por serviço (implantes, Invisalign, urgências) se o cliente quiser ranquear por procedimento.
10. **Vídeo curto da Dra. Santos** (30 s, em espanhol e inglês) no lugar do bloco "De Bogotá a Orlando" ou abaixo dele.
11. **Promoção de primeira visita** (exame + raio-X com preço fechado), se o consultório fizer isso, cabe como uma linha na seção "Your first visit".
12. **Acessibilidade**: a página já tem foco visível, contraste alto e texto real em vez de imagens; manter isso em qualquer CMS escolhido.

## O que é amostra e precisa ser confirmado pelo cliente

- Durações da primeira visita (15 / 10 / 20 min, "o tempo que precisar").
- "A maioria dos planos PPO é aceita" e "estacionamento gratuito na porta" nas perguntas frequentes.
- "Horários do mesmo dia reservados quando possível" nas urgências.
- Os depoimentos são os do site atual, dois deles encurtados (Veronica Mendez e Hubert van Alphen).
- Hoje não há foto da Dra. Santos nem do consultório; o cliente deve fornecer.
- Tradução para o espanhol feita por mim, no tratamento "usted" e com vocabulário neutro ("empaste" em vez do colombiano "calza"); vale uma revisão final por falante nativo.

## Imagens usadas e créditos

Nenhuma imagem é apresentada como se fosse do consultório. Créditos aparecem no rodapé da página.

| Arquivo | Título | Autor / fonte | Licença |
| --- | --- | --- | --- |
| assets/orlando-eola-postcard.jpg | Orlando skyline from across Eola, Orlando, Florida, "the city beautiful" | Boston Public Library, Tichnor Brothers Collection, via Flickr/Openverse | CC BY 2.0 |
| assets/orlando-courthouse-postcard.jpg | Orange County court house, Orlando, Florida | Boston Public Library, via Flickr/Openverse | CC BY 2.0 |
| assets/orlando-greetings-postcard.jpg | Greetings from Orlando, Florida, the city beautiful | Boston Public Library, via Flickr/Openverse | CC BY 2.0 |
| assets/florida-oranges-postcard.jpg | Golden Florida oranges | Boston Public Library, via Flickr/Openverse | CC BY 2.0 |
| assets/bogota-hotel-granada-postcard.jpg | Postal Bogotá - Hotel Granada | Tichnor Bros., Inc., via Wikimedia Commons | Domínio público |
| assets/bogota-catedral-postcard.jpg | Postal Bogotá - La Catedral | Tichnor Bros., Inc., via Wikimedia Commons | Domínio público |
| assets/map/*.png | Tiles do mapa (build publicado) | © OpenStreetMap contributors | ODbL |

Links de origem em `assets/credits.json`. Os desenhos (dente, escova, implante, alinhador) são SVG feitos para a página e podem ser trocados por fotos reais.

## Arquivos

- `index.html`, `styles.css`, `main.js`: o site. Uma fonte (Albert Sans, Google Fonts), sem frameworks, sem build.
- `build-artifact.py`: gera `dist/artifact.html` com CSS e JS embutidos e um mapa estático de tiles no lugar do iframe do OpenStreetMap, para publicação onde iframes não são permitidos.
- `assets/`: postais, tiles do mapa e créditos.
