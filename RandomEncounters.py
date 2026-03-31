import random
from npc import Enemy
from battlesystem import BattleSystem

encounters = [
    # Undead
    ("Skeleton", Enemy("Skeleton", 40, 4, 9), "Undead"),
    ("Zombie", Enemy("Zombie", 45, 3, 8), "Undead"),
    ("Ghoul", Enemy("Ghoul", 55, 5, 10), "Undead"),
    ("Wraith", Enemy("Wraith", 60, 6, 12), "Undead"),
    ("Lich", Enemy("Lich", 90, 8, 14), "Undead"),
    ("Blood Lich", Enemy("Blood Lich", 130, 10, 18), "Undead"),

    # Hellish
    ("Imp", Enemy("Imp", 30, 4, 7), "Hellish"),
    ("Hellhound", Enemy("Hellhound", 55, 6, 11), "Hellish"),
    ("Demon", Enemy("Demon", 75, 7, 13), "Hellish"),
    ("Archdemon", Enemy("Archdemon", 110, 9, 15), "Hellish"),
    ("Satan", Enemy("Satan", 200, 12, 20), "Hellish"),
    ("Storm Demon", Enemy("Storm Demon", 135, 11, 18), "Hellish"),

    # Human
    ("Knight", Enemy("Knight", 70, 6, 12), "Human"),
    ("Bounty Hunter", Enemy("Bounty Hunter", 65, 5, 11), "Human"),
    ("Thug", Enemy("Thug", 40, 4, 8), "Human"),
    ("Mercenary", Enemy("Mercenary", 55, 5, 10), "Human"),
    ("Assassin", Enemy("Assassin", 50, 7, 12), "Human"),
    ("Harvest Reaper", Enemy("Harvest Reaper", 110, 10, 17), "Human"),

    # Divine
    ("Angel", Enemy("Angel", 80, 7, 13), "Divine"),
    ("Seraph", Enemy("Seraph", 100, 8, 14), "Divine"),
    ("Valkyrie", Enemy("Valkyrie", 90, 7, 12), "Divine"),
    ("Celestial Guardian", Enemy("Celestial Guardian", 120, 9, 15), "Divine"),
    ("Demigod", Enemy("Demigod", 150, 10, 18), "Divine"),
    ("Eclipse Seraph", Enemy("Eclipse Seraph", 140, 11, 19), "Divine"),

    # Beast
    ("Wolf", Enemy("Wolf", 30, 4, 8), "Beast"),
    ("Bear", Enemy("Bear", 60, 6, 12), "Beast"),
    ("Giant Spider", Enemy("Giant Spider", 45, 5, 10), "Beast"),
    ("Werewolf", Enemy("Werewolf", 55, 6, 12), "Beast"),
    ("Forest Guardian", Enemy("Forest Guardian", 100, 8, 14), "Beast"),
    ("Ancient Treant", Enemy("Ancient Treant", 140, 9, 15), "Beast"),
]

event_loot = {
    "Blood Moon": ["Blood Crystal", "Vampiric Fang"],
    "Solar Eclipse": ["Solar Feather", "Eclipse Shard"],
    "Frozen Night": ["Frost Core", "Icy Soul"],
    "Inferno Day": ["Flame Heart", "Burning Horn"],
    "Shadow Harvest": ["Shadow Essence", "Reaper Scythe Fragment"],
    "Wild Bloom": ["Ancient Seed", "Nature Spirit"],
    "Thunderstorm Surge": ["Storm Core", "Lightning Rune"],
    "Fog of Souls": ["Soul Mist", "Wraith Cloth"],
    "Undead Uprising": ["Bone Crown"],
    "Hellish Uprising": ["Infernal Crest"],
    "Divine Uprising": ["Holy Sigil"],
    "Human Uprising": ["Crusader Medal"],
    "Beast Uprising": ["Alpha Fang"]
}

def random_encounter(player, world):
    weather = world.weather
    season = world.season
    time_of_day = world.time_of_day
    faction_power = world.faction_power
    rep = player.reputation
    current_town_owner = world.towns.get("Town", "Neutral")

    weights = []
    for name, enemy, faction in encounters:
        base = 1

        base += faction_power[faction] // 2

        if weather == "Rain" and faction == "Undead":
            base += 2
        if weather == "Storm" and faction == "Hellish":
            base += 3
        if weather == "Fog" and faction == "Human":
            base += 2
        if weather == "Clear" and faction == "Divine":
            base += 2

        if season == "Winter" and faction == "Undead":
            base += 3
        if season == "Summer" and faction == "Hellish":
            base += 3
        if season == "Fall" and faction == "Human":
            base += 2
        if season == "Spring" and faction == "Beast":
            base += 2

        if time_of_day == "Night" and faction in ["Undead", "Hellish", "Human"]:
            base += 2

        if rep >= 70 and name == "Bounty Hunter":
            base += 5
        elif rep >= 50 and name == "Knight":
            base += 2
        elif rep <= 20 and name in ["Thug", "Assassin"]:
            base += 3

        if current_town_owner != "Neutral":
            if faction == current_town_owner:
                base += 3
            else:
                base -= 1

        weights.append(max(base, 1))

    name, enemy, faction = random.choices(encounters, weights=weights)[0]

    if name == "Bounty Hunter":
        scale = player.reputation // 10
        enemy.hp += scale * 5
        enemy.min_damage += scale
        enemy.max_damage += scale
        print("A powerful Bounty Hunter tracks you due to your reputation!")

    battle = BattleSystem(player, enemy, qte_word="fight")
    result = battle.start_battle()

    if result and world.current_event in event_loot:
        drop = random.choice(event_loot[world.current_event])
        print(f"You obtained event loot: {drop}!")
        player.inventory.append(drop)

    if result:
        world.harm_faction(faction)

    return result
