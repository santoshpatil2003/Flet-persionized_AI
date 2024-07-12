import flet as ft
# from time import sleep
from controls.homepage import Home
# from controls.Agents import Agents
# from controls.sidebar import sidebar
# from controls.Chat import Chat
from controls.ProgressRings import ProgressRings
from Database.Agents_data import AgentsData
from Backend.Fastapi import AgentEdit
from controls.AgentsPage import AgentsPage

# how llamaindex is different from langchain?


def main(page : ft.Page):
    
    page.views.clear()
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    # page.padding = 50
    page.bgcolor = "#070C12"
    a = AgentsData()
    ae = AgentEdit()
    
    # def spinchange(s : bool) -> bool:
    #     spin = s
    #     return spin

    def open_dlg_modal(_):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    # def open_dlg_modal(e : ft.AlertDialog):
    #     print("click")

    def close_dlg_modal(_):
        dlg_modal.open = False
        page.update()
        
    def rebuild_home():
        home = Home(add=add, add2=add_agent, a=a)
        page.views[0].controls = [home]
        page.update()
    
    def create_new_agent_update(e):
        name_a =  e.control.value
        a.update_name(name_a)
        e.control.value = ""
        # page.update()
        
    def create_new_agent(e):
        n = a.get_name()
        a.create_agent(n)
        dlg_modal.open = False
        rebuild_home()
        
    dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create Your Agent"),
            bgcolor= "#13121D",
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            hint_text="Name Your Agent",
                            border_color= "#202328",
                            on_change=create_new_agent_update,
                            )
                        ]
                    ),
                height= 50,
                width= 10
                ),
            actions=[
                ft.TextButton("Cancel", on_click= close_dlg_modal),
                ft.TextButton("Create", on_click= create_new_agent),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
    
    add = ft.GestureDetector(
        mouse_cursor= ft.MouseCursor.CLICK,
        on_tap= open_dlg_modal,
        content=ft.Card(
        content=ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
            content=ft.Image(
            src="assets/Agent_add.png",
            fit=ft.ImageFit.FILL,
            repeat=ft.ImageRepeat.NO_REPEAT,
            height=80,
            width= 80,
                    ),
                ),
            ]
        ),
        color="#13121D",
        ),
    )
    

    def add_agent(name: str, id : str) -> ft.GestureDetector:
        add2 = ft.GestureDetector(
            mouse_cursor= ft.MouseCursor.CLICK,
            on_tap= lambda _: page.go(f'/{id}'),
            content=ft.Card(
            content=ft.Column(
            # alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content= ft.PopupMenuButton(
                                            items= [
                                                ft.PopupMenuItem(text="Delete", height= 20, on_click= lambda _ : delete_an_agent(agent_id= id) ),
                                            ]
                                        ),
                                    margin= ft.margin.only(right=0, top=0)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ],
                ),
                ft.Container(
                    content= ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(value=name),
                                ),
                            ],
                            # vertical_alignment= ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height= 85
                ),
                )
                ]
            ),
            color="#13121D",
            ),
        )
        return add2
    
    
    def delete_an_agent(agent_id):
        a.delete_agent(agent_id=agent_id)
        rebuild_home()
        
    # def delete_all_history(agent_id):
    #     a.delete_history(agent_id=agent_id)
        # Chat(agent_id= agent_id, agent_edit= ae)
        
        
    def route_change(e : ft.RouteChangeEvent):
        page.views.clear()
        # spin = True
        page.views.append(
            ft.View(
                route= '/',
                controls= [
                    Home(add=add , add2= add_agent, a=a),
                    ],
                bgcolor = '#070C12',
                vertical_alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.MainAxisAlignment.CENTER,
            )
        )
        
        l = a.get_data()
        for i in l:
            if page.route == f'/{str(i["_id"])}':
                page.views.append(
                    ft.View(
                        route= f'/{str(i["_id"])}',
                        controls= [ProgressRings()],
                        bgcolor = '#070C12',
                        vertical_alignment= ft.MainAxisAlignment.CENTER,
                        horizontal_alignment= ft.MainAxisAlignment.CENTER,
                    )
                )
                page.update()
                ag = AgentsPage(agent_data_i=i, agent_data= a, agent_edit= ae)
                page.views.pop()
                page.update()
                print("done list")
                page.views.append(
                    ag
                )
        page.update()
        page.on_route_change = route_change
        
    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.View = page.views[-1]   
        page.go(top_view.route)
        
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)    


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)