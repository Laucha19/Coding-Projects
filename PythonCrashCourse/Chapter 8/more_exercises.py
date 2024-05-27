magician_names = ['vivaldi', 'houdini', 'cris angel', 'david blaine']
great_magicians = []

def show_magicians():
    print("The following are the name of all our best performers for the night:")
    for magicians in magician_names:
        print(magicians.title())

def make_great():
    print("\nThe following is a list of modified names of magicians:")
    while magician_names:
        current_magicians = magician_names.pop()
        great_magicians.append(current_magicians)

    for great_magician in great_magicians:
        print(great_magician.title() + " the Great!")



show_magicians()
make_great()
