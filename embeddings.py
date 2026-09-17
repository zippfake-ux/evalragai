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

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Full-time employees receive 15 paid vacation days."
)

embedding = response.data[0].embedding 

print("Embedding dimensions: ", len(embedding))
print("First 10 values", embedding[:10])