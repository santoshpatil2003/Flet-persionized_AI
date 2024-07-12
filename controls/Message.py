import flet as ft
from time import sleep
import pyperclip



class Message(ft.Container):
    def __init__(self, ai : bool, message: str):
        super().__init__()
        self.ai = ai
        self.width = 980 
        self.message = message
        self.formated_message = ""
        self.m = ft.Text(value="")
        self.content = ft.Row(
            alignment = (ft.MainAxisAlignment.START if self.ai == True else ft.MainAxisAlignment.END),
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(value="AI" if self.ai else "User", color=ft.colors.CYAN_ACCENT),
                                        ),
                                        ft.Container(
                                            content=ft.IconButton(icon=ft.icons.COPY_ROUNDED, icon_size=15, on_click= self.copy_clip,icon_color=ft.colors.CYAN_ACCENT) if self.ai else None,

                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                # bgcolor=ft.colors.RED,
                                height= 30,
                                margin= 0
                            ),
                            ft.Row(
                                controls=[
                                    self.m,    
                                ],
                            ),
                        ],
                    ),
                    bgcolor="#13121D",
                    padding=10,
                    border_radius=5,
                    margin=10,
                    # border=ft.border.all(1, ft.colors.WHITE10),
                )
            ],
        )
    
    def copy_clip(self, _ ):
        pyperclip.copy(text=self.m.value)
        self.page.snack_bar = ft.SnackBar(ft.Text("Text saved on the clipboard"))
        self.page.snack_bar.open = True
        self.page.update()
    
        
    def format_str(self, context : str) -> str:
        c = -1
        space_i = 0
        l = list(context)
        st = ""
        if len(l) < 140:
            return context
        for i in range(len(l)):
            c += 1
            if l[i] == " ":
                space_i = i
            if l[i] == "\n":
                c = -1
            if c == 140:
                if l[i] == " ":
                    l[i] = ""
                    l.insert(i, "\n")
                    c = -1
                elif l[i + 1] == " ":
                    l[i + 1] = ""
                    l.insert(i + 1, "\n")
                    c = -1
                else:
                    l[space_i] = ""
                    l.insert(space_i + 1, "\n")
                    c = -1
        
        for j in range(len(l)):
            if l[j] == "*":
                l[j] = ""
            
        for i in l:
            st += i
        
        return st
        
    def build(self):
        self.formated_message = self.format_str(context = self.message)
        if self.ai == True:
            for i in self.formated_message:
                self.m.value = self.m.value + i
        else:
            self.m.value = self.formated_message
        
        
        