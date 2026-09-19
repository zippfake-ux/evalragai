from openai import OpenAI 
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://zippfake-4596-resource.openai.azure.com/openai/v1"

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

def embed_chunks(chunks):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunks
    )

    embeddings = []

    for item in response.data:
        embeddings.append(item.embedding)

    return embeddings