import re


class CinemaInterface:
    HELP = """List of commands:
              1)'show_movies' -all movies ordered by rating\n
              2)'show_movie_projections <movie_id> [<date>]'\n
              3)'exit'\n
              4)'make_reservation'-input data for new reservation"""

    def __init__(self, cinema_manager):
        self.__manager = cinema_manager

    def __command_dispatcher(self, command):
        if command == "show_movies":
            self.show_movies()

# need to fix if a date is in the input !!!!
        if "show_movie_projections" in command:
            movie_id = re.search(r'\d+', command).group()
            self.show_movie_projections(movie_id)

        if command == "make_reservation":
            self.make_reservation()

        if "cancel_reservation" in command:
# make reservation name unique,this way i can cancel two names that are equal
            name = command[len("cancel_reservation") + 1:]
            self.cancel_reservation(name)

        if command == "exit":
            return False

        if command == "help":
            self.print_help()

    def print_help(self):
        print(self.__class__.HELP)

    def start(self):
        while True:
            command = input("Enter command:")
            if self.__command_dispatcher(command) == False:
                break
            else:
                continue

    def show_movies(self):
        result = self.__manager.get_movies_ordered_by_rating()
        for row in result:
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

    def show_movie_projections(self, movie_id):
        all_seats = self.__manager.MAX_SEATS
        result = self.__manager.get_projections_for_movie(movie_id)
        for row in result:
            print("[{}] - {} {} ({}) - {} spots available".format(row[0],
                                                                  row[1],
                                                                  row[2],
                                                                  row[3],
                                                                  all_seats - row[4]))

    def show_reservation_info(self, movie_id, projection_id, seats):
        result = self.__manager.get_movie_by_id(movie_id)
        print("Movie: {}  ({})".format(result[0], result[1]))

        result = self.__manager.get_projection_by_id(projection_id)
        print("Date and Time:{} {} ({})".format(result[0],
                                                result[1],
                                                result[2]))
        result = ["({}, {})".format(seat[0], seat[1]) for seat in seats]
        print("Seats: {}".format(','.join(result)))

    def take_a_seat(self, number_of_seats):
        seats = []
        for number in range(1, number_of_seats + 1):
            while True:
                seat = input("Choose seat {}:".format(number))

                if not self.__manager.check_if_seat_is_free(int(seat[1]),
                                                            int(seat[3])):
                    print("This seat is already taken!")
                else:
                    seats.append((int(seat[1]), int(seat[3])))
                    break
        return seats

    def make_reservation(self):
        name = input("Choose username:")
        tickets = input("Choose number of tickets:")

        self.show_movies()

        movie = input("Choose movie number:")

        self.show_movie_projections(movie)

        projection = input("Choose projection number:")
        self.__manager.print_seats_for_projection(projection)

        seats = self.take_a_seat(int(tickets))

        self.show_reservation_info(int(movie), int(projection), seats)

        finalize = input("To confirm reservation type 'finalize':")

        if finalize == "finalize":
            for seat in seats:
                self.__manager.make_new_reservation(name, int(projection),
                                                    seat[0],
                                                    seat[1])

        print("Thanks.")

    def cancel_reservation(self, name):
        self.__manager.delete_reservation(name)








