from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model


class Test(Model, ConvertedModel):
    name = fields.CharField(max_length=255, description='Название поста')
    text = fields.TextField(description='Текст поста')

    class Meta:
        table = "test"

    def __str__(self) -> str:
        return self.name


class ScheduleBus(Model, ConvertedModel):
    title = fields.CharField(max_length=150, default='1')
    work_days = fields.TextField(description='Рабочие дни')
    weekend = fields.TextField(description='Выходные')
    class Meta:
        table = "schedule"

    def __str__(self) -> str:
        return self.title


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.test_app.models"],
        app_label="test_app",
        _init_relations=False,
    )
