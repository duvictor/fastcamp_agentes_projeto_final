"""
classe responsável por manter os agentes
Paulo Victor Dos Santos 2025
Universidade Federal de Goiás
"""

from crewai import Crew, Process, Agent, Task, LLM
from src.qdrant_search_tool_custom import QdrantVectorSearchToolCustom
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from data.Protocolo import LaudoPDF
import uuid

from src.Enumeradores import EspecialidadeMedica, ModalidadeMedica
from src.QdrantConection import upsert_to_qdrant
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModel
from src.QdrantConection import get_cliente

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
COLLECTION_NAME = os.environ["COLLECTION_NAME"]
PATH_QDRANT = os.environ["PATH_QDRANT"]


class AgenteRetriever:
    def __init__(self):
        self.llm_OpenAI = ChatOpenAI()
        self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
        self.model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

        self.qdrant_tool = QdrantVectorSearchToolCustom(
            client=get_cliente(),
            collection_name=COLLECTION_NAME,
            limit=3,
            score_threshold=0.35,
            query_filter=None,
            custom_embedding_fn=self.custom_embeddings  # Pass your custom function
        )


        # Create an agent that uses the tool
        self.agentPdfRetriever = Agent(
            role="Médico pesquisador",
            goal="Encontrar informações relevantes em laudos médicos",
            backstory="""Você está trabalhando em um sistema médico que busca laudos a partir da especialidade, da modalidade e do resumo (sumarização).""",
            tools=[self.qdrant_tool]
        )
        # Define tasks
        self.search_task = Task(
            description="""Encontre laudos relevantes similares ao texto a seguir: {query}.""",
            expected_output="""Sua saída final deverá ser em português e deverá incluir:
            - A informação relevante encontrada
            - O score da similaridade dos resultados
            - O metadado do laudo encontrado""",
            agent=self.agentPdfRetriever
        )


    def retriever_query(self, query) -> str:
        # Run CrewAI workflow
        crew = Crew(
            agents=[self.agentPdfRetriever],
            tasks=[self.search_task],
            process=Process.sequential,
            memory=True,
            verbose=True
        )

        result = crew.kickoff(
            inputs={"query": query}
        )
        print(result)

        return result.raw


    def custom_embeddings(self, text: str) -> list[float]:
        # Tokenize and get model outputs
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)

        # Use mean pooling to get text embedding
        embeddings = outputs.last_hidden_state.mean(dim=1)

        # Convert to list of floats and return
        return embeddings[0].tolist()





class AgenteLaudoMedico:
    def __init__(self):
        """
        This script initializes various components for a medical document processing system. It employs
        AI agents with specific roles to analyze medical reports, suggest medical specialties, classify
        modalities, and summarize reports. The agents and tasks are designed to handle specific objectives,
        leveraging the capabilities of a language model and integrating tools for vector search and retrieval.

        Attributes
        ----------
        llm_OpenAI : ChatOpenAI
            The language model used for all AI agents. This serves as the backbone for natural language
            understanding and synthesis.
        agentEspecialidade : Agent
            Medical specialist agent designed to classify and suggest the medical specialty of a given report.
            It includes a defined role, goal, and backstory to tailor its reasoning capabilities.
        tarefaEspecialidade : Task
            Task assigned to the `agentEspecialidade` for identifying the medical specialty in a document.
            The task provides a detailed description and expected output.
        agentModalidade : Agent
            Radiologist agent to classify and suggest the medical modality in a given report. Like other
            agents, it includes specific contextual understanding based on its role.
        tarefaModalidade : Task
            Task assigned to the `agentModalidade` for determining the modality type in a document. This task
            has a defined objective and expected output.
        agentSummarizer : Agent
            Generalist agent responsible for summarizing medical reports into concise and user-friendly text.
            The agent's capabilities are modeled on a generalist physician's expertise.
        tarefaSummarizer : Task
            Task for the `agentSummarizer` to condense medical reports into understandable summaries in
            Portuguese. The task emphasizes the ease of understanding for non-medical users.
        """
        self.llm_OpenAI = ChatOpenAI()

        # Create an agent that uses the tool
        self.agentEspecialidade = Agent(
            role="Médico especialista",
            goal="Com base no contexto, sugerir a especialidade médica do laudo: {laudo} ",
            backstory="Você é um médico com experiência em laudos e consegue classificar a especialidade médica do laudo com base na seguinte lista: {lista_especialidades}",
            llm=self.llm_OpenAI
        )
        self.tarefaEspecialidade = Task(description="Entender o laudo médico e sugerir a especialidade do laudo: {laudo}",
                                        expected_output="Retorne uma das seguintes especialidades médicas da lista a seguir: "
                                                        " <especialidades> "
                                                        " {lista_especialidades} "
                                                        " </especialidades> "
                                                        " O retorno deve ser apenas a especialidade, como por exemplo: Angiologia",
                                        agent=self.agentEspecialidade
                                        )

        self.agentModalidade = Agent(
            role="Médico radiologista",
            goal="Com base no contexto, sugerir a modalidade médica do laudo em português",
            backstory="Você é um médico radiologista com experiência em laudar exames de imagens e consegue classificar a modalidade médica presente no laudo",
            llm=self.llm_OpenAI
        )
        self.tarefaModalidade = Task(
            description="Entender o laudo médico e sugerir a modalidade médica do laudo: {laudo}",
            expected_output="Retorne uma das seguintes modalidades médicas da lista a seguir: "
                            " <modalidades> "
                            " {lista_modalidades} "
                            " </modalidades> "
                            " O retorno deve ser apenas a modalidade, como por exemplo: Mamografia."
                            " Caso não haja nenhuma modalidade para o laudo, retorne: Outros. ",
            agent=self.agentModalidade
            )

        self.agentSummarizer = Agent(
            role="Médico Generalista",
            goal="Com base no contexto, resumir o laudo médico em português",
            backstory="Você é um médico Generalista com experiência em laudos",
            llm=self.llm_OpenAI
        )
        self.tarefaSummarizer = Task(
            description="Entender o laudo médico e resumi-lo. Aqui está o laudo a ser resumido: {laudo}",
            expected_output="Retorne um resumo do laudo médico a seguir em até 50 palavras em português. "
                            "O laudo deve ser de fácil entendimento para pessoas que não são da área médica. Aqui está o laudo: {laudo} ",
            agent=self.agentSummarizer
        )




    def processar_laudo(self, textos: str):
        """
        Processes a medical report using multiple workflows to determine medical specialty,
        modality, and to summarize the report text.

        The function executes three sequential CrewAI workflows: one for identifying the
        medical specialty, another for determining the modality of the medical procedure,
        and a final one for summarizing the content of the medical report. It utilizes
        specified agents and tasks defined within the CrewAI platform to achieve these goals.

        The outputs from all three workflows are collected and returned as raw results.

        :param textos: The content of the medical report in text format to be processed.
        :type textos: str
        :return:
            A tuple containing the raw results of the following workflows:
            - Medical specialty identification.
            - Medical modality classification.
            - Medical report summarization.
        :rtype: tuple
        """
        # Run CrewAI workflow
        crew_especialidade = Crew(
            agents=[self.agentEspecialidade],
            tasks=[self.tarefaEspecialidade],
            process=Process.sequential,
            memory=True,
            verbose=True
        )

        crew_modalidade = Crew(
            agents=[self.agentModalidade],
            tasks=[self.tarefaModalidade],
            process=Process.sequential,
            memory=True,
            verbose=True
        )

        crew_summarizer = Crew(
            agents=[self.agentSummarizer],
            tasks=[self.tarefaSummarizer],
            process=Process.sequential,
            memory=True,
            verbose=True
        )


        lista_especialidades = [especialidade.value for especialidade in EspecialidadeMedica]
        lista_modalidades = [modalidade.value for modalidade in ModalidadeMedica]


        result_especialidade = crew_especialidade.kickoff(
            inputs={"laudo": textos, "lista_especialidades": lista_especialidades}
        )
        print(result_especialidade)


        result_modalidade = crew_modalidade.kickoff(
            inputs={"laudo": textos,
                    "lista_modalidades": lista_modalidades}
        )
        print(result_modalidade)


        result_summarizer = crew_summarizer.kickoff(
            inputs={"laudo": textos}
        )
        print(result_summarizer)

        return result_especialidade.raw, result_modalidade.raw, result_summarizer.raw





