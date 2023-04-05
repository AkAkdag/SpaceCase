import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hallo")
        self.label.pack()
        self.entry = tk.Entry(self, width=5)
        self.entry.pack()

        self.quit_button = tk.Button(self, text="raden", command=self.woordRaden)
        self.quit_button.pack(side="bottom")

    def woordRaden(self):
        global woorden, punten
        geradenWoord = self.entry.get()
        for woord in woorden:
            if woord == geradenWoord:
                punten += 1
                print("GOED")
            else:
                print("FOUT")
        print("Aantal verdiende punten zijn:", punten)

woorden = ["appel", "peer", "aardbei","watermeloen","banaan"]
punten = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
