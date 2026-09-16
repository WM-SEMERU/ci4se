def legacy_events_view(request):
    events = TeacherEvent.objects.all()
    event_count = events.count()
    paginator = Paginator(events, 100)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render_to_response('teacher_events.html', {'page_name':
        'Legacy Events', 'events': events, 'event_count': event_count},
        context_instance=RequestContext(request))