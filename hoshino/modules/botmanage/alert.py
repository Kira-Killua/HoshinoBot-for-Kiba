from nonebot import on_notice, NoticeSession

@on_notice('group_decrease.kick_me')
async def kick_me_alert(session: NoticeSession):
    group_id = session.event.group_id
    operator_id = session.event.operator_id
    coffee = session.bot.config.SUPERUSERS[0]
    await session.bot.send_private_msg(self_id=session.event.self_id, user_id=coffee, message=f'↓框架消息:\n管理员请注意：Bot被操作者{operator_id}踢出群，群ID是{group_id}')
