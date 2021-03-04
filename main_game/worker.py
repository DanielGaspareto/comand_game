"""Base code."""

from config.configs import ProjectConfigs


class Worker:

    def __init__(self):
        super(Worker, self).__init__()
        self.config = ProjectConfigs()

    def _create_adventurous(self, nick) -> dict:
        """
        :param nick:
        :return:
        """
        raise NotImplemented

    def _in_game(self):
        """
        Load the game

        :return:
        """
        self._create_adventurous(nick=None)

    def run(self):
        """
        Star a game.

        :return:
        """
        while True:
            print("A new game has started !")
            self._in_game()
