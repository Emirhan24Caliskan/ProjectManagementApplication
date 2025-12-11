import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Project Management Systems")
        self.geometry("600x300")
        self._set_appearance_mode("System")
        self.minsize(width=600, height=300)

        #Ana sayfadaki projeler ve proje oluştur butonları. Ve diğer butonlar------------------------------------------------------------
        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)  # Üst Tampon (Boşluk)
        #self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.create_project_button = ctk.CTkButton(self, text="Create Project", command=self.project_create_button_callback,
                                                   fg_color="#7E30CC", hover_color="#9345D9", text_color="white", width=200)
        self.create_project_button.grid(row=0, column=0, padx=200, pady=(15,0))
        self.show_project_button = ctk.CTkButton(self, text="Show Projects",
                                                   command=self.project_show_button_callback,
                                                   fg_color="#7E30CC", hover_color="#9345D9", text_color="white", width=200)
        self.show_project_button.grid(row=1, column=0, padx=0, pady=15)
        self.create_project_button = ctk.CTkButton(self, text="Settings",
                                                   command=self.settings_button_callback,
                                                   fg_color="#7E30CC", hover_color="#9345D9", text_color="white",
                                                   width=200)
        self.create_project_button.grid(row=3, column=0, padx=200, pady=(70,0))
        self.show_project_button = ctk.CTkButton(self, text="About",
                                                 command=self.about_button_callback,
                                                 fg_color="#7E30CC", hover_color="#9345D9", text_color="white",
                                                 width=200)
        self.show_project_button.grid(row=4, column=0, padx=0, pady=15)


    def project_create_button_callback(self):
        print("1")

    def project_show_button_callback(self):
        print("2")
    def settings_button_callback(self):
        print("3")
    def about_button_callback(self):
        print("4")
#---------------------------------------------------------------------------------------------------------------------------------------


app = MainWindow()
def start():
    app.mainloop()
