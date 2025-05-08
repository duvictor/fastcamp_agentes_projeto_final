"""
classe responsável por manter os agentes
Paulo Victor Dos Santos 2025
Universidade Federal de Goiás
"""

from crewai import Crew, Process, Agent, Task, LLM
from crewai_tools import QdrantVectorSearchTool
from sentence_transformers import SentenceTransformer
from data.Protocolo import LaudoPDF
import uuid

from src.Enumeradores import EspecialidadeMedica, ModalidadeMedica
from src.QdrantConection import upsert_to_qdrant
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


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
        # Initialize the tool
        # self.qdrant_tool = QdrantVectorSearchTool(
        #     qdrant_url="your_qdrant_url",
        #     qdrant_api_key="your_qdrant_api_key",
        #     collection_name="your_collection"
        # )
        # # Create an agent that uses the tool
        # self.agentPdfRetriever = Agent(
        #     role="Research Assistant",
        #     goal="Find relevant information in documents",
        #     backstory="""Você está trabalhando em um sistema médico que busca laudos a partir da especialidade e da modalidade.""",
        #     tools=[self.qdrant_tool]
        # )
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
                            " O retorno deve ser apenas a modalidade, como por exemplo: Mamografia",
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




    def processar_laudo(self, laudoPdf: LaudoPDF):
        """
        Processes a given medical report (laudo) using CrewAI workflows by leveraging agents and tasks
        configured for extracting specific medical specialties, modalities, and summarizing the report
        content. The method sequentially executes the workflows and returns raw results of all executed
        tasks.

        :param laudoPdf: The medical report in PDF format that needs to be processed. It contains the text
            which will be analyzed through different task chains managed by CrewAI workflows.
        :type laudoPdf: LaudoPDF
        :return: A tuple consisting of raw results from the workflows, which includes extracted medical
            specialties, identified modalities, and a summarized version of the report.
        :rtype: tuple
        """
        # Run CrewAI workflow
        crew_especialidade = Crew(
            agents=[self.agentEspecialidade],
            tasks=[self.tarefaEspecialidade],
            process=Process.sequential,
            verbose=True
        )

        crew_modalidade = Crew(
            agents=[self.agentModalidade],
            tasks=[self.tarefaModalidade],
            process=Process.sequential,
            verbose=True
        )

        crew_summarizer = Crew(
            agents=[self.agentSummarizer],
            tasks=[self.tarefaSummarizer],
            process=Process.sequential,
            verbose=True
        )


        lista_especialidades = [especialidade.value for especialidade in EspecialidadeMedica]
        lista_modalidades = [modalidade.value for modalidade in ModalidadeMedica]


        result_especialidade = crew_especialidade.kickoff(
            inputs={"laudo": laudoPdf.texto, "lista_especialidades": lista_especialidades}
        )
        print(result_especialidade)


        result_modalidade = crew_modalidade.kickoff(
            inputs={"laudo": laudoPdf.texto,
                    "lista_modalidades": lista_modalidades}
        )
        print(result_modalidade)


        result_summarizer = crew_summarizer.kickoff(
            inputs={"laudo": laudoPdf.texto}
        )
        print(result_summarizer)

        return result_especialidade.raw, result_modalidade.raw, result_summarizer.raw





