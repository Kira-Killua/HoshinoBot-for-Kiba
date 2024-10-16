from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

TOP_MANUAL = '''
HoshinoBot for Kiba Ver 1.01
Based on HoshinoBot 2.0-RIP. Powered by Ice9Coffee.
Modified by Kira.

- 使用说明 -

此机器框架并非HoshinoBot官方框架，仅为支持KibaNew运行。多数功能已被砍掉。
发送方括号[]内的关键词即可触发
※功能采取模块化管理，群管理可控制开关

[lssv] 查看当前功能模块的开关状态（群管理限定）
[来杯咖啡] 联系维护组。（非Kira，魔改部分请联系Kira而不是此指令）
[帮助maimaiDX] 移步查看KibaNew（Maimai DX 相关）指令。

------
※服务器运行及开发维护需要成本，赞助支持请私戳作者
※您的支持是本bot更新维护的动力
※※请注意使用频率，您的滥用可能会导致bot账号被封禁
'''.strip()

def gen_bundle_manual(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible:
            spit_line = '=' * max(0, 18 - len(sv.name))
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name} {spit_line}")
            if sv.help:
                manual.append(sv.help)
    return '\n'.join(manual)


@sv.on_prefix(('help', '帮助', '幫助'))
async def send_help(bot, ev: CQEvent):
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    if not bundle_name:
        await bot.send(ev, TOP_MANUAL)
    elif bundle_name in bundles:
        msg = gen_bundle_manual(bundle_name, bundles[bundle_name], ev.group_id)
        await bot.send(ev, msg)
    # else: ignore
