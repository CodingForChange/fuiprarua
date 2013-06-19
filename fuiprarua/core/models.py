from django.db import models

class Participantes(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    LOCAL_CHOICES = (
        ("Av. Paulista", "Avenida Paulista"),
        ("Largo da Batata", "Largo da Batata"),
        ("Praça da Sé", "Praça da Sé"),
        ("Teatro Municipal", "Teatro Municipal"),
    )

    sexo = models.CharField(max_length=1,
                            choices=SEXO_CHOICES)
    data = models.DateTimeField()
    local = models.CharField(max_length=50,
                            choices=LOCAL_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)