def find_first_legal_standard(pokelist): #not working correctly because the Pokemon API is not up to date
  for pokemans in pokelist['data']:
    if 'legalities' in pokemans and 'standard' in pokemans['legalities'] and pokemans['legalities']['standard'] == 'Legal':
      return pokemans
  return None

def find_first_regulation_mark_f_or_higher(pokelist):
    """
    Finds and returns the first entry in the 'pokelist' list where
    'regulationMark' is 'F', 'G', 'H', or a letter that comes later in the alphabet.

    Args:
        pokelist: A dictionary containing a 'data' list of entries.

    Returns:
        The first entry where 'regulationMark' is 'F', 'G', 'H', or higher,
        or None if no such entry is found.
    """
    # listed = pokelist['data']
    for pokeman in pokelist:
        if 'regulationMark' in pokeman and pokeman['regulationMark'] >= 'F':
            return pokeman
    return None