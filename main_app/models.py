from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from taggit.managers import TaggableManager

from custom_user.models import AbstractEmailUser

class User(AbstractEmailUser):
    name = models.TextField(null=True, blank=True)
    github_webhook_secret = models.TextField(blank=True, null=True)
    github_username = models.TextField(blank=True, null=True)
    activation_key = models.CharField(max_length=40, default='no_activation_key')
    key_expires = models.DateTimeField(default=datetime.now)
    seen_intro = models.BooleanField(default=False)

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

# SUMMARY SECTION
class Diary(BaseModel):
    date = models.DateField(default=datetime.now)
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    highlights = models.TextField()
    description = models.TextField()

# HEALTH SECTION
class Sleep(BaseModel):
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time))

class WeightExercise(BaseModel):
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    weight = models.IntegerField()
    reps = models.IntegerField()
    calories_burned = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('WeightExerciseType', on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class CardioExercise(BaseModel):
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    calories_burned = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('CardioExerciseType', on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class WeightExerciseType(BaseModel):
    name = models.TextField()

    def __str__(self):
        return self.name

        
class CardioExerciseType(BaseModel):
    name = models.TextField()

    def __str__(self):
        return self.name

class Food(BaseModel):
    date = models.DateField(default=datetime.now)
    eat_time = models.TimeField()
    name = models.TextField()
    location = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    calories = models.IntegerField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

class Toilet(BaseModel):
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    bristol = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], default = 4)

class Sex(BaseModel):
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField(blank = True, null = True)
    end_time = models.TimeField(blank = True, null = True)
    type = models.TextField()

class Period(BaseModel):
    date = models.DateField(default=datetime.now)
    period = models.BooleanField()

# PRODUCTIVITY SECTION
class Money(BaseModel):
    date = models.DateField(default=datetime.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.TextField()
    category = models.TextField()

class ToDo(BaseModel):
    # Status
    INCOMPLETE = 'IN'; WORKING = 'WO'; PARTIAL = 'PA'; COMPLETE = 'CO'; CANCELED = 'CA'; WAITING = 'SR'
    TODO_STATUS = ( (INCOMPLETE, 'Incomplete'), (WORKING, 'Working'), (PARTIAL, 'Partially Complete'),
        (COMPLETE, 'Complete'), (CANCELED, 'Canceled'), (WAITING, 'Waiting') )
    # Priority
    PRIORITY_HIGH = 1; PRIORITY_MEDIUM = 2; PRIORITY_LOW = 3
    PRIORITY_CHOICES = ( 
        (PRIORITY_HIGH, 'High Priority'), 
        (PRIORITY_MEDIUM, 'Medium Priority'), 
        (PRIORITY_LOW, 'Low Priority')
    )

    date = models.DateField(default=datetime.now)
    name = models.TextField()
    details = models.TextField(blank = True, null = True)
    pursuit = models.ForeignKey('Pursuit', blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=2, choices=TODO_STATUS, default=INCOMPLETE)
    waiting_on = models.TextField(blank = True, null = True)
    project = models.ForeignKey('Project', blank = True, null = True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(default=datetime.now)
    start_time = models.DateTimeField(blank = True, null = True)
    finish_time = models.DateTimeField(blank = True, null = True)
    duration = models.DurationField(blank = True, null = True)
    rank = models.FloatField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
    due_date = models.DateField(blank = True, null = True)

    def __str__(self):
        return self.name

class Pursuit(BaseModel):
    name = models.TextField()
    icon = models.CharField(max_length=2)

    def __str__(self):
        return self.icon + ' ' + self.name

class PursuitProgress(BaseModel):
    date = models.DateField(default=datetime.now)
    pursuit = models.ForeignKey('Pursuit', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.pursuit.icon + ' ' + self.description

class Project(BaseModel):
    name = models.TextField()
    description = models.TextField()
    pursuit = models.ForeignKey('Pursuit', blank=True, null=True, on_delete=models.SET_NULL)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Learning(BaseModel):
    date = models.DateField(default=datetime.now)
    summary = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.summary

class Study(BaseModel):
    date = models.DateField(default=datetime.now)
    name = models.TextField(blank = True, null = True)
    correct_records = models.IntegerField(blank = True, null = True)
    quiz = models.ForeignKey('Quiz', blank = True, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quiz(BaseModel):
    name = models.TextField()
    url = models.TextField()
    total_records = models.IntegerField()
    
    def __str__(self):
        return self.name

# ART SECTION
class Literature(BaseModel):
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    author = models.TextField()
    up_to_page = models.IntegerField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)
    type = models.TextField()

    def __str__(self):
        return self.title

class Film(BaseModel):
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    director = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

class Television(BaseModel):
    date = models.DateField(default=datetime.now)
    series = models.TextField()
    episode = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.series

class VideoGame(BaseModel):
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    console = models.TextField()
    developer = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

class Music(BaseModel):
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    artist = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

class BoardGame(BaseModel):
    date = models.DateField(default=datetime.now)
    title = models.TextField()
    creator = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

class Podcast(BaseModel):
    date = models.DateField(default=datetime.now)
    series = models.TextField()
    episode = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.series

class Beer(BaseModel):
    date = models.DateField(default=datetime.now)
    name = models.TextField()
    brewery = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

class Wine(BaseModel):
    date = models.DateField(default=datetime.now)
    name = models.TextField()
    vineyard = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

class Cheese(BaseModel):
    date = models.DateField(default=datetime.now)
    name = models.TextField()
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

# DISPLAY

class ModuleButton(BaseModel):
    # IconSource
    UNICODE = 'UN'; FONTAWESOME = 'FA'
    ICON_SOURCE = ( (UNICODE, 'Unicode'), (FONTAWESOME, 'FontAwesome') )

    name = models.TextField()
    url_name = models.TextField()
    background_color = models.TextField(default='#8bacbd')
    icon_source = models.CharField(max_length=2, choices=ICON_SOURCE, default=FONTAWESOME)
    icon_unicode = models.CharField(max_length=2, blank=True, null=True)
    icon_font_awesome = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=True)
    category = models.TextField(blank=True, null=True)
    background_color_complete = models.TextField(default='#6e8a99')
    
    def __str__(self):
        return self.name

# GROCERIES

class FoodItem(BaseModel):
    name = models.TextField()
    serving_size_qty = models.DecimalField(blank = True, null = True,max_digits=5, decimal_places=2)
    serving_size_unit = models.TextField()
    barcode = models.TextField(blank = True, null = True)

    # Nutrition
    calories = models.IntegerField(blank=True, null=True)
    total_fat = models.DecimalField(blank = True, null = True,max_digits=5, decimal_places=1)
    saturated_fat = models.DecimalField(blank = True, null = True,max_digits=5, decimal_places=1)
    trans_fat = models.DecimalField(blank = True, null = True,max_digits=5, decimal_places=1)
    cholesterol = models.IntegerField(blank = True, null = True)
    sodium = models.IntegerField(blank = True, null = True)
    potassium = models.IntegerField(blank = True, null = True)
    total_carbs = models.IntegerField(blank = True, null = True)
    dietary_fiber = models.IntegerField(blank = True, null = True)
    total_sugars = models.IntegerField(blank = True, null = True)
    added_sugars = models.IntegerField(blank = True, null = True)
    protein = models.IntegerField(blank = True, null = True)
    vitamin_a = models.IntegerField(blank = True, null = True)
    vitamin_c = models.IntegerField(blank = True, null = True)
    vitamin_d = models.IntegerField(blank = True, null = True)
    vitamin_e = models.IntegerField(blank = True, null = True)
    vitamin_k = models.IntegerField(blank = True, null = True)
    vitamin_b1 = models.IntegerField(blank = True, null = True)
    vitamin_b2 = models.IntegerField(blank = True, null = True)
    vitamin_b3 = models.IntegerField(blank = True, null = True)
    vitamin_b5 = models.IntegerField(blank = True, null = True)
    vitamin_b6 = models.IntegerField(blank = True, null = True)
    vitamin_b9 = models.IntegerField(blank = True, null = True)
    vitamin_b12 = models.IntegerField(blank = True, null = True)
    biotin = models.IntegerField(blank = True, null = True)
    choline = models.IntegerField(blank = True, null = True)
    calcium = models.IntegerField(blank = True, null = True)
    chromium = models.IntegerField(blank = True, null = True)
    copper = models.IntegerField(blank = True, null = True)
    fluoride = models.IntegerField(blank = True, null = True)
    iodine = models.IntegerField(blank = True, null = True)
    iron = models.IntegerField(blank = True, null = True)
    magnesium = models.IntegerField(blank = True, null = True)
    manganese = models.IntegerField(blank = True, null = True)
    molybdenum = models.IntegerField(blank = True, null = True)
    phosphorus = models.IntegerField(blank = True, null = True)
    selenium = models.IntegerField(blank = True, null = True)
    zinc = models.IntegerField(blank = True, null = True)
    potassium = models.IntegerField(blank = True, null = True)
    sodium = models.IntegerField(blank = True, null = True)
    chloride = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name

class Recipe(BaseModel):
    name = models.TextField()
    ingredients = models.ManyToManyField(FoodItem, through='RecipeIngredients')
    url = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class RecipeIngredients(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    item_qty = models.DecimalField(max_digits=5, decimal_places=2)
    item_unit = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

class GroceryPurchase(BaseModel):
    date = models.DateField(default=datetime.now)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    store = models.TextField(blank=True, null=True)
    receipt_name = models.TextField(blank=True, null=True)

    serving_count = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    unit_pieces = models.IntegerField(blank=True, null=True)
    unit_lbs = models.DecimalField(blank=True, null=True,max_digits=5, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    discount_per_unit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    qty = models.IntegerField()

    def __str__(self):
        return self.food_item.name

class FoodStock(BaseModel):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    serving_count = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    qty_num = models.IntegerField()
    qty_lbs = models.DecimalField(max_digits=5, decimal_places=2)

class Cooking(BaseModel):
    date = models.DateField(default=datetime.now)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null = True)

class Meal(BaseModel):
    date = models.DateField(default=datetime.now)
    foods = models.ManyToManyField(FoodItem)
    recipes = models.ManyToManyField(Recipe)
    eat_time = models.TimeField()
    location = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], default = 3, max_digits=2, decimal_places=1)

class Travel(BaseModel):
    date = models.DateField(default=datetime.now)
    name = models.TextField()
    location_type = models.TextField()
    latitude = models.DecimalField(max_digits=16, decimal_places=13)
    longitude = models.DecimalField(max_digits=16, decimal_places=13)

class FilmWish(BaseModel):
    title = models.TextField()
    director = models.TextField(blank=True, null=True)
    fulfillment = models.ForeignKey(Film, blank=True, null=True, on_delete=models.CASCADE) 

class BoardGameWish(BaseModel):
    title = models.TextField()
    creator = models.TextField(blank=True, null=True)
    fulfillment = models.ForeignKey(BoardGame, blank=True, null=True, on_delete=models.CASCADE) 

class LiteratureWish(BaseModel):
    title = models.TextField()
    author = models.TextField(blank=True, null=True)
    fulfillment = models.ForeignKey(Literature, blank=True, null=True, on_delete=models.CASCADE) 