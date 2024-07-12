import os
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.core.memory import ChatMemoryBuffer, ChatSummaryMemoryBuffer
from llama_index.core import Settings, Document,StorageContext , ServiceContext, load_index_from_storage, VectorStoreIndex, SimpleDirectoryReader, PromptTemplate, Prompt
from llama_index.embeddings.gemini import GeminiEmbedding
# from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings




class Embedding:
    def __init__(self, agent_id):
        self.agent_id = agent_id



    def DataSaver(self) -> bool:
        url = f'Backend/Files/{self.agent_id}'

        
        load_dotenv() 
        API_KEY = os.getenv("GOOGLE_API_KEY")
        os.environ["GOOGLE_API_KEY"] = API_KEY
        
        llm = Gemini()
        documents = SimpleDirectoryReader(url).load_data()

        model_name = "models/embedding-001"
        embed_model = GeminiEmbedding(model_name=model_name, api_key=API_KEY)

        service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model, chunk_size=512)
        index = VectorStoreIndex.from_documents(documents,service_context=service_context)
        
        embed_url = f'Backend/EmbeddedFiles/{self.agent_id}'
        index.storage_context.persist(persist_dir= embed_url)
        return True