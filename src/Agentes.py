"""
classe responsável por manter os agentes
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





    def processar_laudo(self, laudoPdf: LaudoPDF):
        """
        responsavel por fazer o processamento do laudo, anotar a modalidade e a especialidade médica
        :param laudoPdf:
        :return:
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


        return result_especialidade.raw, result_modalidade.raw





