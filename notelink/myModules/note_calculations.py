def check_note_slug(note_title):
    note_slug = ""
    note_slug=note_title
    for letter in note_title:
        if not letter.isalpha():
            note_slug=note_slug.replace(letter, "-")
    return note_slug