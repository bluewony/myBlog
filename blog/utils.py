from django.db.models import Model, Manager

class BaseModel(Model):
    class Meta: abstract = True
    obj = objects = Manager()

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.save()
