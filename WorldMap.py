import random
from npc import Enemy
from battlesystem import BattleSystem

class WorldMap:
    def __init__(self):
        self.time_of_day = "Day"
        self.weather_types = ["Clear", "Rain", "Storm", "Fog"]
        self.weather = "Clear"

        self.season = "Spring"
        self.seasons = ["Spring", "Summer", "Fall", "Winter"]
        self.rest_count = 0

        # Factions & power
        self.faction_power = {
            "Undead": 5,
            "Hellish": 5,
            "Human": 5,
            "Divine": 5,
            "Beast": 5
        }

        # Faction relations (diplomacy)
        self.faction_relations = {
            "Undead": {"Hellish": 5, "Human": -5, "Divine": -10, "Beast": 0},
            "Hellish": {"Undead": 5, "Human": -10, "Divine": -10, "Beast": -5},
            "Human": {"Undead": -5, "Hellish": -10, "Divine": 5, "Beast": 0},
            "Divine": {"Undead": -10, "Hellish": -10, "Human": 5, "Beast": 0},
            "Beast": {"Undead": 0, "Hellish": -5, "Human": 0, "Divine": 0}
        }

        # Towns, ownership, relations, prosperity, economy, rebuilding
        self.towns = {
            "Town": "Neutral",
            "Village": "Neutral",
            "Fort": "Human",
            "Shrine": "Divine",
            "Ruins": "Undead"
        }

        self.town_relations = {t: 50 for t in self.towns}
        self.town_prosperity = {
            "Town": 50,
            "Village": 50,
            "Fort": 60,
            "Shrine": 70,
            "Ruins": 20
        }
        self.town_economy = {t: 1.0 for t in self.towns}
        self.town_rebuilding = {t: 0 for t in self.towns}

        # Player property & businesses
        self.player_properties = []
        self.player_businesses = {}

        # Shops & gear
        self.faction_shops = {
            "Undead": {
                "dialogue": "A skeletal merchant rattles as you approach.",
                "price_modifier": 1.3,
                "items": ["Cursed Blade", "Bone Armor", "Soul Lantern"]
            },
            "Hellish": {
                "dialogue": "A demon snarls: 'Buy or burn.'",
                "price_modifier": 1.5,
                "items": ["Hellfire Sword", "Infernal Shield", "Demon Blood"]
            },
            "Human": {
                "dialogue": "A friendly merchant greets you.",
                "price_modifier": 1.0,
                "items": ["Iron Sword", "Leather Armor", "Health Potion"]
            },
            "Divine": {
                "dialogue": "A radiant angelic vendor blesses your presence.",
                "price_modifier": 0.9,
                "items": ["Holy Blade", "Blessed Armor", "Light Essence"]
            },
            "Beast": {
                "dialogue": "A wild druid offers natural goods.",
                "price_modifier": 1.1,
                "items": ["Claw Dagger", "Fur Cloak", "Nature Tonic"]
            },
            "Neutral": {
                "dialogue": "A simple merchant tends the shop.",
                "price_modifier": 1.0,
                "items": ["Basic Sword", "Cloth Armor", "Bread"]
            }
        }

        self.faction_gear = {
            "Undead": ["Boneblade", "Soulreaper Staff", "Necrotic Armor"],
            "Hellish": ["Hellfire Axe", "Demonhide Armor", "Infernal Gauntlets"],
            "Human": ["Knight’s Longsword", "Steel Plate", "Royal Shield"],
            "Divine": ["Holy Greatsword", "Blessed Robes", "Wings of Light"],
            "Beast": ["Claw Gauntlets", "Fur Mantle", "Naturebound Bow"]
        }

        # Faction quests & questlines
        self.faction_quests = {
            "Undead": ["Collect 5 Soul Fragments", "Slay a Divine Guardian", "Spread the Fog of Souls"],
            "Hellish": ["Burn a Human Outpost", "Retrieve Demon Blood", "Summon a Lesser Demon"],
            "Human": ["Escort a Merchant", "Defeat a Bandit Camp", "Deliver Supplies to the Fort"],
            "Divine": ["Cleanse a Corrupted Shrine", "Defeat an Undead Champion", "Recover a Holy Relic"],
            "Beast": ["Hunt a Rogue Werewolf", "Gather Rare Herbs", "Protect the Forest Spirits"]
        }

        self.questlines = {
            "Undead": ["Awaken the Crypt", "Raise the Lich King", "Unleash the Plague"],
            "Hellish": ["Open the Hellgate", "Summon the Archdemon", "Crown Satan"],
            "Human": ["Defend the Fort", "Unite the Kingdom", "Crown the True King"],
            "Divine": ["Cleanse the Shrine", "Defeat the Fallen Angel", "Ascend to Light"],
            "Beast": ["Protect the Forest", "Hunt the Alpha", "Restore Nature’s Balance"]
        }
        self.quest_progress = {f: 0 for f in self.questlines}

        # Legendary gear
        self.legendary_gear = {
            "Undead": "Crown of the Lich King",
            "Hellish": "Satan’s Infernal Blade",
            "Human": "King’s Eternal Shield",
            "Divine": "Wings of Ascension",
            "Beast": "Heart of the Wild God"
        }

        # Guilds
        self.guilds = {
            "Adventurer": {"rank": 0, "rep": 0},
            "Mage": {"rank": 0, "rep": 0},
            "Ranger": {"rank": 0, "rep": 0},
            "Assassin": {"rank": 0, "rep": 0}
        }
        self.guild_war_state = None

        # Events & invasions
        self.current_event = None
        self.last_invasion = None
        self.pending_defense = None

        # Main story
        self.main_story_progress = 0
        self.main_story_steps = [
            "A mysterious prophecy emerges.",
            "Factions grow restless.",
            "A great evil stirs beneath the earth.",
            "The factions prepare for war.",
            "The world descends into chaos.",
            "The final battle approaches.",
            "The fate of the world is decided."
        ]

    # --- Core world progression ---

    def advance_time(self, player):
        # Day/night
        self.time_of_day = "Night" if self.time_of_day == "Day" else "Day"
        self.rest_count += 1

        # Season change
        if self.rest_count >= 6:
            self.rest_count = 0
            idx = self.seasons.index(self.season)
            self.season = self.seasons[(idx + 1) % len(self.seasons)]
            print(f"\n🌱 The season has changed! It is now {self.season}.")

        # Weather by season
        if self.season == "Spring":
            weights = [5, 3, 1, 2]
        elif self.season == "Summer":
            weights = [7, 1, 2, 1]
        elif self.season == "Fall":
            weights = [4, 3, 1, 3]
        else:
            weights = [2, 1, 3, 4]
        self.weather = random.choices(self.weather_types, weights=weights)[0]

        print(f"\nTime passes... It is now {self.time_of_day}.")
        print(f"Weather changed to: {self.weather}")

        # Faction chaos
        if random.randint(1, 5) == 1:
            f1, f2 = random.sample(list(self.faction_power.keys()), 2)
            print(f"\n⚔️ A conflict erupts between {f1} and {f2}!")
            if random.random() < 0.5:
                self.harm_faction(f2)
                print(f"The {f1} gained ground over the {f2}.")
            else:
                self.harm_faction(f1)
                print(f"The {f2} pushed back the {f1}.")

        # Town rebuilding
        for town in self.town_rebuilding:
            if self.town_rebuilding[town] > 0:
                self.town_rebuilding[town] -= 1
                if self.town_rebuilding[town] == 0:
                    print(f"\n🏗️ {town} has finished rebuilding!")
                    self.town_prosperity[town] = min(100, self.town_prosperity[town] + 20)

        # Economy update
        for town in self.town_economy:
            owner = self.towns[town]
            power = self.faction_power.get(owner, 5)
            self.town_economy[town] = 1.0 + (power - 5) * 0.05
            if self.current_event == "Blood Moon":
                self.town_economy[town] += 0.1
            if self.current_event == "Solar Eclipse":
                self.town_economy[town] -= 0.1

        # Prosperity drift
        for town in self.town_prosperity:
            owner = self.towns[town]
            if owner in ["Human", "Divine"]:
                self.town_prosperity[town] = min(100, self.town_prosperity[town] + 1)
            if owner in ["Undead", "Hellish"]:
                self.town_prosperity[town] = max(0, self.town_prosperity[town] - 2)
            if owner == "Beast":
                self.town_prosperity[town] += random.choice([-1, 1])

        # Businesses income
        for town, biz in self.player_businesses.items():
            prosperity = self.town_prosperity[town]
            multiplier = 1 + (prosperity - 50) / 100
            income = int(biz["profit"] * multiplier)
            player.gold += income
            print(f"💰 Your {biz['type']} in {town} earned {income} gold.")

        # Events (example: Blood Moon / Eclipse)
        self.current_event = None
        if self.time_of_day == "Night" and random.randint(1, 20) == 1:
            print("\n🌑 BLOOD MOON RISES! Undead roam freely!")
            self.faction_power["Undead"] = min(10, self.faction_power["Undead"] + 3)
            self.faction_power["Hellish"] = min(10, self.faction_power["Hellish"] + 1)
            self.faction_power["Divine"] = max(0, self.faction_power["Divine"] - 2)
            self.current_event = "Blood Moon"
        elif self.time_of_day == "Day" and random.randint(1, 25) == 1:
            print("\n🌞 A SOLAR ECLIPSE DARKENS THE SKY!")
            self.faction_power["Divine"] = min(10, self.faction_power["Divine"] + 3)
            self.faction_power["Undead"] = max(0, self.faction_power["Undead"] - 2)
            self.faction_power["Hellish"] = max(0, self.faction_power["Hellish"] - 1)
            self.current_event = "Solar Eclipse"

        # Faction invasions
        for faction, power in self.faction_power.items():
            if power >= 9 and random.randint(1, 8) == 1:
                town = random.choice(list(self.towns.keys()))
                print(f"\n🔥 {faction.upper()} INVASION! They attack {town}!")
                self.pending_defense = (town, faction)
                self.last_invasion = (town, faction)

        # Diplomacy drift
        for f1 in self.faction_relations:
            for f2 in self.faction_relations[f1]:
                self.faction_relations[f1][f2] += random.choice([-1, 0, 1])
                self.faction_relations[f1][f2] = max(-10, min(10, self.faction_relations[f1][f2]))

        # Guild war chance
        if random.randint(1, 20) == 1:
            guilds = ["Adventurer", "Mage", "Ranger", "Assassin"]
            g1, g2 = random.sample(guilds, 2)
            self.guild_war_state = (g1, g2)
            print(f"\n⚔️ GUILD WAR! The {g1} Guild is fighting the {g2} Guild!")

    # --- Faction helpers ---

    def help_faction(self, faction, amount=1):
        self.faction_power[faction] = min(10, self.faction_power[faction] + amount)
        print(f"You aided the {faction}. Their power grows.")

    def harm_faction(self, faction, amount=1):
        self.faction_power[faction] = max(0, self.faction_power[faction] - amount)
        print(f"You weakened the {faction}.")

    # --- Town & NPC ---

    def enter_town(self, player, town_name):
        owner = self.towns[town_name]
        relation = self.town_relations[town_name]

        print(f"\nYou approach {town_name}. It is controlled by the {owner} faction.")

        if relation >= 70:
            print("The guards greet you warmly and let you in for free.")
            return True
        if 40 <= relation < 70:
            fee = 5
            print(f"The guards demand a small entry fee of {fee} gold.")
            if player.gold >= fee:
                player.gold -= fee
                print("You pay the fee and enter.")
                return True
            print("You cannot afford the fee. Entry denied.")
            return False
        if 20 <= relation < 40:
            fee = 15
            print(f"The guards distrust you. Entry fee is {fee} gold.")
            if player.gold >= fee:
                player.gold -= fee
                print("You pay reluctantly and enter.")
                return True
            print("You cannot afford the fee. Entry denied.")
            return False

        print("The guards shout: 'We know who you are! You’re not welcome here!'")
        print("They attack you!")
        guard = Enemy(f"{owner} Guard", 70, 6, 12)
        battle = BattleSystem(player, guard, qte_word="fight")
        if battle.start_battle():
            print("You defeated the guards and force your way into town.")
            return True
        print("You were driven away from the town.")
        return False

    def npc_reaction(self, player, town_name="Town"):
        owner = self.towns[town_name]
        relation = self.town_relations[town_name]
        event = self.current_event
        invasion = self.last_invasion

        reactions = []

        if town_name in player.npc_memory:
            memory = player.npc_memory[town_name]
            reactions.append(f"NPCs remember: '{memory}'")

        if player.reputation >= 70:
            reactions.append("People whisper: 'The hero has returned…'")
        elif player.reputation <= 20:
            reactions.append("NPCs glare: 'We remember what you did…'")

        if owner != "Neutral":
            reactions.append(f"'We now serve the {owner} faction,' someone mutters.")

        if event == "Blood Moon":
            reactions.append("'The Blood Moon terrifies us all…'")
        elif event == "Solar Eclipse":
            reactions.append("'The Eclipse is a divine omen…'")

        if invasion:
            town, faction = invasion
            reactions.append(f"'Did you hear? {town} fell to the {faction}!'")

        if not reactions:
            reactions.append("The townsfolk greet you cautiously.")

        return random.choice(reactions)

    # --- Shops & economy ---

    def shop(self, player, town_name="Town"):
        owner = self.towns[town_name]
        shop_data = self.faction_shops.get(owner, self.faction_shops["Neutral"])
        econ = self.town_economy[town_name]

        print("\nSHOP")
        print(shop_data["dialogue"])

        modifier = shop_data["price_modifier"]

        print("\nItems for sale:")
        for item in shop_data["items"]:
            base_price = 20
            price = int(base_price * modifier * econ)
            print(f"- {item}: {price} gold")

        if player.reputation >= 60 and owner in self.faction_gear:
            print("\nSpecial Faction Gear:")
            for item in self.faction_gear[owner]:
                price = int(100 * econ)
                print(f"- {item}: {price} gold")

    def black_market_available(self, player, town_name="Town"):
        owner = self.towns[town_name]
        prosperity = self.town_prosperity[town_name]
        if prosperity < 30 and owner in ["Undead", "Hellish", "Beast"] and player.reputation < 40:
            return True
        return False

    def black_market(self, player):
        print("\n🕵️ A shady figure whispers: 'Looking for something… forbidden?'")
        items = {
            "Poison Dagger": 40,
            "Cursed Amulet": 60,
            "Shadow Cloak": 80,
            "Demon Contract": 120
        }
        for item, price in items.items():
            print(f"- {item}: {price} gold")

    def buy_property(self, player, town_name):
        cost = 200
        if town_name in self.player_properties:
            print("You already own property here.")
            return
        if player.gold < cost:
            print("You cannot afford property.")
            return
        player.gold -= cost
        self.player_properties.append(town_name)
        print(f"You purchased a home in {town_name}!")

    def buy_business(self, player, town_name, business_type):
        cost = 300
        if town_name in self.player_businesses:
            print("You already own a business here.")
            return
        if player.gold < cost:
            print("You cannot afford this business.")
            return
        player.gold -= cost
        self.player_businesses[town_name] = {
            "type": business_type,
            "profit": 20,
            "level": 1
        }
        print(f"You purchased a {business_type} in {town_name}!")

    # --- Quests & questlines ---

    def generate_faction_quest(self, player, town_name="Town"):
        owner = self.towns[town_name]
        quests = self.faction_quests.get(owner, [])
        if not quests:
            return "No quests available."
        quest = random.choice(quests)
        player.npc_memory[town_name] = f"They asked you to: {quest}"
        rep_gain = 3 if owner not in ["Hellish", "Undead"] else -3
        return {"quest": quest, "faction": owner, "rep_gain": rep_gain}

    def advance_questline(self, player, faction):
        progress = self.quest_progress[faction]
        steps = self.questlines[faction]
        if progress >= len(steps):
            print(f"The {faction} questline is complete.")
            return
        print(f"Questline Step: {steps[progress]}")
        self.quest_progress[faction] += 1
        if self.quest_progress[faction] == len(steps):
            legendary = self.legendary_gear[faction]
            print(f"\n🌟 LEGENDARY GEAR OBTAINED: {legendary}!")
            player.inventory.append(legendary)
            player.increase_reputation(10)
            player.unlock_achievement("Questline Champion")

    # --- Town liberation & defense ---

    def liberate_town(self, player, town_name):
        owner = self.towns[town_name]
        if owner in ["Neutral", "Human"]:
            print("This town does not need liberation.")
            return
        print(f"\n⚔️ You attempt to liberate {town_name} from the {owner} faction!")
        power = self.faction_power[owner]
        enemy_hp = 50 + power * 10
        enemy_min = 5 + power
        enemy_max = 10 + power
        boss = Enemy(f"{owner} Champion", enemy_hp, enemy_min, enemy_max)
        battle = BattleSystem(player, boss, qte_word="fight")
        if battle.start_battle():
            print(f"\n🏰 {town_name} has been liberated!")
            self.towns[town_name] = "Human"
            self.faction_power[owner] = max(0, self.faction_power[owner] - 3)
            player.increase_reputation(5)
            player.npc_memory[town_name] = "They say you saved the town."
            self.town_rebuilding[town_name] = 3
            player.unlock_achievement("Town Savior")
        else:
            print(f"\n❌ You failed to liberate {town_name}.")
            player.decrease_reputation(3)
            player.npc_memory[town_name] = "They say you failed them."

    def defend_town(self, player):
        if not self.pending_defense:
            print("No town is currently under attack.")
            return
        town, faction = self.pending_defense
        print(f"\n⚔️ You rush to defend {town} from the {faction}!")
        power = self.faction_power[faction]
        enemy = Enemy(f"{faction} Warlord", 80 + power * 10, 8 + power, 12 + power)
        battle = BattleSystem(player, enemy, qte_word="fight")
        if battle.start_battle():
            print(f"\n🏰 You saved {town}!")
            self.town_prosperity[town] = min(100, self.town_prosperity[town] + 10)
            player.increase_reputation(5)
            player.npc_memory[town] = "They say you defended the town."
        else:
            print(f"\n❌ {town} has fallen.")
            self.towns[town] = faction
            player.decrease_reputation(5)
        self.pending_defense = None

    # --- Guilds ---

    def increase_guild_rep(self, guild, amount):
        g = self.guilds[guild]
        g["rep"] += amount
        if g["rep"] >= 20 and g["rank"] == 0:
            g["rank"] = 1
            print(f"You are now a {guild} Initiate!")
        elif g["rep"] >= 50 and g["rank"] == 1:
            g["rank"] = 2
            print(f"You are now a {guild} Veteran!")
        elif g["rep"] >= 100 and g["rank"] == 2:
            g["rank"] = 3
            print(f"You are now a {guild} Master!")
            player.unlock_achievement("Guild Master")

    def join_guild_war(self, player):
        if not self.guild_war_state:
            print("No guild war is happening.")
            return
        g1, g2 = self.guild_war_state
        print(f"\nWhich guild do you support?")
        print(f"1. {g1}")
        print(f"2. {g2}")
        choice = input("> ")
        chosen = g1 if choice == "1" else g2
        print(f"\nYou join the {chosen} Guild in battle!")
        enemy = Enemy(f"{chosen} Rival Champion", 120, 10, 16)
        battle = BattleSystem(player, enemy, qte_word="fight")
        if battle.start_battle():
            print(f"You helped the {chosen} Guild win the battle!")
            self.guilds[chosen]["rep"] += 10
            player.increase_reputation(5)
        else:
            print("You failed to turn the tide.")
            player.decrease_reputation(5)
        self.guild_war_state = None

    # --- Main story & endings ---

    def advance_main_story(self, player):
        if self.main_story_progress >= len(self.main_story_steps):
            print("The main story is complete.")
            return
        step = self.main_story_steps[self.main_story_progress]
        print(f"\n📜 MAIN STORY: {step}")
        if "chaos" in step.lower():
            for faction in self.faction_power:
                self.faction_power[faction] += 1
        if "final battle" in step.lower():
            print("\n🔥 A world boss emerges: The Harbinger of Ruin!")
            boss = Enemy("Harbinger of Ruin", 300, 15, 25)
            BattleSystem(player, boss, qte_word="fight").start_battle()
        self.main_story_progress += 1

    def check_for_ending(self, player):
        for faction, power in self.faction_power.items():
            if power >= 10 and self.quest_progress[faction] >= len(self.questlines[faction]):
                return f"{faction} Ending"
        if player.alignment >= 70:
            return "Good Ending"
        if player.alignment <= -70:
            return "Evil Ending"
        if (
            all(self.quest_progress[f] >= len(self.questlines[f]) for f in self.questlines) and
            self.main_story_progress >= len(self.main_story_steps) and
            player.all_achievements_complete() and
            all(self.towns[t] == "Human" for t in self.towns) and
            all(self.guilds[g]["rank"] == 3 for g in self.guilds) and
            -10 <= player.alignment <= 10
        ):
            return "True Ending"
        return None

    def unlock_new_game_plus(self, player):
        if self.check_for_ending(player) == "True Ending":
            print("\n🌟 NEW GAME+ UNLOCKED!")
            player.new_game_plus = True

    # --- World map UI ---

    def display_world_map(self):
        print("\n🌍 WORLD MAP")
        print("------------")
        for town in self.towns:
            owner = self.towns[town]
            econ = round(self.town_economy[town], 2)
            prosper = self.town_prosperity[town]
            print(f"{town}:")
            print(f"  Controlled by: {owner}")
            print(f"  Economy: x{econ}")
            print(f"  Prosperity: {prosper}/100\n")
