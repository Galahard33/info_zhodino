from typing import Tuple, List

from . import models


async def get_item() -> List[models.Test]:
    return await models.Test.all()


async def get_text_item(item_id) -> models.Test:
    item2 = await models.Test.get(id=item_id)
    return await item2


async def get_schedule() -> List[models.ScheduleBus]:
    schedule = models.ScheduleBus.all()
    return await schedule


async def get_text_schedule(id, b) -> models.ScheduleBus:
    item = await models.ScheduleBus.get(id=id)
    if b==1:
        item2=item.work_days
        return  item2
    elif b==2:
        item2=item.weekend
        return item2