# from fastapi import FastAPI
# # from pydantic import BaseModel
# # from llama_index.llms import gemini
# import json
# import os
# from llama_index.llms.gemini import Gemini
# from dotenv import load_dotenv



# class Agent:
#     def __init__(self) -> None:
#         load_dotenv() 
#         API_KEY = os.getenv("GOOGLE_API_KEY")
#         os.environ["GOOGLE_API_KEY"] = API_KEY
#         self.query : str = ""
        
#     def get_query(self):
#         return self.query
    
#     def update_query(self, query: str):
#         self.query = query
        
    
#     def agent(self, item):
#         safe = [
#         {
#             "category": "HARM_CATEGORY_DANGEROUS",
#             "threshold": "BLOCK_NONE",
#         },
#         {
#             "category": "HARM_CATEGORY_HARASSMENT",
#             "threshold": "BLOCK_NONE",
#         },
#         {
#             "category": "HARM_CATEGORY_HATE_SPEECH",
#             "threshold": "BLOCK_NONE",
#         },
#         {
#             "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#             "threshold": "BLOCK_NONE",
#         },
#         {
#             "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#             "threshold": "BLOCK_NONE",
#         },
#     ]
#         llm = Gemini(model_name="models/gemini-1.5-pro", safety_settings=safe)
#         q = llm.complete(item)
#         return q.text



import os
import datetime as t
from dotenv import load_dotenv
from llama_index.core.tools import QueryEngineTool
from llama_index.core import Settings, PromptTemplate
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
from llama_index.core import StorageContext,load_index_from_storage, PromptTemplate
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core.agent import ReActAgent

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key is not None:
    os.environ["GOOGLE_API_KEY"] = api_key
else:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCUUXynNiEloPn_zQiJ44cdl6LxkTIKBXI"

def format_upload(context, agent_id)-> None:
    format1 = str(context)
    if os.path.exists(f"Backend/Brain/{agent_id}/task.txt"):
        with open(f"Backend/Brain/{agent_id}/task.txt", 'w', encoding='utf-8') as f:
            f.write(format1)
    else:
        os.mkdir(f"Backend/Brain/{agent_id}")
        with open(f"Backend/Brain/{agent_id}/task.txt", 'x', encoding='utf-8') as f:
            f.write(format1)
            

def check_first(agent_id):
    url = f"Backend/Brain/{agent_id}"
    if os.path.exists(url) and len(os.listdir(url)) > 0:
        b = True
    else:
        b = False
    return b

def get_data(agent_id):
    url = f"Backend/Brain/{agent_id}/task.txt"
    with open(url, 'r') as f:
        h = f.read()
    return str(h)

class AgentEdit:
    def __init__(self):
        self.edit : bool = False
    
    def get_edit(self):
        return self.edit
    
    def update_edit(self, edit: str):
        self.edit = edit

class Agent:
    def __init__(self, chat_history, agent_id, agent_edit):
        # load_dotenv()
        # api_key = os.getenv("GOOGLE_API_KEY")
        # os.environ["GOOGLE_API_KEY"] = api_key
        # self.agent_edit = AgentEdit()
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if api_key is not None:
            os.environ["GOOGLE_API_KEY"] = api_key
        else:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyCUUXynNiEloPn_zQiJ44cdl6LxkTIKBXI"
        
        
        self.agent_id = agent_id
        self.agent_edit = agent_edit
        self.memory = chat_history
        self.llm = Gemini(model_name="models/gemini-pro", safety_settings=None)
        self.embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=api_key)
        Settings.embed_model = self.embed_model
        Settings.llm = self.llm
        self.query : str = ""
        
    def get_query(self):
        return self.query
    
    def update_query(self, query: str):
        self.query = query

    def agent(self, user_input, edit) -> list:
        embed_url = f'Backend/EmbeddedFiles/{self.agent_id}'
        storage_context = StorageContext.from_defaults(persist_dir=embed_url)
        index1 = load_index_from_storage(storage_context)
        knowledge = index1.as_query_engine(memory=self.memory)

        query_engine_tools1 = [
            QueryEngineTool.from_defaults(
                query_engine=knowledge,
                name="KnowledgeBase",
                description=(
                    "Provides information about Content you should write as a copywriter."
                    "Use a detailed plain text question as input to the tool."
                ),
            ),
        ]
        
        if check_first(agent_id=self.agent_id) == False or self.agent_edit.get_edit() == True:

            pack = ReActAgent(tools=query_engine_tools1, llm=self.llm, memory=self.memory, verbose=True)
            response1 = pack.chat(user_input)
            response = response1.response
        else:
   
            pack = ReActAgent(tools=query_engine_tools1, llm=self.llm, memory=self.memory, verbose=True)
            response1 = pack.chat(user_input)
            response = response1.response
            get_format = get_data(agent_id=self.agent_id) 
            response = self.rewrite(context=str(response), format=str(get_format))
        
        return response
    
    
    def rewrite(self, context, format):
        prompt = """Rewrite the below context
                    -------------------------------
                    {context}
                    -------------------------------
                    in the given below format (not same but similar to it).
                    Format: {format}
                """
        template_var_mappings = {"context": "context", "format": "format"}
        prompt_tmpl = PromptTemplate(prompt, template_var_mappings=template_var_mappings)
        
        fmt_prompt = prompt_tmpl.format(
                context=context,
                format=format,
        )
        p = QueryPipeline(chain=[prompt_tmpl, self.llm], verbose=True)
        output = p.run(context=context, format = format)
        return str(output)
    
    
    
    def InsertDocument(self, index, response) -> None:
        formated_str = format_upload(response) 
    




# if __name__ == "__main__":
#     llm = Gemini(model_name="models/gemini-pro", safety_settings=None)
#     chat_history = []
#     memory = ChatMemoryBuffer.from_defaults(llm=llm, chat_history=chat_history, token_limit=3500)
#     agent = Agent(chat_history=memory)
#     loop = True
#     while loop:
#         i = input("input:  ")
#         res = agent.agent2(i)
#         response = res[0]
#         index = res[1]
#         chat_history.append(ChatMessage(role="user", content=i))
#         chat_history.append(ChatMessage(role="assistant", content=response))
#         print("------------------------------------------------------------")
#         print(response)
#         inp = input("choose: ")
#         if inp == "y":
#             agent.InsertDocument(index, response)
#         else:
#             loop = True

    


