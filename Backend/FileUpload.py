import os
import shutil


class de:
    def __init__(self, name) -> None:
        self.name = name
        
    def get(self):
        return self.name
        


class FileU:
    def __init__(self,agent_id) -> None:
        self.agent_id = agent_id
    
    
    def Filesupload(self, filepath, filename) -> bool:
        if filepath != "" and  filename != "":
            try:
                url = f'Backend/Files/{self.agent_id}/{filename}'
                shutil.copy(filepath , url)
            except FileNotFoundError:
                try:
                    os.mkdir(f'Backend/Files')
                    url = f'Backend/Files/{self.agent_id}/{filename}'
                    shutil.copy(filepath , url)
                except Exception as e:
                    os.mkdir(f'Backend/Files/{self.agent_id}')
                    url = f'Backend/Files/{self.agent_id}/{filename}'
                    shutil.copy(filepath , url)
                
    def getfile(self):
        url = f'Backend/Files/{self.agent_id}'
        files = os.listdir(url)
        return files
    
    
    def delete_file(self, myfile):
        if os.path.isfile(myfile):
            os.remove(myfile)
            # print("Removed: %s " % myfile)
        else:
            print("Error: %s file not found" % myfile)
    
    
    
    
# a = FileU(agent_id="12112")
# # print(a.Filesupload(["hot.txt", "cold.docx"]))
# a.getfile()
# ["hot.txt", "cold.txt"]