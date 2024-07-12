import flet as ft
from controls.Addfilebutton import AddFileButton
from controls.Message import Message
from Backend.Fastapi import Agent, AgentEdit
from Backend.Memory import Memory
from controls.TypingAnimation import AnimatedChatBubble
from Database.Agents_data import AgentsData

class Chat(ft.Container):
    def __init__(self, agent_id, agent_edit):
        print("chat started")
        super().__init__()
        self.agent_id = agent_id
        self.agentdata = AgentsData()
        self.memory = Memory(agent_id=agent_id).memory()
        self.agent = Agent(chat_history=self.memory, agent_id=agent_id, agent_edit=agent_edit)
        self.agent_edit = agent_edit
        self.height = 640
        self.width = 1000
        self.margin = ft.margin.symmetric(vertical=-10)
        self.list = ft.ListView(
            controls=[],
            padding=ft.padding.only(right=20),
            auto_scroll=True,
            expand=1,
        )
        self.text_field = ft.TextField(
            hint_text="Message Your AI", 
            height=45, 
            width=600, 
            bgcolor='#13121D',
            border_radius=ft.BorderRadius(30,30,30,30),
            content_padding=15,
            on_change=self.q_update
        )
        self.send_button = ft.ElevatedButton(
            text="send", 
            bgcolor='#13121D',
            style=ft.ButtonStyle(color="#13121D", shape=ft.RoundedRectangleBorder(radius=5)),
            height=45,
            on_click=self.get_ans
        )
        self.content = self.build_layout()

    def build_layout(self):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            height=530, 
                            content=ft.Column(controls=[self.list]),
                            expand=True,
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=self.text_field,
                                    margin=ft.margin.symmetric(vertical=-7, horizontal=5),
                                    border_radius=ft.BorderRadius(30,30,30,30),
                                ), 
                                ft.Container(
                                    content=self.send_button,
                                    margin=ft.margin.symmetric(vertical=-10, horizontal=-10),
                                    border_radius=ft.BorderRadius(30,30,30,30),
                                )
                            ],
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        )

    def build(self):
        self.page.on_resize = self.page_resize
        self.load_chat_history()
        return self.content

    def page_resize(self, e):
        print("New page size:", self.page.window_width, self.page.window_height)
        # Adjust layout based on new size if needed
        self.text_field.width = min(600, self.page.window_width - 100)  # Adjust width based on window size
        self.page.update()

    def load_chat_history(self):
        agent_data = AgentsData()
        d = agent_data.get_data_of(agent_id=self.agent_id)
        for i in d:
            if len(i["chat_history"]) != 0:
                for l in i["chat_history"]:
                    self.list.controls.append(Message(ai=l['ai'], message=l['message']))

    def q_update(self, e):
        name_a = e.control.value
        self.agent.update_query(name_a)
        print(self.agent.get_query())

    def add_message(self, message: dict):
        specific_agent = self.agentdata.get_data_of(agent_id=self.agent_id)
        for i in specific_agent:
            lis = i["chat_history"]
            lis.append(message)
            print(lis)
            self.agentdata.update_history(agent_id=self.agent_id, new_his=lis)

    def get_ans(self, e):
        n = self.agent.get_query()
        mes_user = Message(ai=False, message=n)
        self.add_message(message={"ai": False, "message": n})
        self.list.controls.append(mes_user)
        self.list.controls.append(AnimatedChatBubble())
        self.page.update()
        edi = self.agent_edit.get_edit()
        ans = self.agent.agent(user_input=n, edit=edi)
        self.list.controls.pop()
        print(ans)
        mes_ai = Message(ai=True, message=ans)
        self.add_message(message={"ai": True, "message": ans})
        self.list.controls.append(mes_ai)
        self.text_field.value = ""  # Clear the text field after sending
        self.page.update()