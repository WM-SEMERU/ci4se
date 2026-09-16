def detect_index_renamings(self, table_differences):
    rename_candidates = OrderedDict()
    for added_index_name, added_index in table_differences.added_indexes.items(
        ):
        for removed_index in table_differences.removed_indexes.values():
            if not self.diff_index(added_index, removed_index):
                if added_index.get_name() not in rename_candidates:
                    rename_candidates[added_index.get_name()] = []
                rename_candidates[added_index.get_name()].append((
                    removed_index, added_index, added_index_name))
    for candidate_indexes in rename_candidates.values():
        if len(candidate_indexes) == 1:
            removed_index, added_index, _ = candidate_indexes[0]
            removed_index_name = removed_index.get_name().lower()
            added_index_name = added_index.get_name().lower()
            if not removed_index_name in table_differences.renamed_indexes:
                table_differences.renamed_indexes[removed_index_name
                    ] = added_index
                del table_differences.added_indexes[added_index_name]
                del table_differences.removed_indexes[removed_index_name]