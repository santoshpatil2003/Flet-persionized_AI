import flet as ft
# from controls.Addfile import AddFile
# from Backend.Fastapi import AgentEdit, format_upload
# from Database.Agents_data import AgentsData
from controls.sidebar import sidebar
from controls.Chat import Chat


class AgentsPage(ft.View):
    def __init__(self, agent_data_i, agent_edit, agent_data):
        super().__init__()
        self.agent_edit = agent_edit
        self.agent_data = agent_data
        self.agent_data_i = agent_data_i
        self.route= f'/{str(self.agent_data_i["_id"])}',
        self.bgcolor = '#070C12'
        self.vertical_alignment= ft.MainAxisAlignment.CENTER
        self.horizontal_alignment= ft.MainAxisAlignment.CENTER
        self.chat = ft.SafeArea(
                                Chat(
                                    agent_id=str(self.agent_data_i["_id"]), 
                                    agent_edit=self.agent_edit
                                    )
                                )
        self.del_his_but = ft.TextButton(
                                        text="Delete History", 
                                        style=ft.ButtonStyle(color= "red"),
                                        on_click= lambda _ : self.delete_all_history(agent_id=agent_data_i["_id"])
                                        )
        self.delete_his = ft.Column(
                                controls=[
                                    self.del_his_but
                                    ], 
                                alignment=ft.MainAxisAlignment.CENTER
                                )
        self.controls = [
                    ft.AppBar(
                        title=ft.Text(self.agent_data_i["agent_name"]), 
                        center_title= True,
                        actions = [
                                ft.Container(
                            content= self.delete_his, 
                            height= 30, 
                            width= 150, 
                            margin= ft.margin.only(left= 0)
                            ),
                        ], 
                        bgcolor= "#13121D"
                    ), 
                    ft.Row(
                        controls=[
                            sidebar(
                                agent_id = str(self.agent_data_i["_id"]), 
                                agent_edit=self.agent_edit
                            ),
                            self.chat
                            ]
                        )
                    ]
        
        
    def delete_all_history(self, agent_id):
        x = self.agent_data.delete_history(agent_id=agent_id)
        if x:  
            self.delete_his.controls[0] = ft.ProgressRing(height=25, width=25)
            self.delete_his.update()
            self.chat = ft.SafeArea(
                                    Chat(
                                        agent_id=str(self.agent_data_i["_id"]), 
                                        agent_edit=self.agent_edit
                                        )
                                    )
            self.controls[1].controls[1] = self.chat
            self.delete_his.controls[0] = self.del_his_but
            self.update()
        # self.page.update()
        # Chat(agent_edit=self.agent_edit, agent_id= self.agent_data_i["_id"]).build()
        # self.page.update()
        
    def build(self):
        return super().build()
        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.title = ft.Text(i["agent_name"])
        # self.center_title= True
        # self.actions = [
        #                         ft.Container(
        #                     content=ft.Column(
        #                         controls=[
        #                             ft.TextButton(
        #                                 text="Delete History", 
        #                                 style=ft.ButtonStyle(color= "red"),
        #                                 on_click= lambda _ : delete_all_history(agent_id=i["_id"])
        #                                 )
        #                             ], 
        #                         alignment=ft.MainAxisAlignment.CENTER
        #                         ), 
        #                     height=30, 
        #                     width= 150, 
        #                     margin=ft.margin.only(left= 0)
        #                     ),
        #                 ]
        # self.bgcolor= "#13121D"