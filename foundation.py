class Foundation():
    champions = [
        {
            "name": "Ashe",
            "gender": "female",
            "role": "adc",
            "championCost": [450, "blueEssence"],
            "skins": [
                {
                    "name": "Sherwood Forest Ashe",
                    "skinCost": [520, "blackEssence"]
                },
                {
                    "name": "Woad Ashe",
                    "skinCost": [520, "blackEssence"]
                },
                {
                    "name": "Amethyst Ashe",
                    "skinCost": [975, "blackEssence"]
                },
                {
                    "name": "Marauder Ashe",
                    "skinCost": [750, "blackEssence"]
                },
                {
                    "name": "PROJECT: Ashe",
                    "skinCost": [1820, "blackEssence"]
                },
                {
                    "name": "Cosmic Queen Ashe",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "High Noon Ashe",
                    "skinCost": [1820, "blackEssence"]
                }
            ]
        },
        {
            "name": "Jhin",
            "gender": "male",
            "role": "adc",
            "championCost": [6300, "blueEssence"],
            "skins": [
                {
                    "name": "Blood Moon Jhin",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "High Noon Jhin",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "PROJECT: Jhin",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "Dark Cosmic Jhin",
                    "skinCost": [1820, "blackEssence"]
                }
            ]
        },
        {
            "name": "Nami",
            "gender": "female",
            "role": "support",
            "championCost": [4800, "blueEssence"],
            "skins": [
                {
                    "name": "Koi Nami",
                    "skinCost": [975, "blackEssence"]
                },
                {
                    "name": "River Spirit Nami",
                    "skinCost": [975, "blackEssence"]
                },
                {
                    "name": "Urf the Nami-tee",
                    "skinCost": [750, "blackEssence"]
                },
                {
                    "name": "Deep Sea Nami",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "Program Nami",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "Splendid Staff Nami",
                    "skinCost": [1350, "blackEssence"]
                }
            ]
        },
        {
            "name": "Pyke",
            "gender": "male",
            "role": "support",
            "championCost": [6300, "blueEssence"],
            "skins": [
                {
                    "name": "Sand Wraith Pyke",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "Blood Moon Pyke",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "PROJECT: Pyke",
                    "skinCost": [1820, "blackEssence"]
                }
            ]
        },
        {
            "name": "Neeko",
            "gender": "female",
            "role": "mid",
            "championCost": [6300, "blueEssence"],
            "skins": [
                {
                    "name": "Winter Wonder Neeko",
                    "skinCost": [1350, "blackEssence"]
                },
                {
                    "name": "Star Guardian Neeko",
                    "skinCost": [1350, "blackEssence"]
                }
            ]
        }
        # TODO: create entries for mid role
        # TODO: create entries for jungle role
        # TODO: create entries for top role
    ]
    skins = []

    def __init__(self):
        for champion in self.champions:
            for skin in champion["skins"]:
                self.skins.append(skin)
