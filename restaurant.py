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


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def add_review(self, review):
        self.reviews.append(review)

    def reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews


# User input
def main():
    customer_name = input("First name: ")
    customer_family_name = input("Last name: ")
    restaurant_name = input("Restaurant's name: ")
    rating = int(input("Rating (1-15): "))

    customer = Customer(customer_name, customer_family_name)
    restaurant = Restaurant(restaurant_name)
    customer.add_review(restaurant, rating)

    print("Review added!")
