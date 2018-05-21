from django.db import models
from django.contrib.auth.models import AbstractUser

# Users
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_referee = models.BooleanField(default=False)
class Player(models.Model):
    # name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Coach(models.Model):
    # name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Referee(models.Model):
    # name
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Field(models.Model):
    # name
    name = models.CharField(max_length=128)
    # location
class Team(models.Model):
    # name
    name = models.CharField(max_length=128)
    # coach
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='coach')
    # players
    players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='players')
class Division(models.Model):
    # name
    name = models.CharField(max_length=128)
    # teams
    teams = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')
class Game(models.Model):
    # team1
    home_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='home_team')
    # team2
    away_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='away_team')
    # referees
    referees = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='referees')
    # time/date
    date = models.DateField()


