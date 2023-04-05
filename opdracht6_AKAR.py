import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.woordRaden()

    def create_widgets(self):
        self.label = tk.Label(self, text="Raad de naam van een vrucht")
        self.label.pack()
        self.entry = tk.Entry(self, width=5)
        self.entry.pack()

        self.raden_button = tk.Button(self, text="Raden", command=self.woordRaden)
        self.raden_button.pack(side="bottom")

        self.quit_button = tk.Button(self, text="Afsluiten", command=self.master.quit)
        self.quit_button.pack(side="bottom")

    def woordRaden(self):
        geradenWoord = self.entry.get()
        if geradenWoord in self.woorden:
            self.punten += 1
            print("GOED")
        else:
            print("FOUT")
        self.pogingen -= 1

        if self.punten == 5:
            print("Je hebt het maximale aantal punten bereikt.")
            self.raden_button["state"] = "disabled"
            return

        if self.pogingen == 0:
            print("Maximum aantal gokken bereikt.")
            self.raden_button["state"] = "disabled"
            return

    woorden = ["appel", "peer", "aardbei", "watermeloen", "banaan"]
    punten = 0
    pogingen = 5

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
