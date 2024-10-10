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
    sf.sv.logger.info(f'��Ϣ��: {event.message_id} ������ģ�顣 {sf.__name__} ģ����Ϣ�� {trigger_name}.')

    if sf.only_to_me and not event['to_me']:
        return  # not to me, ignore.

    if not sf.sv._check_all(event):
        return  # permission denied.

    try:
        await sf.func(bot, event)
    except CanceledException:
        raise
    except Exception as e:
        sf.sv.logger.error(f'��������{type(e)} / �� {sf.__name__} ģ��ִ��ʱ�����˴�����Ϣ��Ϊ�� {event.message_id}.��ϸ��Ϣ���£�')
        sf.sv.logger.exception(e)
    raise CanceledException(f'�� Hoshino �� {trigger_name} ���ա�')
