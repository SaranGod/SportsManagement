from django.db import models
from django.contrib.auth.models import User

class Admin_model(models.Model):
    GameName    =   models.CharField(max_length=50)
    Referee     =   models.CharField(max_length=50)
    Owner       =   models.ForeignKey(User, on_delete=models.CASCADE)
class player(models.Model):
    id          =       models.DecimalField(decimal_places=0,max_digits=20, primary_key=True)
    name        =       models.CharField(max_length=50)
class Owner_model(models.Model):
    username      =       models.ForeignKey(User, unique=False, on_delete=models.CASCADE, null=True)
    sport         =       models.CharField(max_length=50, null=True)
    player1       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player1', blank=True, null=True)
    player2       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player2', blank=True, null=True)
    player3       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player3', blank=True, null=True)
    player4       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player4', blank=True, null=True)
    player5       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player5', blank=True, null=True)
    player6       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player6', blank=True, null=True)
    player7       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player7', blank=True, null=True)
    player8       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player8', blank=True, null=True)
    player9       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player9', blank=True, null=True)
    player10       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player10', blank=True, null=True)
    player11     =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player11', blank=True, null=True)
    player12      =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player12', blank=True, null=True)
    player13      =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='player13', blank=True, null=True) 
    playerb1       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb1', blank=True, null=True)
    playerb2       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb2', blank=True, null=True)
    playerb3       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb3', blank=True, null=True)
    playerb4       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb4', blank=True, null=True)
    playerb5       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb5', blank=True, null=True)
    playerb6       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb6', blank=True, null=True)
    playerb7       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb7', blank=True, null=True)
    playerb8       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb8', blank=True, null=True)
    playerb9       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb9', blank=True, null=True)
    playerb10       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb10', blank=True, null=True)
    playerb11     =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb11', blank=True, null=True)
    playerb12      =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb12', blank=True, null=True)
    playerb13      =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='playerb13', blank=True, null=True) 
    round1_date   =       models.DateField()
    round2_date   =       models.DateField()
    round3_date   =       models.DateField()
    winner        =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='winner', blank=True)
    runner       =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='runner', blank=True)
    runner2     =       models.ForeignKey(player, on_delete=models.CASCADE, related_name='runner2', blank=True)
# Create your models here.