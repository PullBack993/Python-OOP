from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if self.available_capacity >= software.capacity_consumption and \
                self.available_memory >= software.memory_consumption:

            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])
