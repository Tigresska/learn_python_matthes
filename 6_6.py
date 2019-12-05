favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}

poll_list = ['maria', 'sarah', 'daniel', 'phil']

for name in poll_list:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for comleting the survey!")
    else:
        print(f"{name.title()}, would you like to participate in a survey?")