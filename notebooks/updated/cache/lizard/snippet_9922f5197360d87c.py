def insert_injfilterrejector_option_group(parser):
    injfilterrejector_group = parser.add_argument_group(
        _injfilterrejector_group_help)
    curr_arg = '--injection-filter-rejector-chirp-time-window'
    injfilterrejector_group.add_argument(curr_arg, type=float, default=None,
        help=_injfilterer_cthresh_help)
    curr_arg = '--injection-filter-rejector-match-threshold'
    injfilterrejector_group.add_argument(curr_arg, type=float, default=None,
        help=_injfilterer_mthresh_help)
    curr_arg = '--injection-filter-rejector-coarsematch-deltaf'
    injfilterrejector_group.add_argument(curr_arg, type=float, default=1.0,
        help=_injfilterer_deltaf_help)
    curr_arg = '--injection-filter-rejector-coarsematch-fmax'
    injfilterrejector_group.add_argument(curr_arg, type=float, default=
        256.0, help=_injfilterer_fmax_help)
    curr_arg = '--injection-filter-rejector-seg-buffer'
    injfilterrejector_group.add_argument(curr_arg, type=int, default=10,
        help=_injfilterer_buffer_help)
    curr_arg = '--injection-filter-rejector-f-lower'
    injfilterrejector_group.add_argument(curr_arg, type=int, default=None,
        help=_injfilterer_flower_help)