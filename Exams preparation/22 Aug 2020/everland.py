from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumptions: {consumption:.2f}$."

    def pay(self):
        info = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                info.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= total_expenses
            else:
                self.rooms.remove(room)
                info.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(info)

    def status(self):
        result = ""
        result += f"Total population: {sum([members.members_count for members in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            for index, child in enumerate(room.children):
                result += f"--- Child {index + 1} monthly cost: {child.cost * 30:.2f}$\n"
            appliances = sum([appl.get_monthly_expense() for appl in room.appliances])
            result += f"--- Appliances monthly cost: {appliances:.2f}$\n"
        return result
