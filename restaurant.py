class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)


