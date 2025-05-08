"""
responsavel por permitir a interação com o Qdrant
Paulo Victor Dos Santos 2025
Universidade Federal de Goiás
"""
from qdrant_client import QdrantClient, models
import os
from dotenv import load_dotenv
# from qdrant_client.http import models as rest
from qdrant_client.models import PointStruct, Distance, VectorParams


# from src.modelo.Protocolo import ProtocoloImagem

# Load environment variables from the .env file
load_dotenv()

COLLECTION_NAME = os.environ["COLLECTION_NAME"]
PATH_QDRANT = os.environ["PATH_QDRANT"]


try:
    client = QdrantClient(path=PATH_QDRANT)
    collections = client.get_collections()
except Exception:
    # Docker is unavailable in Google Colab so we switch to local
    # mode available in Python SDK
    client = QdrantClient(":memory:")
    collections = client.get_collections()

print(collections)


# try:
#     client.recreate_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=rest.VectorParams(
#             size=512,
#             distance=rest.Distance.COSINE,
#         )
#     )
# except Exception as e:
#     print(e)

# try:
#     client.delete_collection(collection_name=COLLECTION_NAME)
# except Exception as e:
#     print(f"Error during delete collection: {e}")

try:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        on_disk_payload=True,  # store the payload on disk
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )
except Exception as e:
    print(f"Error during create collection: {e}")


def get_cliente() -> QdrantClient:
    """
    Provides a function to initialize and return an instance of QdrantClient.

    This function is responsible for creating and returning a unique QdrantClient object,
    which is commonly used to interact with a Qdrant database.

    :return: An instance of QdrantClient initialized and ready to use.
    :rtype: QdrantClient
    """
    return client

def get_count(chave):
    """
    This function calculates the count of items in the specified collection that satisfy
    a given condition. The condition is defined as the absence of a specific field value
    for the provided key. The function ensures that items satisfying the filter conditions
    are precisely counted.

    :param chave: The key or field to be checked for specific conditions in the collection
                  items.
    :type chave: str
    :return: The count of items in the collection that have the specified key not matching
             the given condition.
    :rtype: int
    """
    # Define o filtro para buscar vetores onde o campo 'especialidade' não é nulo
    filters = models.Filter(
        must_not=[
            # models.HasIdCondition(has_id=True),  # Garante que o ponto existe
            models.FieldCondition(
                key=chave,
                match=models.MatchValue(value=" "),
            )
        ]
    )

    # Realiza a contagem dos pontos que соответствуют ao filtro
    count_result = client.count(
        collection_name=COLLECTION_NAME,
        count_filter=filters,
        exact=True  # Para obter uma contagem precisa
    )

    quantidade = count_result.count
    print(f"A quantidade de itens com a propriedade {chave} preenchida é: {quantidade}")
    return quantidade


def upsert_to_qdrant(laudoPdf) -> bool:
    """
    Insert or update a document in the Qdrant collection.

    This function takes a document (laudoPdf), converts it into the required
    format for Qdrant, and inserts or updates it in the specified collection.
    The document must have an `id`, an `embedding` representing its vector,
    and must be convertible to a dictionary format for payload metadata.

    :param laudoPdf: The document to be upserted into Qdrant. It must have an
        `id`, `embedding` as a list of vectors, and should be convertible to a
        dictionary format.
    :type laudoPdf: Any
    :return: A boolean flag indicating whether the upsert operation was
        successful. Returns `True` if successful, otherwise `False`.
    :rtype: bool
    """
    try:
        points = []

        points.append(
            models.PointStruct(
                id=str(laudoPdf.id),
                vector=laudoPdf.embedding,  # This is now a list of vectors
                payload=laudoPdf.dict(),  # can also add other metadata/data
            )
        )

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
            wait=False,
        )

    except Exception as e:
        print(f"Error during upsert: {e}")
        return False
    return True


# def closeQdrant(self):
#     client.close()


# def upsert_to_qdrant(multivector, protocolo) -> bool:
#     try:
#         points = []
#
#         points.append(
#             models.PointStruct(
#                 id=protocolo.id,
#                 vector=multivector[0],  # This is now a list of vectors
#                 payload=protocolo,  # can also add other metadata/data
#             )
#         )
#
#         client.upsert(
#             collection_name=COLLECTION_NAME,
#             points=points,
#             wait=False,
#         )
#     except Exception as e:
#         print(f"Error during upsert: {e}")
#         return False
#     return True