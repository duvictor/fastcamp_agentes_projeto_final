"""
responsavel por manter os enumeradores da solução
Paulo Victor Dos Santos 2025
Universidade Federal de Goiás
"""
from enum import Enum

class EspecialidadeMedica(Enum):
    """
    Enumeration of medical specialties.

    This class defines a set of constants representing various medical specialties.
    It provides an organized way to handle specialty names, mainly as string values.
    Each constant has a descriptive name corresponding to a specific medical field.

    :ivar ACUPUNTURA: Acupuncture specialty.
    :ivar ALERGIA_E_IMUNOLOGIA: Allergy and Immunology specialty.
    :ivar ANESTESIOLOGIA: Anesthesiology specialty.
    :ivar ANGIOLOGIA: Angiology specialty.
    :ivar CARDIOLOGIA: Cardiology specialty.
    :ivar CARDIOLOGIA_DE_INTERVENCAO: Interventional Cardiology specialty.
    :ivar CIRURGIA_CARDIOVASCULAR: Cardiovascular Surgery specialty.
    :ivar CIRURGIA_DA_MAO: Hand Surgery specialty.
    :ivar CIRURGIA_DE_CABECA_E_PESCOCO: Head and Neck Surgery specialty.
    :ivar CIRURGIA_DO_APARELHO_DIGESTIVO: Digestive System Surgery specialty.
    :ivar CIRURGIA_GERAL: General Surgery specialty.
    :ivar CIRURGIA_ONCOLOGICA: Oncology Surgery specialty.
    :ivar CIRURGIA_PEDIATRICA: Pediatric Surgery specialty.
    :ivar CIRURGIA_PLASTICA: Plastic Surgery specialty.
    :ivar CIRURGIA_TORACICA: Thoracic Surgery specialty.
    :ivar CIRURGIA_VASCULAR: Vascular Surgery specialty.
    :ivar CLINICA_MEDICA: General Medicine specialty.
    :ivar COLOPROCTOLOGIA: Coloproctology specialty.
    :ivar DERMATOLOGIA: Dermatology specialty.
    :ivar DERMATOPATOLOGIA: Dermatopathology specialty.
    :ivar ENDOCRINOLOGIA_E_METABOLOGIA: Endocrinology and Metabolism specialty.
    :ivar ENDOSCOPIA: Endoscopy specialty.
    :ivar GASTROENTEROLOGIA: Gastroenterology specialty.
    :ivar GENETICA_MEDICA: Medical Genetics specialty.
    :ivar GERIATRIA: Geriatrics specialty.
    :ivar GINECOLOGIA_E_OBSTETRICIA: Gynecology and Obstetrics specialty.
    :ivar HEMATOLOGIA_E_HEMOTERAPIA: Hematology and Hemotherapy specialty.
    :ivar HOMEOPATIA: Homeopathy specialty.
    :ivar INFECTOLOGIA: Infectious Disease specialty.
    :ivar MASTOLOGIA: Mastology specialty.
    :ivar MEDICINA_DE_EMERGENCIA: Emergency Medicine specialty.
    :ivar MEDICINA_DE_FAMILIA_E_COMUNIDADE: Family and Community Medicine specialty.
    :ivar MEDICINA_DO_TRABALHO: Occupational Medicine specialty.
    :ivar MEDICINA_DO_TRAFEGO: Traffic Medicine specialty.
    :ivar MEDICINA_ESPORTIVA: Sports Medicine specialty.
    :ivar MEDICINA_FISICA_E_REABILITACAO: Physical Medicine and Rehabilitation specialty.
    :ivar MEDICINA_INTENSIVA: Intensive Care Medicine specialty.
    :ivar MEDICINA_LEGAL_E_PERICIA_MEDICA: Legal Medicine and Medical Expertise specialty.
    :ivar MEDICINA_NUCLEAR: Nuclear Medicine specialty.
    :ivar MEDICINA_PREVENTIVA_E_SOCIAL: Preventive and Social Medicine specialty.
    :ivar NEFROLOGIA: Nephrology specialty.
    :ivar NEUROCIRURGIA: Neurosurgery specialty.
    :ivar NEUROLOGIA: Neurology specialty.
    :ivar NUTROLOGIA: Nutrition specialty.
    :ivar OFTALMOLOGIA: Ophthalmology specialty.
    :ivar ONCOLOGIA_CLINICA: Clinical Oncology specialty.
    :ivar ONCOLOGIA_PEDIATRICA: Pediatric Oncology specialty.
    :ivar ORTOPEDIA_E_TRAUMATOLOGIA: Orthopedics and Traumatology specialty.
    :ivar OTORRINOLARINGOLOGIA: Otorhinolaryngology specialty.
    :ivar PATOLOGIA: Pathology specialty.
    :ivar PATOLOGIA_CLINICA_MEDICINA_LABORATORIAL: Clinical Pathology/Laboratory Medicine specialty.
    :ivar PEDIATRIA: Pediatrics specialty.
    :ivar PNEUMOLOGIA: Pulmonology specialty.
    :ivar PSIQUIATRIA: Psychiatry specialty.
    :ivar PSIQUIATRIA_FORENSE: Forensic Psychiatry specialty.
    :ivar RADIOLOGIA_E_DIAGNOSTICO_POR_IMAGEM: Radiology and Image Diagnostics specialty.
    :ivar RADIOTERAPIA: Radiotherapy specialty.
    :ivar REUMATOLOGIA: Rheumatology specialty.
    :ivar UROLOGIA: Urology specialty.
    """
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
    """
    This class represents an enumeration of different medical imaging modalities.

    It provides predefined constant values for various types of imaging techniques
    used in the medical field. Each constant is paired with a string description
    of the modality it represents.

    :ivar RADIOGRAFIA_CONVENCIONAL: Describes the use of conventional radiography,
        commonly referred to as X-rays.
    :type RADIOGRAFIA_CONVENCIONAL: str
    :ivar MAMOGRAFIA: Describes mammography, an imaging modality specializing in
        the examination of breast tissues.
    :type MAMOGRAFIA: str
    :ivar DENSITOMETRIA_OSSEA: Represents bone densitometry, also known as DXA,
        used for measuring bone mineral density.
    :type DENSITOMETRIA_OSSEA: str
    :ivar TOMOGRAFIA_COMPUTADORIZADA: Describes computed tomography (CT), a method
        that provides cross-sectional imaging.
    :type TOMOGRAFIA_COMPUTADORIZADA: str
    :ivar RESSONANCIA_MAGNETICA: Refers to magnetic resonance imaging (MRI),
        which uses magnetic fields and radio waves to generate detailed images.
    :type RESSONANCIA_MAGNETICA: str
    :ivar ULTRASSONOGRAFIA: Describes ultrasonography, which uses high-frequency
        sound waves to create images of internal body structures.
    :type ULTRASSONOGRAFIA: str
    :ivar MEDICINA_NUCLEAR: Represents nuclear medicine, which involves the use of
        small amounts of radioactive material to diagnose or treat diseases.
    :type MEDICINA_NUCLEAR: str
    :ivar ANGIOGRAFIA: Refers to angiography, a technique for visualizing the inside
        of blood vessels and organs.
    :type ANGIOGRAFIA: str
    :ivar OUTROS: Represents other imaging modalities not categorized in the
        predefined constants.
    :type OUTROS: str
    """
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