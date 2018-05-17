from django.db import models

# Users
class Player(models.Model):
    # name
    # team
class Coach(models.Model):
    # name
class Referee(models.Model):
    # name

class Division(models.Model):
    # name
    name = models.CharField(max_length=128)
    # teams
    teams = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')
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
class Game(models.Model):
    # team1
    home_team = models.OneToOneField(Team, on_delete=models.CASCADE)
    # team2
    away_team = models.OneToOneField(Team, on_delete=models.CASCADE)
    # referees
    referees = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='referees')
    # time/date
    date = models.DateField()


