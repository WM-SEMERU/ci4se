def check_shutdown_flag(self):
    if self.shutdown_requested:
        tornado.ioloop.IOLoop.instance().stop()
        print('web server stopped.')