#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : tornado_study.py
# @Description:
# @Time       : 2020-2-10 下午 1:54
# @Author     : Hou

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
     tornado的Web程序会将web程序的URL或URL范式映射到tornado.web.RequestHandler的子类上,在子类中定影
     定义get()或post()方法，用以处理不同的HTTP请求。
    """
    def get(self):
        self.write("In the beginning was the Word, "
                   "and the Word was the God, "
                   "and the Word was God")


def make_app():
    return tornado.web.Application([
        (r"/",MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
