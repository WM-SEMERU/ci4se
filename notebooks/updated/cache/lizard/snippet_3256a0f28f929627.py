def insert_seperator_results(results):
    sepbench = BenchmarkResult(*[(' ' * w) for w in COLUMN_WIDTHS])
    last_bm = None
    for r in results:
        if last_bm is None:
            last_bm = r.benchmark
        elif last_bm != r.benchmark:
            yield sepbench
            last_bm = r.benchmark
        yield r