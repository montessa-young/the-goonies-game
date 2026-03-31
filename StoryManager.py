from BattleSystem import BattleSystem
from NPC import Enemy


class StoryState:
    def __init__(self):
        self.achievements = set()
        self.boss_gear = set()
        self.lost_to_sonic = False

    def add_achievement(self, key):
        self.achievements.add(key)

    def add_gear(self, key):
        self.boss_gear.add(key)


def fight_boss(player, enemy, story, qte_word, gear_name=None, achievement_key=None):
    battle = BattleSystem(player, enemy, qte_word=qte_word)
    result = battle.start_battle()

    if result:
        if achievement_key:
            story.add_achievement(achievement_key)
        if gear_name:
            story.add_gear(gear_name)
    return result


def run_story(player, story):
    print("\n--- STORY: MJ INTRO ---")
    mj = Enemy("MJ", 50, 6, 10)
    if not fight_boss(player, mj, story, qte_word="dance", gear_name="MJ_GEAR",
                      achievement_key="DEFEATED_MJ"):
        story.add_achievement("ENDING_MJ_KILLED_YOU")
        return False

    print("\n--- STORY: THUGS ---")
    for i in range(2):
        thug = Enemy("Lvl 5 Thug", 40, 5, 9)
        fight_boss(player, thug, story, qte_word="fight", gear_name=f"THUG_GEAR_{i+1}")

    print("\nDroyd George and Rick Astley appear!")
    droyd = Enemy("Droyd George", 60, 7, 12)
    if not fight_boss(player, droyd, story, qte_word="laser",
                      gear_name="DROYD_GEAR", achievement_key="DEFEATED_DROYD"):
        story.add_achievement("ENDING_DROYD_KILLED_YOU")
        return False

    rick = Enemy("Rick Astley", 70, 8, 13)
    if not fight_boss(player, rick, story, qte_word="never",
                      gear_name="RICK_GEAR", achievement_key="DEFEATED_RICK"):
        story.add_achievement("ENDING_RICK_KILLED_YOU")
        return False

    print("\nTrump appears and heals you, giving you 100 gold.")
    player.hp = player.max_hp
    player.gold += 100
    story.add_achievement("TRUMP_HELPED_YOU")

    print("\n--- STORY: MARIO ---")
    mario = Enemy("Mario", 90, 10, 15)
    mario_result = fight_boss(player, mario, story, qte_word="jump",
                              gear_name="MARIO_GEAR", achievement_key="DEFEATED_MARIO")
    if not mario_result:
        story.add_achievement("ENDING_1_MARIO_KILLED_YOU")
        return False
    else:
        story.add_achievement("ENDING_2_YOU_KILLED_MARIO")

    print("\n--- STORY: SONIC ---")
    sonic = Enemy("Sonic", 120, 12, 18)
    sonic_result = fight_boss(player, sonic, story, qte_word="speed",
                              gear_name="SONIC_GEAR", achievement_key="DEFEATED_SONIC")
    if not sonic_result:
        story.lost_to_sonic = True
        story.add_achievement("ENDING_3_SONIC_KILLED_YOU")
        return False
    else:
        story.add_achievement("ENDING_4_YOU_KILLED_SONIC")

    if len(story.boss_gear) >= 5:
        story.add_achievement("SECRET_ENDING_ALL_BOSS_GEAR")

    if player.gold >= 500:
        story.add_achievement("ENDING_5_RICH")

    if "DEFEATED_MARIO" in story.achievements and "DEFEATED_SONIC" in story.achievements:
        story.add_achievement("ENDING_RULER_OF_ALL")

    print("\nStory segment complete. Achievements updated.")
    return True
