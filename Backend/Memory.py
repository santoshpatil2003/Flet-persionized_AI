from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.llms import ChatMessage
from llama_index.llms.gemini import Gemini
from Database.Agents_data import AgentsData

class Memory:
    def __init__(self, agent_id) -> None:
        self.agent_id = agent_id
        self.chat_his = []
        # self.memory = ChatMemoryBuffer.from_defaults(llm=llm, chat_history=self.chat_his, token_limit=3500)
        self.llm = Gemini(model_name="models/gemini-pro", safety_settings=None)
        
        
    def get_his(self):
        #{"ai" : bool, "content": str}
        data = AgentsData()
        d = data.get_data_of(agent_id=self.agent_id)
        for i in d:
            his = i["chat_history"]
            for j in his:
                x = ChatMessage(role= "assistant" if j["ai"] == True else "user", content= j["message"])
                self.chat_his.append(x)
        return self.chat_his
        
    def memory(self):
        self.get_his()
        memory = ChatMemoryBuffer.from_defaults(llm=self.llm, chat_history=self.chat_his, token_limit=3500)
        return memory