import flet as ft
from Backend.FileUpload import de
# from controls.Addfile import AddFile
from Backend.FileUpload import FileU

class IconBu(ft.IconButton):
    def __init__(self, name, fil, agent_id, filelist):
        super().__init__()
        self.icon="cancel" 
        self.icon_size=17
        self.agent_id = agent_id
        self.fil = fil
        self.on_click= lambda _ : self.deletefile()
        self.name = name
        self.filelist = filelist
        
    # def deletefile(self):
    #     # fil.delete_file(f"Backend/Files/{self.agent_id}/{i}")
    #     # n = de(i)
    #     print(f"delete fileeeee:  {self.name}")
    # self.file.update()
    
    def build(self):
        return super().build()
    
    def deletefile(self):
        self.fil.delete_file(f"Backend/Files/{self.agent_id}/{self.name}")
        print(f"delete fileeeee:  {self.name}")
        # fil = FileU(agent_id= self.agent_id)
        # l = fil.getfile()
        # for i in l:
        #     print(i)
        #     self.filelist.controls.append(
        #         ft.ListTile(
        #             title=ft.Text(value=str(i)),
        #             height=25,
        #             trailing= IconBu(name = i, fil=fil, agent_id=self.agent_id, filelist=self.filelist)
        #         )
        #     )
        print(self.filelist.controls)
        # self.filelist.controls.pop()
        # self.page.go(f'/{str(self.agent_id)}')
        self.filelist.update()
        
    