# O que fazer?

Abaixo as tarefas a serem consideradas no projeto final do curso de agentes inteligentes.


 01/05/2025


[ ] validação de dados Pydantic = ok

[ ] Orquestração de multiagente

[ ] interface com usuário, streamlit = ok

[ ] comunicação com whatsapp via langflow

[ ] embeddings = ok

[ ] fluxos de trabalho com langflow

[ ] relatório e código


#### ETAPAS DO PROJETO

[ ] problema na área da saúde.

[ ] uma seção no relatório descrevendo o problema.

[ ] definir o agente, único ou multiagente

[ ] uma seção no relatório detalhando a arquitetura do mvp, diagrama e explicação do agente

[ ] identificar os dados de entrada e implementar modelo pydantic

[ ] código python demonstrando os modelos pydantic, referenciar o código no relatório

[ ] criar fluxo no langflow que represente a lógica principal do agente

[ ] entregar arquivo langflow e colocar na seção do relatório

[ ] utilizar embeedings, exemplo, na classificação ou na busca

[ ] código python e seção no relatório

[ ] Orquestração de multiagente

[ ] seção e código

[ ] Interface com usuário utilizando streamlit

[ ] código e seção no relatório

[ ] comunicar com whatsapp 

[ ] código e seção no relatório

[ ] readme.md detalhadado
** descrição
** tecnologias usadas
** instrução de instalação
** instruçoes como executar
** capturas de tela

















O desafio é construir um agente inteligente que possa classificar mensagens de entrada, 
definir rotas e comportamentos com base em embeddings e similaridade, 
e realizar a sumarização de informações específicas contidas em um PDF, 
utilizando RAG (Retrieval-Augmented Generation) para focar o modelo nas informações relevantes.


#### 1 [ ] Classificação de mensagens de entrada.




1.1 [ ] Implementar um modelo de classificação simples para filtrar mensagens de entrada.

1.2 [ ] Utilizar técnicas de prompt para melhorar a eficácia do modelo de classificação.

#### 2 [ ] Definição de Rotas e Comportamentos

2.1 [ ] Utilizar Embeddings e técnicas de similaridade para definir rotas e comportamentos do agente com base nas mensagens classificadas

2.2 [ ] Usar sentence-transformers ou qualquer outra biblioteca de embeddings

#### 3 [ ] Sumarização 
3.1 [ ] implementar código para sumarizar informações utilizando prompt para melhorar resultados.

3.2 [ ] Utilizar RAG para garantir que o modelo se concentre apenas nas informações contidas em um PDF específico

3.3 [ ] pmupdf para leitura de pdf e transformes da Hugging Face para Rag e sumarização




## Roteiro

* criar um front usando streamlit 
* fazer upload de pdf, gerar chunks, gerar embeddings, salvar num banco de dados
* Classificar as mensagens de entrada do usuário através de um agente
* Criar rotas (flow) usando o crewai, as rotas e comportamentos devem ser com base em embedding e similaridade
     Exemplo,    tal similaridade é parecido com tal coisa, vai pra rota tal
                tal similaridade é parecido com outra coisa, vai pra outra rota
* Realizar a sumarização de informações específica do PDF utilizando RAG.



O front deverá ter um upload de pdf, um aba para mostrar as palavras chaves e a sumarização
o front deverá ter um chat para o usuário interagir com o pdf (embeddings)
as mensagens do usuário deverão ser classificadas e exibidas em uma outra aba
Os PDF devem ser classificados e exibidos no formato de árvore.
    Os Pdf deverão ser classificados em especialidade e modalidade
    Haverá fluxo para modalidade e fluxo para especialidade



A pergunta é sobre a especialidade?
A pergunta é sobre a modalidade?
A pergunta é genérica?



# Qdrant

!docker run -d -p "6333:6333" -p "6334:6334" --name "reverse_image_search" qdrant/qdrant:v1.10.1



# Referencias

https://levelup.gitconnected.com/building-a-rag-application-using-streamlit-langchain-and-deepseek-r1-7e7225e598ae
https://medium.com/@habbema/estruturando-projetos-em-python-692502641c05
https://eskelsen.medium.com/estruturando-projetos-em-python-um-modelo-de-sistema-d0652d289bc
https://medium.com/@vikrambhat2/agentic-rag-mastering-document-retrieval-with-crewai-deepseek-and-streamlit-21cb3886bbbf
https://ai.gopubby.com/multi-agent-system-for-research-summarization-and-reporting-with-crew-ai-c5e41a712c25
https://www.datacamp.com/tutorial/agentic-rag-tutorial
https://medium.com/the-ai-forum/build-a-local-reliable-rag-agent-using-crewai-and-groq-013e5d557bcd
https://github.com/benitomartin/crewai-rag-langchain-qdrant
https://medium.aiplanet.com/retrieval-augmented-generation-using-qdrant-huggingface-embeddings-and-langchain-and-evaluate-the-3c7e3b1e4976
https://medium.com/@erickcalderin/classic-rag-with-huggingface-qdrant-and-streamlit-4a0918b20fa7
https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/
https://qdrant.tech/documentation/agentic-rag-crewai-zoom/
https://github.com/qdrant/examples/blob/master/rag-with-qdrant-deepseek/deepseek-qdrant.ipynb
https://qdrant.tech/documentation/agentic-rag-crewai-zoom/
https://docs.crewai.com/tools/qdrantvectorsearchtool
https://huggingface.co/blog/Andyrasika/qdrant-transformers



correções para debugar streamlit no pycharm

https://discuss.streamlit.io/t/cannot-debug-streamlit-in-pycharm-2023-3-3/61581
https://python.langchain.com/docs/integrations/vectorstores/qdrant/
https://qdrant.tech/documentation/data-ingestion-beginners/#:~:text=To%20start%20visualizing%20your%20data,and%20select%20Access%20the%20database.&text=The%20first%20query%20retrieves%20all,third%20performs%20a%20sample%20query.
https://docs.crewai.com/tools/qdrantvectorsearchtool



