def __interrupt_search(self):
    if self.__search_worker_thread:
        self.__search_worker_thread.quit()
        self.__search_worker_thread.wait()
        self.__container.engine.stop_processing(warning=False)