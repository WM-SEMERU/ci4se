def start_dut_thread(self):
    if Dut._th is None:
        Dut._run = True
        Dut._sem = Semaphore(0)
        Dut._signalled_duts = deque()
        Dut._logger = LogManager.get_bench_logger('Dut')
        Dut._th = Thread(target=Dut.run, name='DutThread')
        Dut._th.daemon = True
        Dut._th.start()