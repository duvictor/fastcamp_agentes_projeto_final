"""
responsável por testar o fluxo principal
"""

import src.Util as utils

temp_file = "./temp.pdf"
textUtil = utils.TextUtil()
print(temp_file)

textUtil.process_pdf(temp_file, "arquivo de teste.pdf")