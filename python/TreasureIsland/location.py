island_map = {
    "beach": {
        "description": "You are on a sandy beach. You see a path leading into the jungle.",
        "actions": {"go north": "jungle"}
    },
    "jungle": {
        "description": "You are in a dense jungle. The trees are tall and the undergrowth is thick. There is a cave to the east and ancient ruins to the west.",
        "actions": {"go south": "beach", "go east": "cave"}
    },
    "cave": {
        "description": "You are in a dark, damp cave. There is a faint light coming from deeper within.",
        "actions": {"go west": "jungle", "go deeper": "treasure chamber"}
    },
    "treasure chamber": {
        "description": "You have found the hidden treasure chamber! Gold and jewels are piled high. You have achieved your goal!",
        "actions": {"go back": "cave"}
    }
}

current_location = "beach"

def show_curr(location):
    print(island_map[location]["description"])
    print("You can: " + ", ".join(island_map[location]["actions"].keys()))

show_curr(current_location)
