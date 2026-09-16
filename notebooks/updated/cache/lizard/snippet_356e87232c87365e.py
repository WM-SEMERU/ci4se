def generate_string(out_dir, limits):
    max_limit = max(int(v) for v in limits)
    with open(filename(out_dir, 'string'), 'wb') as out_f:
        with IncludeGuard(out_f):
            out_f.write(
                """
#include <boost/metaparse/v{0}/cpp11/impl/concat.hpp>
#include <boost/preprocessor/cat.hpp>
"""
                .format(VERSION))
            generate_make_string(out_f, 512)
            out_f.write(
                """
#ifndef BOOST_METAPARSE_LIMIT_STRING_SIZE
#  error BOOST_METAPARSE_LIMIT_STRING_SIZE not defined
#endif

#if BOOST_METAPARSE_LIMIT_STRING_SIZE > {0}
#  error BOOST_METAPARSE_LIMIT_STRING_SIZE is greater than {0}. To increase the limit run tools/string_headers.py of Boost.Metaparse against your Boost headers.
#endif

"""
                .format(max_limit))
            define_macro(out_f, ('STRING', ['s'],
                '{0}::make_string< {0}::take(sizeof(s)-1), sizeof(s)-1-{0}::take(sizeof(s)-1),BOOST_PP_CAT({1}, BOOST_METAPARSE_LIMIT_STRING_SIZE)(s)>::type'
                .format('::boost::metaparse::v{0}::impl'.format(VERSION),
                macro_name('I'))))
            out_f.write('\n')
            for limit in xrange(0, max_limit + 1):
                out_f.write('#define {0} {1}\n'.format(macro_name('I{0}'.
                    format(limit)), macro_name('INDEX_STR{0}'.format(min(
                    int(l) for l in limits if int(l) >= limit)))))
            out_f.write('\n')
            prev_macro = None
            prev_limit = 0
            for length_limit in (int(l) for l in limits):
                this_macro = macro_name('INDEX_STR{0}'.format(length_limit))
                out_f.write('#define {0}(s) {1}{2}\n'.format(this_macro, 
                    '{0}(s),'.format(prev_macro) if prev_macro else '', ','
                    .join('{0}((s), {1})'.format(macro_name('STRING_AT'), i
                    ) for i in xrange(prev_limit, length_limit))))
                prev_macro = this_macro
                prev_limit = length_limit