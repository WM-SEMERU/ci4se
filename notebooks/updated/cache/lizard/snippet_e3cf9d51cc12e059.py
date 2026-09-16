def home(request):
    cage_list = Animal.objects.values('Cage').distinct()
    cage_list_current = cage_list.filter(Alive=True)
    animal_list = Animal.objects.all()
    animal_list_current = animal_list.filter(Alive=True)
    strain_list = animal_list.values('Strain').distinct()
    strain_list_current = animal_list_current.values('Strain').distinct()
    return render(request, 'home.html', {'animal_list': animal_list,
        'animal_list_current': animal_list_current, 'strain_list':
        strain_list, 'strain_list_current': strain_list_current,
        'cage_list': cage_list, 'cage_list_current': cage_list_current})