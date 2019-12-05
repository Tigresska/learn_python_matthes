def get_formatted_name(first_name, last_name, middle_name = ''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = F"{first_name} {middle_name} {last_name}"
    else:
        full_name = F"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'lee' )
print(musician)