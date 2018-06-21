# coding: utf-8
from wxpy import *

# 初始化机器人，扫码登陆，在命令行上登录console_qr参数必须设置为True
# 因为在命令行登录不会弹出二维码图片，只会在命令行上直接生成二维码
bot = Bot(console_qr=True)


# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print('msg:' + str(msg))
    articles = msg.articles
    if articles is not None:
        for article in articles:
            print('title:' + str(article.title))
            print('summary:' + str(article.summary))
            print('url:' + str(article.url))
            print('cover:' + str(article.cover))


if __name__ == '__main__':
    # 或者仅仅堵塞线程
    bot.join()
