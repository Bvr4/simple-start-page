from django.db import models

class Ligne(models.Model):
    ligne_id = models.AutoField(primary_key=True)
    emplacement = models.IntegerField()

    # crée une ligne par défaut si elle n'existe pas
    # @classmethod
    # def get_default_ligne(cls) -> "Ligne":
    #     ligne, _ = cls.objects.get_or_create(emplacement=0)
    #     return ligne
    
class Lien(models.Model):
    nom = models.CharField(max_length=40)
    url = models.TextField()
    emplacement = models.IntegerField()
    id_ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
        
    # permet d'avoir le nom visible dans l'interface d'admin django
    def __str__(self) -> str:
        return self.nom