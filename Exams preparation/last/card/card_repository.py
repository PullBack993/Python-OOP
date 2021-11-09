from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card: Card):
        if any(p.name == card.name for p in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        crd = self.find(card)
        self.cards.remove(crd)

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
