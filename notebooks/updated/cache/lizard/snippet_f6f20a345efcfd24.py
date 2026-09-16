def wait_for_all(self, objects, timeout=120):
    start = time.time()
    while True:
        all_exist = True
        for obj in objects:
            if not obj.exists():
                all_exist = False
                break
        if all_exist:
            return
        if time.time() - start > timeout:
            raise PocoTargetTimeout('all to appear', objects)
        self.sleep_for_polling_interval()