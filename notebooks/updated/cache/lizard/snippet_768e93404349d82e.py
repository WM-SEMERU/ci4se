def rerank(args: argparse.Namespace):
    reranker = Reranker(args.metric, args.return_score)
    with utils.smart_open(args.reference) as reference, utils.smart_open(args
        .hypotheses) as hypotheses:
        for i, (reference_line, hypothesis_line) in enumerate(zip(reference,
            hypotheses), 1):
            reference = reference_line.strip()
            hypotheses = json.loads(hypothesis_line.strip())
            utils.check_condition('translations' in hypotheses,
                "Reranking requires nbest JSON input with 'translations' key present."
                )
            num_hypotheses = len(hypotheses['translations'])
            if not num_hypotheses > 1:
                logger.info(
                    'Line %d contains %d hypotheses. Nothing to rerank.', i,
                    num_hypotheses)
                reranked_hypotheses = hypotheses
            else:
                reranked_hypotheses = reranker.rerank(hypotheses, reference)
            if args.output_best:
                if not num_hypotheses:
                    print()
                else:
                    print(reranked_hypotheses['translations'][0])
            else:
                print(json.dumps(reranked_hypotheses, sort_keys=True))