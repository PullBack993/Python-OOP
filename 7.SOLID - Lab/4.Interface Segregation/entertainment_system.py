class Connector:
    def connect(self, other):
        pass


class HDMIConnector(Connector):
    pass


class PowerConnector(Connector):
    pass


class EthernetConnector(Connector):
    pass


class Television:
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerConnector()
        self.ethernet_connector = EthernetConnector()


class GameConsole:
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerConnector()
        self.ethernet_connector = EthernetConnector()


class Router:
    def __init__(self):
        self.ethernet_connector = EthernetConnector()


tv = Television()
game_console = GameConsole()
tv.hdmi_connector.connect(game_console.hdmi_connector)
