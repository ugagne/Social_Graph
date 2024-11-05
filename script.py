
import random
import os
os.system('clear')

people_list = ["Myrto", "Ulysse", "Usher", "Indiana", "Isaac", "Raoul", "Raphaël", "Krystel", "Kelsey", "Sara", "Shawn", "Thomas", "Théo", "Marie", "Nathan", "Nadia"]
people_dict = {person: [] for person in people_list}
#people_dict = {"Ulysse": ["Indiana"], "Indiana": ["Ulysse"],"Raoul": ["Ivan"], "Ivan": ["Raoul"]}

def setup_graph():
    for person in people_dict:
        friend = person
        while friend == person:
            friend = random.choice(people_list)
        if friend not in people_dict[person]:
            people_dict[person].append(friend)
        if person not in people_dict[friend]:
            people_dict[friend].append(person)

def search_person():
    result = None
    while result == None:
        input_1 = input("\nStart typing a name:\n\n")
        os.system('clear')
        possible_names = []
        for person in people_list:
            match = True
            input_1_substring = input_1[:len(person)]
            for character_index in range(len(input_1_substring)):
                if input_1[character_index].lower() != person[character_index].lower():
                    match = False
                    break
            if match:
                possible_names.append(person)
        if len(possible_names) == 0:
            print("\nNo match found. Let's try again.")
        elif len(possible_names) == 1:
            input_2 = input(f"\nAre you looking for {possible_names[0]} ? Answer y/n :\n\n")
            os.system('clear')
            if input_2.lower() == "y".lower():
                result = possible_names[0]
            elif input_2.lower() != "n".lower():
                print("\nInvalid entry. Let's try again.")
        else:
            possible_names_string = ""
            for name in possible_names: possible_names_string += name + ", "
            possible_names_string = possible_names_string[:-2]
            print(f"\nMatching results: {possible_names_string}\n\nPlease refine your search.")
    return result

def bfs(person_1, person_2):
    queue = [[person_1]]
    visited = []
    while queue:
        # print("a", queue)
        # print("b", visited)
        current_path = queue.pop(0)
        current_person = current_path[-1]
        # print("c", current_path)
        # print("d", current_person)
        visited.append(current_person)
        if current_person == person_2:
            return current_path
        for friend in people_dict[current_person]:
            # print("e", friend)
            if friend not in visited:
                new_path = current_path + [friend]
                # print("f", new_path)
                queue.append(new_path)

def find_path(person_1, person_2):
    path = bfs(person_1, person_2)
    if path == None:
        print("\nNo path found.")
    elif len(path) == 1:
        print("\nYou entered the same name twice.")
    else:
        output = ""
        for person in path:
            output += person + ", "
        print("\nAmazing! Here's the shortest link I could find:\n\n" + str(output[:-2]))
                
def script():
    setup_graph()
    # print(people_dict)
    print("\nWelcome! Enter two names to find how they are related!")
    person_1 = search_person()
    print("\nGreat! Let's move on to the second name!")
    person_2 = search_person()
    find_path(person_1, person_2)
    input("\n")
    os.system('clear')

script()