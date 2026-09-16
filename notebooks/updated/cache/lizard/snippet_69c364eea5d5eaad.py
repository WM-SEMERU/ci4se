def format_diffindex(diff_index):
    for diff in diff_index:
        if diff.new_file:
            yield format_diff_A(diff)
        elif diff.deleted_file:
            yield format_diff_D(diff)
        elif diff.renamed:
            yield format_diff_R(diff)
        elif diff.a_blob and diff.b_blob and diff.a_blob != diff.b_blob:
            yield format_diff_M(diff)