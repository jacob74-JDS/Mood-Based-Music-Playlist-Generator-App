import webbrowser
from enum import Enum
from typing import Dict, List, Tuple
import tkinter as tk
from tkinter import ttk, messagebox

class Mood(Enum):
    HAPPY = "happy"
    SAD = "sad"
    ENERGETIC = "energetic"
    RELAXED = "relaxed"

class Song:
    def __init__(self, title: str, artist: str, youtube_url: str):
        self.title = title
        self.artist = artist
        self.youtube_url = youtube_url
    
    def __str__(self):
        return f"{self.title} by {self.artist}"

class PlaylistGenerator:
    """Generates music playlists based on user's mood."""
    
    # Color codes for terminal output
    COLOR_CODES = {
        Mood.HAPPY: "\033[93m",     # Yellow
        Mood.SAD: "\033[94m",       # Blue
        Mood.ENERGETIC: "\033[91m",  # Red
        Mood.RELAXED: "\033[92m",   # Green
        "RESET": "\033[0m"          # Reset to default
    }
    
    # Mood-related quotes
    MOOD_QUOTES = {
        Mood.HAPPY: "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        Mood.SAD: "The way sadness works is one of the strange riddles of the world. - Lemony Snicket",
        Mood.ENERGETIC: "Energy and persistence conquer all things. - Benjamin Franklin",
        Mood.RELAXED: "Sometimes the most productive thing you can do is relax. - Mark Black"
    }
    
    def __init__(self):
        self.playlists = self._initialize_playlists()
    
    def _initialize_playlists(self) -> Dict[Mood, List[Song]]:
        """Initialize and return the predefined playlists for each mood."""
        
        return {
            Mood.HAPPY: [
                Song("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
                Song("Don't Stop Me Now", "Queen", "https://www.youtube.com/watch?v=HgzGwKwLmgM"),
                Song("Walking on Sunshine", "Katrina and the Waves", "https://www.youtube.com/watch?v=iPUmE-tne5U"),
                Song("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=Wr9ie2J2690"),
                Song("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw")
            ],
            Mood.SAD: [
                Song("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
                Song("Everybody Hurts", "R.E.M.", "https://www.youtube.com/watch?v=5rOiW_xY-kc"),
                Song("Hurt", "Johnny Cash", "https://www.youtube.com/watch?v=vt1Pwfnh5pc"),
                Song("The Sound of Silence", "Simon & Garfunkel", "https://www.youtube.com/watch?v=4fWyzwo1xg0"),
                Song("Mad World", "Gary Jules", "https://www.youtube.com/watch?v=4N3N1MlvVc4")
            ],
            Mood.ENERGETIC: [
                Song("Eye of the Tiger", "Survivor", "https://www.youtube.com/watch?v=btPJPFnesV4"),
                Song("Lose Yourself", "Eminem", "https://www.youtube.com/watch?v=_Yhyp-_hX2s"),
                Song("Thunderstruck", "AC/DC", "https://www.youtube.com/watch?v=v2AC41dglnM"),
                Song("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg"),
                Song("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g")
            ],
            Mood.RELAXED: [
                Song("Weightless", "Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
                Song("Strawberry Swing", "Coldplay", "https://www.youtube.com/watch?v=oU9qMyeOq4A"),
                Song("River Flows In You", "Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
                Song("Clair de Lune", "Claude Debussy", "https://www.youtube.com/watch?v=CvFH_6DNRCY"),
                Song("Breathe", "Pink Floyd", "https://www.youtube.com/watch?v=3b9i13o8J3E")
            ]
        }
    
    def get_mood_from_input(self, mood_input: str) -> Mood:
        """Convert user input string to Mood enum, case-insensitive."""
        mood_input = mood_input.strip().lower()
        for mood in Mood:
            if mood.value == mood_input:
                return mood
        raise ValueError(f"Invalid mood: {mood_input}")
    
    def generate_playlist_cli(self):
        """Command-line interface for the playlist generator."""
        print("\n=== Mood-Based Music Playlist Generator ===")
        print("Available moods: happy, sad, energetic, relaxed")
        
        while True:
            try:
                mood_input = input("\nHow are you feeling today? ").strip().lower()
                mood = self.get_mood_from_input(mood_input)
                break
            except ValueError:
                print("Invalid mood. Please enter one of: happy, sad, energetic, relaxed")
        
        self.display_playlist(mood)
    
    def display_playlist(self, mood: Mood):
        """Display the playlist for the given mood with colors and quotes."""
        color = self.COLOR_CODES[mood]
        reset = self.COLOR_CODES["RESET"]
        
        print(f"\n{color}=== {mood.value.capitalize()} Playlist ==={reset}")
        print(f"{color}{self.MOOD_QUOTES[mood]}{reset}\n")
        
        for i, song in enumerate(self.playlists[mood], 1):
            print(f"{color}{i}. {song}{reset}")
        
        print(f"\n{color}Enjoy your music!{reset}")
        
        # Ask if user wants to open any songs in browser
        self._ask_to_open_songs(mood)
    
    def _ask_to_open_songs(self, mood: Mood):
        """Ask user if they want to open any songs in browser."""
        while True:
            choice = input("\nWould you like to open a song in your browser? (enter number or 'no'): ")
            if choice.lower() == 'no':
                break
            
            try:
                song_num = int(choice)
                if 1 <= song_num <= len(self.playlists[mood]):
                    song = self.playlists[mood][song_num - 1]
                    webbrowser.open(song.youtube_url)
                    print(f"Opening {song.title}...")
                else:
                    print("Invalid number. Please enter a number from the playlist.")
            except ValueError:
                print("Please enter a valid number or 'no'.")

class PlaylistGeneratorGUI:
    """Graphical user interface for the playlist generator."""
    
    BG_COLORS = {
        Mood.HAPPY: "#FFFACD",     # Lemon Chiffon
        Mood.SAD: "#ADD8E6",      # Light Blue
        Mood.ENERGETIC: "#FFCCCB", # Light Red
        Mood.RELAXED: "#98FB98"    # Pale Green
    }
    
    def __init__(self, root: tk.Tk, generator: PlaylistGenerator):
        self.root = root
        self.generator = generator
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the graphical user interface."""
        self.root.title("Mood-Based Music Playlist Generator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Mood selection
        ttk.Label(self.main_frame, text="Select Your Mood:").pack(pady=5)
        
        self.mood_var = tk.StringVar()
        self.mood_combobox = ttk.Combobox(
            self.main_frame,
            textvariable=self.mood_var,
            values=[mood.value for mood in Mood],
            state="readonly"
        )
        self.mood_combobox.pack(pady=5)
        self.mood_combobox.current(0)  # Set default to first mood
        
        # Generate button
        self.generate_btn = ttk.Button(
            self.main_frame,
            text="Generate Playlist",
            command=self.generate_playlist
        )
        self.generate_btn.pack(pady=10)
        
        # Playlist display
        self.playlist_frame = ttk.Frame(self.main_frame)
        self.playlist_frame.pack(fill=tk.BOTH, expand=True)
        
        # Quote label
        self.quote_label = ttk.Label(
            self.playlist_frame,
            text="",
            wraplength=550,
            justify=tk.CENTER
        )
        self.quote_label.pack(pady=10)
        
        # Playlist treeview
        self.playlist_tree = ttk.Treeview(
            self.playlist_frame,
            columns=("title", "artist"),
            show="headings",
            selectmode="browse"
        )
        self.playlist_tree.heading("title", text="Title")
        self.playlist_tree.heading("artist", text="Artist")
        self.playlist_tree.column("title", width=300)
        self.playlist_tree.column("artist", width=200)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            self.playlist_frame,
            orient=tk.VERTICAL,
            command=self.playlist_tree.yview
        )
        self.playlist_tree.configure(yscrollcommand=scrollbar.set)
        
        self.playlist_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind double click to open song
        self.playlist_tree.bind("<Double-1>", self.open_selected_song)
    
    def generate_playlist(self):
        """Generate and display the playlist based on selected mood."""
        mood_input = self.mood_var.get()
        
        try:
            mood = self.generator.get_mood_from_input(mood_input)
        except ValueError:
            messagebox.showerror("Invalid Mood", "Please select a valid mood from the dropdown.")
            return
        
        # Change background color based on mood
        self.root.configure(background=self.BG_COLORS[mood])
        self.main_frame.configure(style=f"{mood.value}.TFrame")
        
        # Display quote
        self.quote_label.config(text=self.generator.MOOD_QUOTES[mood])
        
        # Clear previous playlist
        for item in self.playlist_tree.get_children():
            self.playlist_tree.delete(item)
        
        # Add songs to treeview
        for song in self.generator.playlists[mood]:
            self.playlist_tree.insert("", tk.END, values=(song.title, song.artist), tags=(song.youtube_url,))
        
        # Configure tag to store YouTube URL
        self.playlist_tree.tag_configure(song.youtube_url, background="white")
    
    def open_selected_song(self, event):
        """Open the selected song in default web browser."""
        selected_item = self.playlist_tree.selection()
        if selected_item:
            youtube_url = self.playlist_tree.item(selected_item, "tags")[0]
            webbrowser.open(youtube_url)

def run_cli():
    """Run the command-line interface version."""
    generator = PlaylistGenerator()
    generator.generate_playlist_cli()

def run_gui():
    """Run the graphical user interface version."""
    root = tk.Tk()
    
    # Create styles for different mood frames
    style = ttk.Style()
    for mood, color in PlaylistGeneratorGUI.BG_COLORS.items():
        style.configure(f"{mood.value}.TFrame", background=color)
    
    generator = PlaylistGenerator()
    app = PlaylistGeneratorGUI(root, generator)
    root.mainloop()

if __name__ == "__main__":
    print("Choose interface:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            run_cli()
            break
        elif choice == "2":
            run_gui()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")