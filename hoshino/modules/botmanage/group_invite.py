import nonebot
#from nonebot import NoneBot
from nonebot import RequestSession, CommandSession, on_request, on_command
from hoshino import util

@on_request('group.invite')
async def handle_group_invite(session: RequestSession):
    if session.ctx['user_id'] in nonebot.get_bot().config.SUPERUSERS:
        await session.approve()
    else:
        await session.reject(reason='邀请入群请联系维护组')

# Nonebot版本不同，此部分仍在调试。
#
#@on_command('exitgroup', aliases=('退群', '关闭'), only_to_me=True)
##async def exitGroup(session: CommandSession):
#    if session.ctx['user_id'] in nonebot.get_bot().config.SUPERUSERS:
#        try:
#            group_id = session.current_arg_text.split()
#            await Bot.set_group_leave(group_id=group_id, is_dismiss=True)
#            await session.finish(f"↓ 框架消息\n已成功退出{group_id}。")
#        except Exception as e:
#            await session.send(f"↓ 框架消息\n退群过程中出现错误。\n请验证群号，如群号没有问题请反馈。\n[Exception]{e}")
#    else:
#        await session.finish("↓ 框架消息\n您的权限不足，无法退出。请联系管理员。")