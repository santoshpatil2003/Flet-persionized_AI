import flet as ft 
from Database.Agents_data import AgentsData



class Home(ft.GridView):
    
    def __init__(self, add: ft.GestureDetector, add2: ft.GestureDetector, a : object):
        super().__init__()
        self.add = add
        self.add2 = add2
        self.controls.append(self.add)
        self.expand = 1
        self.runs_count = 1
        self.max_extent = 200
        self.child_aspect_ratio = 1
        self.spacing = 5
        self.run_spacing = 5
        self.a = a
        
        
    def build(self):
        # l = ["Twitter Agent", "Youtube Script Writer"]
        # a = AgentsData()
        l = self.a.get_data()
        print(f"list of data {l}")
        for i in l:
            add3 = self.add2(name = i["agent_name"], id = str(i["_id"]))
            # d = self.a.create_agent(name=self.name)
            self.controls.append(
                add3
            )
        
    
    