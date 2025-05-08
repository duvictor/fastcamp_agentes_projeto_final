from qdrant_client import QdrantClient, models
import os
from dotenv import load_dotenv
# from qdrant_client.http import models as rest


# from src.modelo.Protocolo import ProtocoloImagem

# Load environment variables from the .env file
load_dotenv()

COLLECTION_NAME = os.environ["COLLECTION_NAME"]


try:
    client = QdrantClient(path="/tmp/langchain_qdrant")
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



try:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        on_disk_payload=True,  # store the payload on disk
        vectors_config=models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            on_disk=True, # move original vectors to disk
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
            quantization_config=models.BinaryQuantization(
            binary=models.BinaryQuantizationConfig(
                always_ram=True  # keep only quantized vectors in RAM
                ),
            ),
        ),
    )
except Exception as e:
    print(f"Error during create collection: {e}")



def upsert_to_qdrant(laudoPdf) -> bool:
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