import hoshino
import asyncio
import sys

bot = hoshino.init()
app = bot.asgi

if __name__ == '__main__':
    try:
        print("Hoshino Framework for Kiba\nModified by Kira.\n正在启动......")
        bot.run(use_reloader=False, loop=asyncio.get_event_loop())
    except KeyboardInterrupt:
        print("检测到用户中断。正在退出Bot运行......")
        sys.exit(0)