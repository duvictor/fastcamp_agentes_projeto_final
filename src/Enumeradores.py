"""
responsavel por manter os enumeradores da solução
"""

from enum import Enum


from enum import Enum

class EspecialidadeMedica(Enum):
    ACUPUNTURA = "Acupuntura"
    ALERGIA_E_IMUNOLOGIA = "Alergia e Imunologia"
    ANESTESIOLOGIA = "Anestesiologia"
    ANGIOLOGIA = "Angiologia"
    CARDIOLOGIA = "Cardiologia"
    CARDIOLOGIA_DE_INTERVENCAO = "Cardiologia de Intervenção"
    CIRURGIA_CARDIOVASCULAR = "Cirurgia Cardiovascular"
    CIRURGIA_DA_MAO = "Cirurgia da Mão"
    CIRURGIA_DE_CABECA_E_PESCOCO = "Cirurgia de Cabeça e Pescoço"
    CIRURGIA_DO_APARELHO_DIGESTIVO = "Cirurgia do Aparelho Digestivo"
    CIRURGIA_GERAL = "Cirurgia Geral"
    CIRURGIA_ONCOLOGICA = "Cirurgia Oncológica"
    CIRURGIA_PEDIATRICA = "Cirurgia Pediátrica"
    CIRURGIA_PLASTICA = "Cirurgia Plástica"
    CIRURGIA_TORACICA = "Cirurgia Torácica"
    CIRURGIA_VASCULAR = "Cirurgia Vascular"
    CLINICA_MEDICA = "Clínica Médica"
    COLOPROCTOLOGIA = "Coloproctologia"
    DERMATOLOGIA = "Dermatologia"
    DERMATOPATOLOGIA = "Dermatopatologia"
    ENDOCRINOLOGIA_E_METABOLOGIA = "Endocrinologia e Metabologia"
    ENDOSCOPIA = "Endoscopia"
    GASTROENTEROLOGIA = "Gastroenterologia"
    GENETICA_MEDICA = "Genética Médica"
    GERIATRIA = "Geriatria"
    GINECOLOGIA_E_OBSTETRICIA = "Ginecologia e Obstetrícia"
    HEMATOLOGIA_E_HEMOTERAPIA = "Hematologia e Hemoterapia"
    HOMEOPATIA = "Homeopatia"
    INFECTOLOGIA = "Infectologia"
    MASTOLOGIA = "Mastologia"
    MEDICINA_DE_EMERGENCIA = "Medicina de Emergência"
    MEDICINA_DE_FAMILIA_E_COMUNIDADE = "Medicina de Família e Comunidade"
    MEDICINA_DO_TRABALHO = "Medicina do Trabalho"
    MEDICINA_DO_TRAFEGO = "Medicina do Tráfego"
    MEDICINA_ESPORTIVA = "Medicina Esportiva"
    MEDICINA_FISICA_E_REABILITACAO = "Medicina Física e Reabilitação"
    MEDICINA_INTENSIVA = "Medicina Intensiva"
    MEDICINA_LEGAL_E_PERICIA_MEDICA = "Medicina Legal e Perícia Médica"
    MEDICINA_NUCLEAR = "Medicina Nuclear"
    MEDICINA_PREVENTIVA_E_SOCIAL = "Medicina Preventiva e Social"
    NEFROLOGIA = "Nefrologia"
    NEUROCIRURGIA = "Neurocirurgia"
    NEUROLOGIA = "Neurologia"
    NUTROLOGIA = "Nutrologia"
    OFTALMOLOGIA = "Oftalmologia"
    ONCOLOGIA_CLINICA = "Oncologia Clínica"
    ONCOLOGIA_PEDIATRICA = "Oncologia Pediátrica"
    ORTOPEDIA_E_TRAUMATOLOGIA = "Ortopedia e Traumatologia"
    OTORRINOLARINGOLOGIA = "Otorrinolaringologia"
    PATOLOGIA = "Patologia"
    PATOLOGIA_CLINICA_MEDICINA_LABORATORIAL = "Patologia Clínica/Medicina Laboratorial"
    PEDIATRIA = "Pediatria"
    PNEUMOLOGIA = "Pneumologia"
    PSIQUIATRIA = "Psiquiatria"
    PSIQUIATRIA_FORENSE = "Psiquiatria Forense"
    RADIOLOGIA_E_DIAGNOSTICO_POR_IMAGEM = "Radiologia e Diagnóstico por Imagem"
    RADIOTERAPIA = "Radioterapia"
    REUMATOLOGIA = "Reumatologia"
    UROLOGIA = "Urologia"

# # Exemplo de uso
# print(EspecialidadeMedica.CARDIOLOGIA)
# print(EspecialidadeMedica.CARDIOLOGIA.value)
# print(EspecialidadeMedica['DERMATOLOGIA'])
#
# for especialidade in EspecialidadeMedica:
#     print(especialidade.value)

# Para obter uma lista dos valores (para um prompt de LLM, por exemplo):
lista_especialidades = [especialidade.value for especialidade in EspecialidadeMedica]
print(f"\nLista de especialidades: {lista_especialidades}")



class ModalidadeMedica(Enum):
    RADIOGRAFIA_CONVENCIONAL = "Radiografia convencional (Raio-x)"
    MAMOGRAFIA = "Mamografia"
    DENSITOMETRIA_OSSEA = "Densitometria óssea"
    TOMOGRAFIA_COMPUTADORIZADA = "Tomografia computadorizada"
    RESSONANCIA_MAGNETICA = "Ressonância magnética"
    ULTRASSONOGRAFIA = "Ultrassonografia"
    MEDICINA_NUCLEAR = "Medicina nuclear"
    ANGIOGRAFIA = "Angiografia"
    OUTROS = "Outros"

# Exemplo de uso:
print(ModalidadeMedica.RADIOGRAFIA_CONVENCIONAL)
print(ModalidadeMedica.MAMOGRAFIA.value)

# for modalidade in ModalidadeMedica:
#     print(f"{modalidade.name}: {modalidade.value}")

# Para obter uma lista dos valores (para um prompt de LLM, por exemplo):
lista_modalidades = [modalidade.value for modalidade in ModalidadeMedica]
print(f"\nLista de modalidades: {lista_modalidades}")