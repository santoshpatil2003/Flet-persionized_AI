import flet as ft
from controls.Addfilebutton import AddFileButton
import shutil
import os
from Backend.FileUpload import FileU
from controls.IconButton import IconBu
from Backend.Embedding import Embedding

class AddFile(ft.Container):
    def __init__(self, agent_id):
        super().__init__()
        self.bgcolor = '#13121D'
        self.agent_id = agent_id
        self.embedding = Embedding(agent_id=agent_id)
        self.height = 250  
        self.width = 250
        self.margin = 0
        self.upload = ft.Container(
                            content=ft.ElevatedButton(text="Upload", on_click=self.upload_files),
                            bgcolor='#13121D',
                            height=50,
                            width=115,
                            padding=10,
                        )
        self.file = ft.ListView(
            controls=[],
            expand=True,
            spacing=5,
            padding=10
        )
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        AddFileButton(click=self.click)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=self.file,
                            bgcolor='#13121D',
                            height=100,
                            width=250,
                            padding=10,
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        self.upload
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def file_uploaded(self, e: ft.FilePickerResultEvent):
        if self.file_picker.result is not None and self.file_picker.result.files is not None:
            fil = FileU(agent_id=self.agent_id)
            for f in self.file_picker.result.files:
                fil.Filesupload(filepath=f.path, filename=f.name)
            l = fil.getfile()
            for i in l:
                self.file.controls.append(
                    ft.ListTile(
                        title=ft.Text(value=str(i)),
                        height=25,
                        trailing=IconBu(name=i, fil=fil, agent_id=self.agent_id, filelist=self.file)
                    )
                )
            self.upload.content = ft.ElevatedButton(text="Upload", on_click=self.upload_files)
            self.upload.width = 115
            self.file.update()
            self.upload.update()

    def did_mount(self):
        self.file_picker = ft.FilePicker(on_result=self.file_uploaded)
        self.page.overlay.append(self.file_picker)
        self.page.update()

    def click(self, _):
        self.file_picker.pick_files(allow_multiple=True)

    def upload_files(self, _):
        # Debugging: Ensure this method is called
        self.upload.content = ft.ProgressRing()
        self.upload.width = 50
        self.upload.update()
        d = self.embedding.DataSaver()
        print(f"Finished Embedding: {d}")
        self.upload.content = ft.ElevatedButton(text="Done", disabled= True)
        self.upload.width = 115
        self.upload.update()

    def build(self):
        self.spin = False
        url = f'Backend/Files/{self.agent_id}'
        if os.path.exists(url):
            fil = FileU(agent_id=self.agent_id)
            l = fil.getfile()
            print("finding file in addfile started")
            for i in l:
                self.file.controls.append(
                    ft.ListTile(
                        title=ft.Text(value=str(i)),
                        height=25,
                        trailing=IconBu(name=i, fil=fil, agent_id=self.agent_id, filelist=self.file)
                    )
                )
            print("appending all file in addfile has ended")
        
        if os.path.exists(url) == False or len(os.listdir(url)) == 0:
            self.upload.content = ft.ElevatedButton(text="Upload", disabled= True)
            self.upload.width = 115
            # self.upload.update()

