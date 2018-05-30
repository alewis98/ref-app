from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# Managers
class UserProfileManager(models.Manager):

    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()

# Users
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    phone_number = models.CharField(max_length=9, null=True, blank=True)
    address = models.CharField(max_length=240, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_referee = models.BooleanField(default=False)

    # override objects with manager
    objects = UserProfileManager()

    def __str__(self):
        return self.user.__str__()
    
    def to_string(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

# Signal to create UserProfile when a new User is created
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        user_profile = UserProfile.objects.create(user=user)
        if user.is_staff:
            user_profile.is_admin = True
            user_profile.save()

post_save.connect(create_profile, sender=User)

class Player(models.Model):
    # name
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    number = models.IntegerField(default=8, validators=[MaxValueValidator(99), MinValueValidator(0)])
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    def __str__(self):
        return self.user.to_string()

class Coach(models.Model):
    # name
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.to_string()

class Referee(models.Model):
    # name
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    grade = models.IntegerField(default=8, validators=[MaxValueValidator(9), MinValueValidator(1)])
    years_experience = models.IntegerField(default=0)
    is_certified = models.BooleanField(default=True)
 
    def __str__(self):
        return self.user.to_string()

class Field(models.Model):
    # name
    name = models.CharField(max_length=128)
    # location
class Team(models.Model):
    # name
    name = models.CharField(max_length=128)
    # color
    color = models.CharField(max_length=20, null=True, blank=True)
    # coach
    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING, related_name='coach', null=True, blank=True)
    # assistant coach
    assistant_coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING, related_name='assistant_coach', null=True, blank=True)
    # players
    players = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='players', null=True, blank=True)

    def __str__(self):
        if self.color is not None:
            return str(self.name) + " (" + str(self.color) + ")"
        return str(self.name)

class Division(models.Model):
    # name
    name = models.CharField(max_length=128)
    # teams
    teams = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='teams', null=True, blank=True)
class Game(models.Model):
    # team1
    home_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='home_team')
    # team2
    away_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='away_team')
    # referees
    referees = models.ForeignKey(Referee, on_delete=models.DO_NOTHING, related_name='referees', null=True, blank=True)
    # time/date
    date = models.DateTimeField()
    # field
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, related_name='field', null=True, blank=True)

    # @property
    # def get_field(self):
    #     if self.field is not None:
    #         return 