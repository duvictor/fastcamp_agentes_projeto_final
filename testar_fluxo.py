"""
responsável por testar o fluxo principal
"""

import src.Util as utils
import src.Agentes as agents

# temp_file = "./temp.pdf"
# textUtil = utils.TextUtil()
# print(temp_file)

# textUtil.process_pdf(temp_file, "arquivo de teste.pdf")
retriever = agents.AgenteRetriever()
resultado = retriever.retriever_query("O que é imagem hipoecogênica?")
print(resultado)

