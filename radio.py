import customtkinter
import Song
import spotipy

class Radio(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Radio")
        self.geometry("700x350")
        self.spotify_connection = False
        self.curr_song = Song.Song("On the Radio", "Donna Summer", "On the Radio: Greatest Hits Volumes I & II", 1979).get_song()

        REDIRECT_URI = "http://127.0.0.1:8888/callback"

        # track state
        self.modes = ['study', 'normal', 'hype']
        self.mode = 1

        # setup grid
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.grid_rowconfigure((0,1,2,3), weight=1, uniform='b')

        # widgets
        self.connection_indicator = customtkinter.CTkCanvas(self, width=25, height=25, bg=self.cget("bg"), highlightthickness=0)
        self.connection_indicator.create_oval(0, 0, 15, 15, fill="red" if not self.spotify_connection else "green")
        self.connection_label = customtkinter.CTkLabel(self, font=("Arial", 10),text="Not connected to Spotify" if not self.spotify_connection else "Connected to Spotify")
        self.study_btn = customtkinter.CTkButton(self, text="Study", command=lambda: self.change_study_mode('s'))
        self.normal_btn = customtkinter.CTkButton(self, text="Normal", command=lambda: self.change_study_mode('n'))
        self.hype_btn = customtkinter.CTkButton(self, text="Hype", command=lambda: self.change_study_mode('h'))
        self.mode_label = customtkinter.CTkLabel(self, text=f"Current Mode: {self.modes[self.mode].upper()}")

        # currently playing
        self.song_name_label = customtkinter.CTkLabel(self, text=f"Song Name: {self.curr_song['title']}")


        # add to grid
        self.connection_indicator.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.connection_label.grid(row=0, column=0, padx=30, sticky="nw", columnspan=2)
        self.study_btn.grid(row=1, column=1, padx=10, sticky="n")
        self.normal_btn.grid(row=1, column=2, padx=10, sticky="n")
        self.hype_btn.grid(row=1, column=3, padx=10, sticky="n")
        self.mode_label.grid(row=0, column=1, columnspan=3)
        # curr playing
        self.song_name_label.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="w")

    def change_study_mode(self, x):
        match x.lower():
            case 's':
                print("Study Mode: 0")
                self.mode = 0
            case 'n':
                print("Normal Mode: 1")
                self.mode = 1
            case 'h':
                print("Hype Mode: 2")
                self.mode = 2
        self.mode_label.configure(text=f"Current Mode: {self.modes[self.mode].upper()}")

    def connect_spotify(self):
        # Implementation for connecting to Spotify
        self.spotify_connection = True
        self.update_connection_indicator()
    
    def update_connection_indicator(self):
        color = "green" if self.spotify_connection else "red"
        status_text = "Connected to Spotify" if self.spotify_connection else "Not connected to Spotify"
        self.connection_indicator.itemconfig(self.connection_indicator.find_all()[0], fill=color)
        self.connection_label.configure(text=status_text)
    
    def check_spotify_connection(self):
        # Implementation for checking Spotify connection status
        pass

app = Radio()
app.mainloop()