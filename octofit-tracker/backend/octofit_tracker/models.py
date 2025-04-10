from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    ...

class Team(models.Model):
    name = models.CharField(max_length=100)
    ...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    ...