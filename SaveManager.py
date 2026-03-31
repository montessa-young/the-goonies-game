import json
import os
from Player import Player
from StoryManager import StoryState

SAVE_FILE = "saves.json"
SLOTS = ["Slot1", "Slot2", "Slot3", "AutoSave"]


def initialize_save_file():
    if not os.path.exists(SAVE_FILE):
        data = {slot: None for slot in SLOTS}
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=2)


def serialize_player(player):
    return {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "min_damage": player.min_damage,
        "max_damage": player.max_damage,
        "defense": player.defense,
        "crit_rate": player.crit_rate,
        "gold": player.gold,
        "inventory": player.inventory.items,
        "gear": player.inventory.gear,
    }


def serialize_story(story):
    return {
        "achievements": list(story.achievements),
        "boss_gear": list(story.boss_gear),
        "lost_to_sonic": story.lost_to_sonic,
    }


def deserialize_player(data):
    p = Player(data["name"])
    p.hp = data["hp"]
    p.max_hp = data["max_hp"]
    p.min_damage = data["min_damage"]
    p.max_damage = data["max_damage"]
    p.defense = data["defense"]
    p.crit_rate = data["crit_rate"]
    p.gold = data["gold"]

    p.inventory.items = data.get("inventory", [])

    saved_gear = data.get("gear", {})
    for slot in p.inventory.gear.keys():
        p.inventory.gear[slot] = saved_gear.get(slot)

    return p


def deserialize_story(data):
    s = StoryState()
    s.achievements = set(data.get("achievements", []))
    s.boss_gear = set(data.get("boss_gear", []))
    s.lost_to_sonic = data.get("lost_to_sonic", False)
    return s


def save_game(slot, player, story):
    initialize_save_file()
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    data[slot] = {
        "player": serialize_player(player),
        "story": serialize_story(story)
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Game saved to {slot}.")


def load_game(slot):
    initialize_save_file()
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    slot_data = data.get(slot)
    if not slot_data:
        print("No save data in that slot.")
        return None, None

    player = deserialize_player(slot_data["player"])
    story = deserialize_story(slot_data["story"])
    print(f"Loaded {slot}.")
    return player, story


def auto_save(player, story):
    save_game("AutoSave", player, story)
