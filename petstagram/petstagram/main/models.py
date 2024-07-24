from datetime import datetime
from django.contrib.auth.models import User

from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main.validators import only_letters_validator, MinDateValidator, MaxDateValidator


# Create your models here.
class Profile(models.Model):
    # Constants
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # ^ same as v
    # GENDERS = [
    #     ('Male',  'Male',),
    #     ('Female', 'Female',),
    #     ('Do not show', 'Do not show',),
    # ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
            # always_valid('asd')
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    picture = models.URLField(max_length=200)

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    NAME_MAX_LENGTH = 30

    # MIN_DATE = datetime.date(1920, 1, 1)

    # Fields(Columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        if self.date_of_birth:
            return datetime.now().year - self.date_of_birth.year
        return None

    def __str__(self):
        return f'{self.name} ({self.type})'


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size,
        )
    )
    tagged_pets = models.ManyToManyField(Pet)

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
