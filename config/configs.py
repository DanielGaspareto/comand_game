"""Game general configs."""


class ProjectConfigs:
    """General configs."""

    def __init__(self):
        """Class constructor."""

        self.pattern_sleep = 5
        self.character_dict = {
            '1': 'Warrior',
            '2': 'Wizard',
            '3': 'Archer'
        }
        self.type_dict = {
            '1': 'Fire',
            '2': 'Water',
            '3': 'Earth',
            '4': 'Wind'
        }
        self.status_dict = {
            'life': {
                'Warrior': 30,
                'Wizard': 20,
                'Archer': 15
            },
            'mp': {
                'Warrior': 15,
                'Wizard': 40,
                'Archer': 35
            },
            'damage': {
                'Warrior': 20,
                'Wizard': 10,
                'Archer': 35
            }
        }
