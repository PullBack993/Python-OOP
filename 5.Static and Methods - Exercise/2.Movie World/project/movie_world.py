from project.customer import Customer


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []  # list of Customer !
        self.dvds = []  # list of DVD objects !

    def __repr__(self):
        result = '\n'.join([repr(c) for c in self.customers])
        result += '\n' + '\n'.join([repr(b) for b in self.dvds])
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            return f"{customer.family_name} has already rented {dvd.family_name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if dvd.age_restriction > customer.age:
            return f"{customer.family_name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.family_name} has successfully rented {dvd.family_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.family_name} has successfully returned {dvd.family_name}"
        return f"{customer.family_name} does not have that DVD"
