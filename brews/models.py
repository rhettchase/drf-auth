from django.db import models
from django.contrib.auth import get_user_model

class Brew(models.Model):
    IPA = "IPA"
    BROWN_ALE = "BR"
    PILSNER = "PL"
    SOUR = "SR"
    PALE_ALE = "PA"
    STOUT = "ST"
    WHITE_ALE = "WH"
    
    BREW_TYPE_CHOICES = {
        IPA: "IPA",
        BROWN_ALE: "Brown Ale",
        PILSNER: "Pilsner",
        SOUR: "Sour",
        PALE_ALE: "Pale Ale",
        STOUT: "Stout",
        WHITE_ALE: "White Ale"
    }
    
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    brew_type = models.CharField(
        max_length=3,
        choices=BREW_TYPE_CHOICES,
        default=IPA
    )
    brewery = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
