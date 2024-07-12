import flet as ft
from controls.Addfile import AddFile
from Backend.Fastapi import AgentEdit, format_upload
from Database.Agents_data import AgentsData


class sidebar(ft.Container):
    def __init__(self, agent_id, agent_edit):
        super().__init__()
        self.bgcolor = '#13121D'
        # self.bgcolor = '#070C12'
        self.agent_id = agent_id
        self.agent = agent_edit
        self.height = 642
        self.width = 300
        self.margin = -10
        self.accept_button = ft.Row(controls=[ft.ElevatedButton(text="Accept", on_click= self.for_upload)],alignment=ft.MainAxisAlignment.CENTER)
        self.switch = ft.Switch(label=None,label_position= ft.LabelPosition.LEFT , value=False, on_change=self.agent_edit)
        self.content = ft.Column(
            controls= [
                ft.Row(controls=[AddFile(agent_id = self.agent_id)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[self.switch],alignment=ft.MainAxisAlignment.CENTER),
                self.accept_button,
                ], 
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            spacing= 100
        )
        
    # def build(self):
    #     file_picker = ft.FilePicker()
    #     self.page.overlay.append(file_picker)
    #     self.page.update()
    def agent_edit(self, e):
        print(f"inintial edit:  {self.agent.get_edit()}")
        value = not self.agent.get_edit()
        self.agent.update_edit(edit= value)
        print(f"after switch:  {self.agent.get_edit()}")
        
    def for_upload(self, _):
        self.accept_button.controls.pop()
        self.accept_button.controls.append(ft.ProgressRing(width=30 , height=30))
        self.accept_button.update()
        agent_data = AgentsData()
        d = agent_data.get_data_of(agent_id=self.agent_id)
        for u in d:
            lis : list = u["chat_history"]
            context = lis[len(lis) - 1]["message"]
            format_upload(context = context, agent_id=self.agent_id)
        self.accept_button.controls.pop()
        self.accept_button.controls.append(ft.ElevatedButton(text="Accept", on_click= self.for_upload))
        self.accept_button.update()