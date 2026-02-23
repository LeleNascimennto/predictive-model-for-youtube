#  Documentação dos Dados do YouTube

## Sumário
- Canais
- Chats ao vivo
- Histórico do YouTube
- Inscrições
- Metadados de Vídeos
- Biblioteca de Músicas
- Playlists

---

#  Explicação das Colunas dos Arquivos CSV

## canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Identificador único do canal dentro do YouTube. |
| Título do canal (Original) | object (str) | Nome público do canal. |
| Visibilidade do canal | object (str) | Público, privado ou restrito. |

## configurações da página do canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Referência ao canal. |

## configurações de moderação da comunidade do canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Canal ao qual as regras pertencem. |

## configurações de URL do canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Identificador do canal. |
| Nome do URL curto 1 do canal | object (str) | Nome usado no link curto. |

## dados de recursos do canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Identificador do canal. |
| Moderação automática do canal no chat ao vivo | object (str) | Filtros automáticos no chat. |
| Tipo de comentários permitidos padrão do vídeo | object (str) | Configuração padrão de comentários. |
| Público-alvo padrão do vídeo | object (str) | Público infantil/adulto. |
| Licença padrão do vídeo | object (str) | Licença aplicada. |
| Latitude do local padrão do vídeo | int64 | Coordenada geográfica. |
| Longitude do local padrão do vídeo | int64 | Coordenada geográfica. |

## imagens do canal.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| Criar Carimbo de data/hora | object (str) | Momento da atualização da imagem. |
| URL de conteúdo completo da imagem do canal | object (str) | Endereço da imagem. |

---

#  Chats ao vivo.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do chat ao vivo | object (str) | Identificador da mensagem. |
| ID do canal | object (str) | Canal da transmissão. |
| Marcação de tempo da criação do chat ao vivo | object (str) | Data e hora da mensagem. |
| Preço | int64 | Super Chat pago ou não. |
| ID do vídeo | object (str) | Live associada. |
| Texto do chat ao vivo | object (str) | Conteúdo da mensagem. |

---

#  Histórico do YouTube

## histórico de pesquisa.html
| Coluna | Tipo | Explicação |
|---|---|---|
| tipo | object (str) | Tipo de ação. |
| titulo | object (str) | Pesquisa realizada. |
| url | object (str) | Link relacionado. |
| data | object (str) | Data e hora. |

## histórico-de-visualização.html
| Coluna | Tipo | Explicação |
|---|---|---|
| tipo | object (str) | Tipo de ação. |
| titulo | object (str) | Vídeo assistido. |
| url | object (str) | Link do vídeo ou canal. |
| data | object (str) | Data e hora. |

---

#  inscrições.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do canal | object (str) | Canal inscrito. |
| URL do canal | object (str) | Link do canal. |
| Título do canal | object (str) | Nome público. |

---

#  Metadados dos Vídeos

## gravações de vídeo.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do vídeo | object (str) | Identificador do vídeo. |
| Altitude de gravação do vídeo | int64 | Altitude da gravação. |
| Latitude da gravação do vídeo | int64 | Latitude. |
| Longitude da gravação do vídeo | int64 | Longitude. |

## textos de vídeo.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do vídeo | object (str) | Identificador. |
| Carimbo de data/hora da criação do texto do vídeo | object (str) | Criação do texto. |
| Segmentos 1 do texto de descrição do vídeo | object (str) | Descrição. |
| Segmentos 1 do texto do título do vídeo | object (str) | Título. |
| Carimbo de data/hora da atualização do texto do vídeo | object (str) | Última edição. |

## vídeos.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do vídeo | object (str) | Identificador. |
| Duração aproximada (ms) | int64 | Duração. |
| Categoria do vídeo | object (str) | Categoria. |
| Descrição do vídeo (original) | object (str) | Descrição original. |
| ID do canal | object (str) | Canal. |
| Título do vídeo (original) | object (str) | Título. |
| Privacidade | object (str) | Público/privado. |
| Estado do vídeo | object (str) | Processamento. |
| Carimbo de data/hora de criação do vídeo | object (str) | Upload. |
| Carimbo de data/hora de publicação do vídeo | object (str) | Publicação. |

---

#  music library songs.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do vídeo | object (str) | Música/vídeo. |
| Song Title | object (str) | Música. |
| Album Title | object (str) | Álbum. |
| Artist Name 1-10 | object (str) | Artistas participantes. |

---

#  Playlists

## playlists.csv
| Coluna | Tipo | Explicação |
|---|---|---|
| Código da playlist | object (str) | Identificador. |
| Adicionar novos vídeos ao topo | object (str) | Ordem automática. |
| Título da playlist (original) | object (str) | Nome. |
| Idioma do título da playlist (original) | object (str) | Idioma. |
| Carimbo de data/hora da criação da playlist | object (str) | Criação. |
| Carimbo de data/hora da atualização da playlist | object (str) | Atualização. |
| Ordem dos vídeos da playlist | object (str) | Ordem. |
| Visibilidade da playlist | object (str) | Pública/privada. |

## Vídeos da playlist
| Coluna | Tipo | Explicação |
|---|---|---|
| ID do vídeo | object (str) | Vídeo. |
| Carimbo de data/hora da criação do vídeo da playlist | object (str) | Data de adição. |
"""

out = "/mnt/data/youtube_documentacao.md"
pypandoc.convert_text(md_text, 'md', format='md', outputfile=out, extra_args=['--standalone'])
out
