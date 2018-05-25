class player:
    def __init__(self, name, chips):
        self.__name = name
        self.__chips = chips

    def bet(self, chips):
        self.__chips -= chips