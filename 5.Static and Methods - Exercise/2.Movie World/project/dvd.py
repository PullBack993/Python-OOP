NUM_TO_STR_MOTH = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
                   8: "Avgust", 9: "September", 10: "October", 11: "November", 12: "December"}


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}." \
               f" Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id, name, data, age_restriction):
        day, month, year = data.split(".")
        year = int(year)
        month = NUM_TO_STR_MOTH[int(month)]
        return cls(name, id, year, month, age_restriction)
