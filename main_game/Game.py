"""D&D on python!!!"""

from main_game.worker import Worker
from time import sleep


class Construct(Worker):
    """Construct class"""

    def __init__(self):
        """Class constructor."""
        super(Construct, self).__init__()
        self.time_to_wait = self.config.pattern_sleep
        self.class_chose = self.config.character_dict
        self.element_choice = self.config.type_dict
        self.balance_dict = self.config.status_dict

    def _create_adventurous(self, nick: str) -> dict:
        """
        Create a first person.

        :return: characteristics of Character.
        """
        character = {}
        class_person = str
        element_person = str

        print(f"Welcome {nick}!")
        print(self.class_chose)
        primary_chose = input("First, tell your primary class: ")
        # primary_chose = '1'  # Debug only
        for select_class in self.class_chose:
            if select_class == primary_chose:
                class_person = self.class_chose.get(select_class)

        print(self.element_choice)
        secondary_chose = input("Now, chose you secondary class: ")
        # secondary_chose = '1'  # Debug only
        for select_type in self.element_choice:
            if select_type == secondary_chose:
                element_person = self.element_choice.get(select_type)

        character[class_person] = element_person

        return character

    def _status(self, key: str, value: str):
        """
        Get a character and balance your status.

        :param key,value:
        :return:
        """
        # TODO MELHORAR ESSE CÓDIGO AQUI, MUITA REPETIÇÃO
        balanced_character = {key: value}

        for balance_key, balance_value in self.balance_dict.items():
            if balance_key == 'life':
                for _ in balance_value:
                    add = balance_value.get(key)
                    balanced_character['Life'] = add

            elif balance_key == 'mp':
                for _ in balance_value:
                    add = balance_value.get(key)
                    balanced_character['MP'] = add

            elif balance_key == 'damage':
                for _ in balance_value:
                    add = balance_value.get(key)
                    balanced_character['Damage'] = add

        return balanced_character

    def _in_game(self):
        """
        Load the game.

        :return:
        """
        # Create an character
        print("Hello adventurous, first you do make a character")
        nick_name = input("Please, tell me you nick name: ")
        person = self._create_adventurous(nick=nick_name)  # nick_name

        # Balance character status
        print('We are generating your status ...')
        for key, value in person.items():
            balanced_character = self._status(key=key, value=value)
            print('Add you tipe for this balance', balanced_character, '...')
        sleep(self.time_to_wait)
