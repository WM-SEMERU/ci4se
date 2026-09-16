def process_directory(source, target, apikey, handler, overwrite=False):
    handler.on_start()
    attempts = defaultdict(lambda : 0)
    input_files = files_with_exts(source, suffix='.png')
    next_ = lambda : next(input_files, None)
    current_file = next_()
    response = None
    last_processed = None
    while current_file:
        output_file = target_path(source, target, current_file)
        if os.path.exists(output_file) and not overwrite:
            handler.on_skip(current_file, source=source)
            current_file = next_()
            continue
        try:
            handler.on_pre_item(current_file)
            last_processed = current_file
            response = _process_file(current_file, output_file, apikey)
            current_file = next_()
        except StopProcessing as e:
            response = e.response
            handler.on_stop(response.errmsg)
            break
        except RetryProcessing as e:
            response = e.response
            if attempts[current_file] < 9:
                handler.on_retry(current_file)
                time.sleep(TINYPNG_SLEEP_SEC)
                attempts[current_file] += 1
            else:
                current_file = next_()
        finally:
            handler.on_post_item(response, input_file=last_processed,
                source=source)
    handler.on_finish(output_dir=target)