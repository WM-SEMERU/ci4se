def anim_to_html(anim, fps=None, embed_frames=True, default_mode='loop'):
    if fps is None and hasattr(anim, '_interval'):
        fps = 1000.0 / anim._interval
    plt.close(anim._fig)
    if hasattr(anim, '_html_representation'):
        return anim._html_representation
    else:
        with _NameOnlyTemporaryFile(suffix='.html') as f:
            anim.save(f.name, writer=HTMLWriter(fps=fps, embed_frames=
                embed_frames, default_mode=default_mode))
            html = open(f.name).read()
        anim._html_representation = html
        return html