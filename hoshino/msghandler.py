from hoshino import CanceledException, message_preprocessor, trigger
from hoshino.typing import CQEvent


@message_preprocessor
async def handle_message(bot, event: CQEvent, _):

    if event.detail_type != 'group':
        return

    for t in trigger.chain:
        sf = t.find_handler(event)
        if sf:
            trigger_name = t.__class__.__name__
            break

    if not sf:
        return  # triggered nothing.
    sf.sv.logger.info(f'信息号: {event.message_id} 触发了模块。 {sf.__name__} 模块信息： {trigger_name}.')

    if sf.only_to_me and not event['to_me']:
        return  # not to me, ignore.

    if not sf.sv._check_all(event):
        return  # permission denied.

    try:
        await sf.func(bot, event)
    except CanceledException:
        raise
    except Exception as e:
        sf.sv.logger.error(f'发生错误：{type(e)} / 在 {sf.__name__} 模块执行时发生了错误。信息号为： {event.message_id}.详细信息如下：')
        sf.sv.logger.exception(e)
    raise CanceledException(f'被 Hoshino 的 {trigger_name} 接收。')
