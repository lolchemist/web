from django.core.management.base import BaseCommand, CommandError
from photopacks.models import Person, Product, Food, Train, Activity
from django.db import connection
from random import randint, choice
from timeit import default_timer

names_list = ["Alice", "Mark", "Broderick", "Aberforth", "Andromeda", "Antioch", "Ariana", "Bane", "Bathilda", "Bartemius", "Dedalus", "Dolores"]
surnames_list = ["Pentus", "Raag", "Pedaru", "Roosnurm", "Ojala", "Tali", "Hinrikus","Kanepi"]
activity_list = ["Walking", "Roller skating", "Bicycling", "Aerobic dancing", "Yoga", "Gymnastics","Step aerobics"]
food_list = ["Bedfordshire clanger", "Bangers and mash", "Chicken tikka masala", "Cobbler",  "Beef", "Wellington"]
product_list = ["Wheat", "Rye", "Oat", "Corn", "Rice","Shrimp", "Crab", "Oysters","Milk", "Yogurt", "Cream", "Sour cream", "Butter"]


class Command(BaseCommand)
    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = options['number']
        bulk_people = [] 
        bulk_products = []
        bulk_food = []
        bulk_trains = []
        bulk_activities = []
        
        bulk_people = [Person(
            name = random.choice(names_list),
            surname = random.choice(surnames_list),
            sex = random.choice(['F', 'M']),
            age = random.randint(13, 86)
            ) for i in range(n)]
        Person.object.bulk_create(bulk_people)
       
    
        bulk_products = [Product(
            name = random.choice(product_list_list),
            prod_ccal = random.randint([29,700]),
            prod_weigth = random.randint(10, 800)
            ) for i in range(n)]
        Product.object.bulk_create(bulk_products)
    
        bulk_food = [Food(
            name = random.choice(food_list),
            ingredients = random.sample(product_list, randint(1, 10)
            ) for i in range(n)]
        Food.object.bulk_create(bulk_products)



        for _ in range (number):
            person = generate_person()
            bulk_people.append(person)
        
        number_of_activities = number* randint(min(6, len(activity_list)), min(9, len(activity_list))    
        
                
        for _ in range (number_of_activities):
            activity = generate_activity()
            bulk_activities.append(activity)
                                    
        number_of_products = number * randint(10, 30)
        
        for _ in range (number_of_products):
            product = generate_product()
            bulk_products.append(product)
    

        number_of_food = number* randint(4, 10)
            
        for _ in range (number_of_food):
            food = generate_food()
            bulk_food.append(food)
        
        number_of_trains = number*randint(10, 30)
            
        for _ in range (number_of_trains):
            train = generate_train()
            bulk_trains.append(train)



def generate_person():
    return Person(
    name = choice(names_list),
    surname = choice(surnames_list),
    sex = choice(['F', 'M']),
    age = randint(13, 86),
    )

