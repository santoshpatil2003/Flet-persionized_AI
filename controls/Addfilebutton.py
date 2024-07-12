import flet as ft


class AddFileButton(ft.ElevatedButton):
    def __init__(self, click):
        super().__init__()
        self.height = 100
        self.width = 200
        self.icon = "add"
        self.text = "Add File"
        self.style = ft.ButtonStyle(color= "#13121D", shape= ft.RoundedRectangleBorder(radius=5))
        self.on_click = click
        
    # def did_mount(self):
    #     self.file_picker = ft.FilePicker()
    #     self.page.overlay.append(self.file_picker)
    #     self.page.update()
        
    # def click(self, _):
    #     self.file_picker.pick_files(allow_multiple=True)
        
    
    # def build(self):
    #     # file_picker = ft.FilePicker()
    #     # self.page.overlay.append(file_picker)
    #     self.page.update()
        
        
        