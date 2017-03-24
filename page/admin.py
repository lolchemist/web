from django.contrib import admin

from .models import Person, Activity,Workout_type, Workout, Food, Product

admin.site.register(Person)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Workout_type)
admin.site.register(Food)
admin.site.register(Product)
# Register your models here.
