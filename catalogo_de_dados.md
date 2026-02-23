# Documentação dos Dados do YouTube

## Sumário

-   Canais
-   Chats ao vivo
-   Histórico do YouTube
-   Inscrições
-   Metadados de Vídeos
-   Biblioteca de Músicas
-   Playlists

------------------------------------------------------------------------

# Explicação das Colunas dos Arquivos CSV

## canal.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do canal             object (str)            Identificador único do
                                                  canal dentro do
                                                  YouTube.

  Título do canal         object (str)            Nome público do canal.
  (Original)                                      

  Visibilidade do canal   object (str)            Público, privado ou
                                                  restrito.
  -----------------------------------------------------------------------

## configurações da página do canal.csv

  Coluna        Tipo           Explicação
  ------------- -------------- ----------------------
  ID do canal   object (str)   Referência ao canal.

## configurações de moderação da comunidade do canal.csv

  Coluna        Tipo           Explicação
  ------------- -------------- ------------------------------------
  ID do canal   object (str)   Canal ao qual as regras pertencem.

## configurações de URL do canal.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do canal             object (str)            Identificador do canal.

  Nome do URL curto 1 do  object (str)            Nome usado no link
  canal                                           curto.
  -----------------------------------------------------------------------

## dados de recursos do canal.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do canal             object (str)            Identificador do canal.

  Moderação automática do object (str)            Filtros automáticos no
  canal no chat ao vivo                           chat.

  Tipo de comentários     object (str)            Configuração padrão de
  permitidos padrão do                            comentários.
  vídeo                                           

  Público-alvo padrão do  object (str)            Público
  vídeo                                           infantil/adulto.

  Licença padrão do vídeo object (str)            Licença aplicada.

  Latitude do local       int64                   Coordenada geográfica.
  padrão do vídeo                                 

  Longitude do local      int64                   Coordenada geográfica.
  padrão do vídeo                                 
  -----------------------------------------------------------------------

## imagens do canal.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  Criar Carimbo de        object (str)            Momento da atualização
  data/hora                                       da imagem.

  URL de conteúdo         object (str)            Endereço da imagem.
  completo da imagem do                           
  canal                                           
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Chats ao vivo.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do chat ao vivo      object (str)            Identificador da
                                                  mensagem.

  ID do canal             object (str)            Canal da transmissão.

  Marcação de tempo da    object (str)            Data e hora da
  criação do chat ao vivo                         mensagem.

  Preço                   int64                   Super Chat pago ou não.

  ID do vídeo             object (str)            Live associada.

  Texto do chat ao vivo   object (str)            Conteúdo da mensagem.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

#  Histórico do YouTube

## histórico de pesquisa.html

  Coluna   Tipo           Explicação
  -------- -------------- ---------------------
  tipo     object (str)   Tipo de ação.
  titulo   object (str)   Pesquisa realizada.
  url      object (str)   Link relacionado.
  data     object (str)   Data e hora.

## histórico-de-visualização.html

  Coluna   Tipo           Explicação
  -------- -------------- -------------------------
  tipo     object (str)   Tipo de ação.
  titulo   object (str)   Vídeo assistido.
  url      object (str)   Link do vídeo ou canal.
  data     object (str)   Data e hora.

------------------------------------------------------------------------

#  inscrições.csv

  Coluna            Tipo           Explicação
  ----------------- -------------- -----------------
  ID do canal       object (str)   Canal inscrito.
  URL do canal      object (str)   Link do canal.
  Título do canal   object (str)   Nome público.

------------------------------------------------------------------------

#  Metadados dos Vídeos

## gravações de vídeo.csv

  Coluna                           Tipo           Explicação
  -------------------------------- -------------- -------------------------
  ID do vídeo                      object (str)   Identificador do vídeo.
  Altitude de gravação do vídeo    int64          Altitude da gravação.
  Latitude da gravação do vídeo    int64          Latitude.
  Longitude da gravação do vídeo   int64          Longitude.

## textos de vídeo.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do vídeo             object (str)            Identificador.

  Carimbo de data/hora da object (str)            Criação do texto.
  criação do texto do                             
  vídeo                                           

  Segmentos 1 do texto de object (str)            Descrição.
  descrição do vídeo                              

  Segmentos 1 do texto do object (str)            Título.
  título do vídeo                                 

  Carimbo de data/hora da object (str)            Última edição.
  atualização do texto do                         
  vídeo                                           
  -----------------------------------------------------------------------

## vídeos.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do vídeo             object (str)            Identificador.

  Duração aproximada (ms) int64                   Duração.

  Categoria do vídeo      object (str)            Categoria.

  Descrição do vídeo      object (str)            Descrição original.
  (original)                                      

  ID do canal             object (str)            Canal.

  Título do vídeo         object (str)            Título.
  (original)                                      

  Privacidade             object (str)            Público/privado.

  Estado do vídeo         object (str)            Processamento.

  Carimbo de data/hora de object (str)            Upload.
  criação do vídeo                                

  Carimbo de data/hora de object (str)            Publicação.
  publicação do vídeo                             
  -----------------------------------------------------------------------

------------------------------------------------------------------------

#  music library songs.csv

  Coluna             Tipo           Explicação
  ------------------ -------------- -------------------------
  ID do vídeo        object (str)   Música/vídeo.
  Song Title         object (str)   Música.
  Album Title        object (str)   Álbum.
  Artist Name 1-10   object (str)   Artistas participantes.

------------------------------------------------------------------------

#  Playlists

## playlists.csv

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  Código da playlist      object (str)            Identificador.

  Adicionar novos vídeos  object (str)            Ordem automática.
  ao topo                                         

  Título da playlist      object (str)            Nome.
  (original)                                      

  Idioma do título da     object (str)            Idioma.
  playlist (original)                             

  Carimbo de data/hora da object (str)            Criação.
  criação da playlist                             

  Carimbo de data/hora da object (str)            Atualização.
  atualização da playlist                         

  Ordem dos vídeos da     object (str)            Ordem.
  playlist                                        

  Visibilidade da         object (str)            Pública/privada.
  playlist                                        
  -----------------------------------------------------------------------

## Vídeos da playlist

  -----------------------------------------------------------------------
  Coluna                  Tipo                    Explicação
  ----------------------- ----------------------- -----------------------
  ID do vídeo             object (str)            Vídeo.

  Carimbo de data/hora da object (str)            Data de adição.
  criação do vídeo da                             
  playlist                                        
  -----------------------------------------------------------------------
