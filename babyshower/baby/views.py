import random
from django.shortcuts import render
from typing import List
from django.http import HttpResponse, JsonResponse
NUMBER_OF_PEOPLE = 60
NUMBER_OF_HOUSES = 4


def index(request):
    # Generate a random number from 1 to 4

    counter = request.GET.get('counter')
    # Get the corresponding music file for the random number
    if counter is None:
        counter = 0
    else:
        counter = int(counter)
    # Define a dictionary to map random numbers to music file names
    music_files = {1: 'Gryfindor.mp3',
                   2: 'Hufflepuff.mp3',
                   3: 'Ravenclaw.mp3',
                   4: 'Slytherin.mp3',
                   }

    file = music_files[return_number(counter)]

    return render(request, 'play-song.html',
                  {'music_file': file}
                  )


def return_number(counter) -> List[int]:

    loop = int(NUMBER_OF_PEOPLE/NUMBER_OF_HOUSES)
    my_list = [i for i in range(1, 5) for _ in range(loop)]
    random.Random(6).shuffle(my_list)
    return my_list[counter]
