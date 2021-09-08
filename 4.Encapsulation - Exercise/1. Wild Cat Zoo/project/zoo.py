class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        elif self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.family_name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough space for animals"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.family_name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for 1.Worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.family_name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_sum_to_play = sum([s.salary for s in self.workers])
        if self.__budget > total_sum_to_play:
            left_budget = self.__budget - total_sum_to_play
            self.__budget = left_budget
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_to_tend = sum([a.get_needs() for a in self.animals])
        if self.__budget > total_sum_to_tend:
            left_budget = self.__budget - total_sum_to_tend
            self.__budget = left_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "{}".format('\n'.join([repr(t) for t in tigers])) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "{}".format('\n'.join([repr(c) for c in cheetahs])) + ""
        return result

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "{}".format('\n'.join([repr(k) for k in keepers])) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "{}".format('\n'.join([repr(c) for c in caretakers])) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "{}".format('\n'.join([repr(v) for v in vets])) + ""

        return result
