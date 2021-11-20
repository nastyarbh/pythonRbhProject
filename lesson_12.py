def rus_facults(engname):
    hogwards = {
        'gryffindor': 'гриффиндор',
        'slytherin': 'слизерин',
        'ravenclaw': 'когтевран',
        'hufflepuff': 'пуффендуй'
    }
    if hogwards[engname]:
        return hogwards[engname]
    else:
        return 'нет такого факультета'
