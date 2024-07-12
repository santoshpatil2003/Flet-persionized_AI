import flet as ft

class Agents(ft.GestureDetector):
    def __init__(self, page: ft.Page , name: str, first: bool, open_dlg_modal : None):
        super().__init__()
        self.name = name
        self.first = first
        self.open_dlg_modal = open_dlg_modal
        self.on_tap = open_dlg_modal
        self.page = page
        
    def build(self):
        
        def enter(self, e : ft.HoverEvent):
            self.add.content.color = "#3C3B43"
            e.control.update()
    
        # def exit(self, e : ft.HoverEvent):
        #     self.add.content.color = "#13121D"
        #     e.control.update()
        
        def change_view(self, _):
            self.page.go('/agents')
        
        if self.first == True: 
            self.add = ft.GestureDetector(
            on_enter= enter,
            on_exit= exit,
            on_tap= self.on_tap,
            mouse_cursor= ft.MouseCursor.CLICK,
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
        else:
            self.add = ft.GestureDetector(
            mouse_cursor= ft.MouseCursor.CLICK,
            on_tap= self.change_view,
            content=ft.Card(
            content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Text(value= self.name),
                    ),
                ]
            ),
            color="#13121D",
            ),
        )
            
        return self.add
            