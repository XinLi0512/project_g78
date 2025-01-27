from django.db import models

class Sighting(models.Model):
    """Sighting data-structure"""

    uniqueSquirrelId = models.TextField(primary_key=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    hectare = models.TextField(null=True)
    shift = models.TextField(null=True)
    date = models.DateField(null=True)
    hectareSquirrelNumber = models.IntegerField(null=True)
    age = models.TextField(null=True)
    primaryFurColor = models.TextField(null=True)
    highlightFurColor = models.TextField(null=True)
    combinationOfPrimaryAndHighlightColor = models.TextField(null=True)
    colorNotes = models.TextField(null=True)
    location = models.TextField(null=True)
    aboveGroundSighterMeasurement = models.IntegerField(null=True)
    specificLocation = models.TextField(null=True)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    otherActivities = models.TextField(null=True)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tailFlags = models.BooleanField(null=True)
    tailTwitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runsFrom = models.BooleanField(null=True)
    otherInteractions = models.TextField(null=True)
    textOfLatAndLng = models.TextField(null=True)
    zipCodes = models.TextField(null=True)
    communityDistricts = models.IntegerField(null=True)
    boroughBoundaries = models.IntegerField(null=True)
    cityCouncilDistricts = models.IntegerField(null=True)
    policePrecincts = models.IntegerField(null=True)

# Create your models here.
