# Explicação das Colunas dos Arquivos do YouTube (CSV e HTML)

Este documento descreve, de forma estruturada, as colunas presentes nos arquivos exportados pelo YouTube, explicando o que cada dado representa e como eles se relacionam.

---

## `canal.csv`

| Coluna | Explicação |
|---|---|
| ID do canal | Identificador único do canal dentro do YouTube. Funciona como chave de ligação entre todos os outros arquivos. |
| Título do canal (Original) | Nome oficial exibido publicamente no canal. |
| Visibilidade do canal | Define se o canal está público, privado ou restrito. |

---

## `configurações da página do canal.csv`

| Coluna | Explicação |
|---|---|
| ID do canal | Referência ao canal ao qual as configurações da página principal pertencem. |

---

## `configurações de moderação da comunidade do canal.csv`

| Coluna | Explicação |
|---|---|
| ID do canal | Identifica qual canal possui as regras de moderação da comunidade (comentários, chat e interações). |

---

## `configurações de URL do canal.csv`

| Coluna | Explicação |
|---|---|
| ID do canal | Identificador do canal. |
| Nome do URL curto 1 do canal | Nome personalizado usado para gerar o link curto do canal (ex: `youtube.com/@nome`). |

---

## `dados de recursos do canal.csv`

| Coluna | Explicação |
|---|---|
| ID do canal | Identificador do canal. |
| Moderação automática do canal no chat ao vivo | Indica se o YouTube aplica filtros automáticos no chat de transmissões ao vivo. |
| Tipo de comentários permitidos padrão do vídeo | Configuração padrão de comentários aplicada aos vídeos. |
| Público-alvo padrão do vídeo | Define se o conteúdo é voltado para crianças, adultos ou não definido. |
| Licença padrão do vídeo | Tipo de licença aplicada automaticamente aos vídeos publicados. |
| Latitude do local padrão do vídeo | Coordenada geográfica padrão associada aos vídeos. |
| Longitude do local padrão do vídeo | Coordenada geográfica padrão associada aos vídeos. |

---

## `imagens do canal.csv`

| Coluna | Explicação |
|---|---|
| Criar carimbo de data/hora | Momento exato em que a imagem do canal foi registrada ou atualizada na plataforma. |
| URL de conteúdo completo da imagem do canal | Endereço onde a imagem de perfil do canal está armazenada nos servidores do YouTube. |

---

# `Chats ao vivo.csv` — Explicação das Colunas

| Coluna | Explicação |
|---|---|
| ID do chat ao vivo | Identificador único de cada mensagem enviada no chat durante a live. |
| ID do canal | Identifica qual canal estava realizando a transmissão ao vivo. |
| Marcação de tempo da criação do chat ao vivo | Data e hora exata (timestamp) em que a mensagem foi enviada no chat. |
| Preço | Indica se a mensagem foi enviada como Super Chat (pago). Valor 0 significa que não houve pagamento. |
| ID do vídeo | Identificador do vídeo (live) onde o chat ocorreu. |
| Texto do chat ao vivo | Conteúdo textual da mensagem enviado no chat, armazenado em formato estruturado (JSON). |

---

# Histórico do YouTube — Arquivos HTML

## `histórico de pesquisa.html`

| Coluna | Explicação |
|---|---|
| tipo | Indica o tipo de ação realizada (ex: pesquisa feita na barra do YouTube). |
| titulo | Texto pesquisado pelo usuário. |
| url | Link relacionado ao resultado da pesquisa. |
| data | Data e hora exata em que a pesquisa foi realizada. |

---

## `histórico-de-visualização.html`

| Coluna | Explicação |
|---|---|
| tipo | Tipo de ação registrada (visualização de vídeo). |
| titulo | Título do vídeo assistido. |
| url | Link do canal ou do vídeo assistido. |
| data | Data e hora exata da visualização, incluindo o fuso horário. |

---

# `inscrições.csv` — Explicação das Colunas

| Coluna | Explicação |
|---|---|
| ID do canal | Identificador único do canal no YouTube. |
| URL do canal | Endereço direto para a página do canal. |
| Título do canal | Nome público do canal no qual o usuário está inscrito. |

---

# Metadados dos Vídeos — Arquivos CSV

## `gravações de vídeo.csv`

| Coluna | Explicação |
|---|---|
| ID do vídeo | Identificador único do vídeo. |
| Altitude de gravação do vídeo | Altitude geográfica associada ao local de gravação. |
| Latitude da gravação do vídeo | Coordenada de latitude do local de gravação. |
| Longitude da gravação do vídeo | Coordenada de longitude do local de gravação. |

---

## `textos de vídeo.csv`

| Coluna | Explicação |
|---|---|
| ID do vídeo | Identificador único do vídeo. |
| Carimbo de data/hora da criação do texto do vídeo | Momento de criação do título e descrição. |
| Segmentos 1 do texto de descrição do vídeo | Conteúdo textual da descrição. |
| Segmentos 1 do texto do título do vídeo | Conteúdo textual do título. |
| Carimbo de data/hora da atualização do texto do vídeo | Momento da última alteração. |

---

## `vídeos.csv`

| Coluna | Explicação |
|---|---|
| ID do vídeo | Identificador único do vídeo. |
| Duração aproximada (ms) | Tempo total do vídeo em milissegundos. |
| Categoria do vídeo | Categoria definida pelo YouTube. |
| Descrição do vídeo (original) | Texto original da descrição. |
| ID do canal | Identificador do canal que publicou o vídeo. |
| Título do vídeo (original) | Título original do vídeo. |
| Privacidade | Público, privado ou não listado. |
| Estado do vídeo | Situação do processamento do vídeo. |
| Carimbo de data/hora de criação do vídeo | Momento exato do upload. |
| Carimbo de data/hora de publicação | Momento em que o vídeo se tornou público. |

---

# `music library songs.csv`

| Coluna | Explicação |
|---|---|
| ID do vídeo | Identificador único da música/vídeo. |
| Song Title | Nome da música. |
| Album Title | Nome do álbum. |
| Artist Name 1–10 | Artistas participantes da música. |

---

# Playlists — Estrutura e Vídeos

## `playlists.csv`

| Coluna | Explicação |
|---|---|
| Código da playlist | Identificador único da playlist. |
| Adicionar novos vídeos ao topo | Define a posição automática de novos vídeos. |
| Título da playlist (original) | Nome criado pelo usuário. |
| Idioma do título da playlist (original) | Idioma do título. |
| Carimbo de data/hora da criação da playlist | Momento de criação. |
| Carimbo de data/hora da atualização da playlist | Última modificação. |
| Ordem dos vídeos da playlist | Manual ou automática. |
| Visibilidade da playlist | Pública, privada ou não listada. |

---

## `Vídeos da playlist <nome>.csv`

| Coluna | Explicação |
|---|---|
| ID do vídeo | Identificador do vídeo adicionado à playlist. |
| Carimbo de data/hora da criação do vídeo da playlist | Momento em que o vídeo foi adicionado. |