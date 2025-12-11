import gui

class Projects:
    def __init__(self, name:str, tasks:list,
                 completion_percentage:int, start_date:str,
                 due_date:str, status:str):
        self.name = name
        self.tasks = tasks
        self.completion_percentage = completion_percentage
        self.start_date = start_date
        self.due_date = due_date
        self.status = status

class Admin:
    projectList = []
    def create_project(self,name):
        self.projectList.append(Projects(name))


admin = Admin

def main():
    gui.start()



if __name__ == "__main__":
    main()