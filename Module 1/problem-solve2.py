# 1. update_rating Implementation 
def update_rating(library: list, song_title: str, new_rating: int) -> bool:
    '''
    This function updates the rating of a specific song in the library
    Args:
        library: A list containing song dictionaries with 'title' and 'rating' keys
        song_title: The title of the song to update the rating for
        new_rating: The new rating (1 to 5) to assign to the song
    Returns:
        Returns True if the song's rating was successfully updated, 
        False if the song is not found
    Raises:
        ValueError: If the new rating is not between 1 and 5
    '''

    # 1. Validate the rating is between 1 and 5
    if new_rating < 1 or new_rating > 5:
        raise ValueError("Rating must be between 1 and 5.")
    
    # 2. Loop over the library to find the song
    for song in library:
        if song['title'] == song_title:
            # 3. Update the rating if song found
            song['rating'] = new_rating
            return True
    
    # 4. Return False if the song was not found
    return False


# 2. add_song Implementation
def add_song(library: list, song: dict) -> bool:
    '''
    This function adds a new song to the library
    Args:
        library: A list containing existing song dictionaries
        song: A dictionary representing a new song with 'title' and 'rating'
    Returns:
        Returns True if the song was successfully added, 
        False if a song with the same title already exists
    Raises:
        ValueError: If the song dictionary is missing required keys or has invalid data
    '''

    # 1. Validate that the song dictionary contains 'title' and 'rating'
    if 'title' not in song or 'rating' not in song:
        raise ValueError("Song dictionary must contain 'title' and 'rating' keys.")
    
    # 2. Validate that the rating is between 1 and 5
    if not (1 <= song['rating'] <= 5):
        raise ValueError("Rating must be between 1 and 5.")
    
    # 3. Check if a song with the same title already exists
    for existing_song in library:
        if existing_song['title'] == song['title']:
            return False  # Song with same title already exists
    
    # 4. Add the song to the library
    library.append(song)
    return True


# 3. remove_song Implementation
def remove_song(library: list, song_title: str) -> bool:
    '''
    This function removes a specific song from the library
    Args:
        library: A list of song dictionaries with 'title' key
        song_title: The title of the song to remove
    Returns:
        Returns True if the song was successfully removed, 
        False if the song is not found
    Raises:
        ValueError: If the song_title is empty or invalid
    '''

    # 1. Validate that the song title is not empty
    if not song_title:
        raise ValueError("Song title cannot be empty.")
    
    # 2. Loop through the library to find and remove the song
    for song in library:
        if song['title'] == song_title:
            library.remove(song)
            return True
    
    # 3. Return False if song is not found
    return False


# 4. get_song_by_title Implementation
def get_song_by_title(library: list, song_title: str) -> dict:
    '''
    This function retrieves the details of a song by its title
    Args:
        library: A list of song dictionaries
        song_title: The title of the song to search for
    Returns:
        A dictionary representing the song with the matching title, 
        or None if not found
    Raises:
        ValueError: If the song_title is empty or invalid
    '''

    # 1. Validate that the song title is not empty
    if not song_title:
        raise ValueError("Song title cannot be empty.")
    
    # 2. Loop through the library to find the song
    for song in library:
        if song['title'] == song_title:
            return song
    
    # 3. Return None if the song is not found
    return None


# 5. average_rating Implementation
def average_rating(library: list) -> float:
    '''
    This function calculates the average rating of all songs in the library
    Args:
        library: A list of song dictionaries with 'rating' key
    Returns:
        The average rating of the songs in the library, rounded to two decimal places
    Raises:
        ValueError: If the library is empty or if all ratings are invalid
    '''

    # 1. Validate that the library is not empty
    if not library:
        raise ValueError("The library is empty.")
    
    # 2. Initialize total rating and count
    total_rating = 0
    count = 0
    
    # 3. Loop through the library to sum valid ratings
    for song in library:
        if 'rating' in song and 1 <= song['rating'] <= 5:
            total_rating += song['rating']
            count += 1
    
    # 4. Raise an error if no valid ratings are found
    if count == 0:
        raise ValueError("No valid ratings in the library.")
    
    # 5. Return the average rating, rounded to 2 decimal places
    return round(total_rating / count, 2)






# Test for the `update_rating` function
def test_update_rating():
    library = [
        {'title': 'Song A', 'rating': 3},
        {'title': 'Song B', 'rating': 4}
    ]

    # Normal case: updating rating for an existing song
    result = update_rating(library, 'Song A', 5)
    if result != True:
        print(f"Case 1: Expected True, got {result}")
    
    # Case where the rating is out of range
    try:
        update_rating(library, 'Song A', 6)
    except ValueError as e:
        if str(e) != "Rating must be between 1 and 5.":
            print(f"Case 2: Expected error 'Rating must be between 1 and 5.', got {str(e)}")

    # Edge case: song not found
    result2 = update_rating(library, 'Song C', 5)
    if result2 != False:
        print(f"Case 3: Expected False, got {result2}")

# Test for the `add_song` function
def test_add_song():
    library = [
        {'title': 'Song A', 'rating': 3},
        {'title': 'Song B', 'rating': 4}
    ]

    # Normal case: adding a new song
    new_song = {'title': 'Song C', 'rating': 5}
    result = add_song(library, new_song)
    if result != True:
        print(f"Case 1: Expected True, got {result}")

    # Edge case: adding a song that already exists
    result2 = add_song(library, new_song)
    if result2 != False:
        print(f"Case 2: Expected False, got {result2}")

    # Edge case: invalid rating
    try:
        add_song(library, {'title': 'Song D', 'rating': 6})
    except ValueError as e:
        if str(e) != "Rating must be between 1 and 5.":
            print(f"Case 3: Expected error 'Rating must be between 1 and 5.', got {str(e)}")

# Test for the `remove_song` function
def test_remove_song():
    library = [
        {'title': 'Song A', 'rating': 3},
        {'title': 'Song B', 'rating': 4}
    ]

    # Normal case: removing an existing song
    result = remove_song(library, 'Song A')
    if result != True:
        print(f"Case 1: Expected True, got {result}")

    # Edge case: trying to remove a song that doesn't exist
    result2 = remove_song(library, 'Song C')
    if result2 != False:
        print(f"Case 2: Expected False, got {result2}")

    # Edge case: empty song title
    try:
        remove_song(library, '')
    except ValueError as e:
        if str(e) != "Song title cannot be empty.":
            print(f"Case 3: Expected error 'Song title cannot be empty.', got {str(e)}")

# Test for the `get_song_by_title` function
def test_get_song_by_title():
    library = [
        {'title': 'Song A', 'rating': 3},
        {'title': 'Song B', 'rating': 4}
    ]

    # Normal case: getting a song by title
    result = get_song_by_title(library, 'Song A')
    if result != {'title': 'Song A', 'rating': 3}:
        print(f"Case 1: Expected { {'title': 'Song A', 'rating': 3} }, got {result}")

    # Edge case: song not found
    result2 = get_song_by_title(library, 'Song C')
    if result2 != None:
        print(f"Case 2: Expected None, got {result2}")

    # Edge case: empty song title
    try:
        get_song_by_title(library, '')
    except ValueError as e:
        if str(e) != "Song title cannot be empty.":
            print(f"Case 3: Expected error 'Song title cannot be empty.', got {str(e)}")

# Test for the `average_rating` function
def test_average_rating():
    library = [
        {'title': 'Song A', 'rating': 3},
        {'title': 'Song B', 'rating': 4}
    ]

    # Normal case: calculating the average rating
    result = average_rating(library)
    if result != 3.5:
        print(f"Case 1: Expected 3.5, got {result}")

    # Edge case: empty library
    try:
        average_rating([])
    except ValueError as e:
        if str(e) != "The library is empty.":
            print(f"Case 2: Expected error 'The library is empty.', got {str(e)}")

    # Edge case: no valid ratings
    try:
        library2 = [{'title': 'Song C', 'rating': 0}]
        average_rating(library2)
    except ValueError as e:
        if str(e) != "No valid ratings in the library.":
            print(f"Case 3: Expected error 'No valid ratings in the library.', got {str(e)}")

# Main test driver function to run all tests
def test_main():
    test_update_rating()
    print("All tests for update_rating passed successfully!")

    test_add_song()
    print("All tests for add_song passed successfully!")

    test_remove_song()
    print("All tests for remove_song passed successfully!")

    test_get_song_by_title()
    print("All tests for get_song_by_title passed successfully!")

    test_average_rating()
    print("All tests for average_rating passed successfully!")


# Run all tests
test_main()
