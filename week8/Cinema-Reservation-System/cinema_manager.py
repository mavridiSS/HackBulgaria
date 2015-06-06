from settings import ROWS, COLUMNS, FREE_SEAT, TAKEN_SEAT


class CinemaManager:
    MAX_SEATS = 100

    def __init__(self, conn):
        self.__conn = conn
        self.__hall = None

    def get_movies_ordered_by_rating(self):
        cursor = self.__conn.cursor()
        result = cursor.execute("""SELECT movie_id,movie_name,movie_rating
                                   FROM Movies
                                   ORDER BY movie_rating DESC""")
        return result.fetchall()

    def get_movie_by_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute("""SELECT movie_name,movie_rating
                                   FROM Movies
                                   WHERE movie_id=?""", (movie_id, ))
        return result.fetchone()

    def get_projection_by_id(self, projection_id):
        cursor = self.__conn.cursor()
        result = cursor.execute("""SELECT date,time,type
                                   FROM Projections
                                   WHERE projection_id=?""", (projection_id, ))
        return result.fetchone()

    def get_projections_for_movie(self, movie_id, date=None):
        cursor = self.__conn.cursor()
        if date:
            result = cursor.execute("""SELECT P.projection_id,date,time,type,COUNT(R.username)
                                       FROM Projections AS P
                                       LEFT OUTER JOIN Reservations AS R
                                       ON R.projection_id=P.projection_id
                                       WHERE movie_id=? AND date=?
                                       GROUP BY P.projection_id
                                       ORDER BY time ASC""", (movie_id, date))
            return result.fetchall()
        else:
            result = cursor.execute("""SELECT P.projection_id,date,time,type,COUNT(R.username)
                                       FROM Projections AS P
                                       LEFT OUTER JOIN Reservations AS R
                                       ON R.projection_id=P.projection_id
                                       WHERE movie_id=?
                                       GROUP BY P.projection_id
                                       ORDER BY time ASC""", (movie_id, ))
            return result.fetchall()

    def create_hall(self):
        self.__hall = [["." for _ in range(1, ROWS + 1)]
                       for _ in range(1, COLUMNS + 1)]

    def get_seats_for_projection(self, projection_id):
        cursor = self.__conn.cursor()

        cursor.execute(""" SELECT row,col
                           FROM Reservations
                           WHERE projection_id=?""", (projection_id, ))
        seats = cursor.fetchall()
        return seats

    def take_seats(self, seats):
        for seat in seats:
            self.__hall[seat[0]][seat[1]] = TAKEN_SEAT

    def create_and_populate_hall(self, projection_id):
        self.create_hall()

        seats = self.get_seats_for_projection(projection_id)

        self.take_seats(seats)

    def check_if_seat_is_free(self, row, col):
        return self.__hall[row - 1][col - 1] == FREE_SEAT

    def print_seats_for_projection(self, projection_id):
        self.create_and_populate_hall(projection_id)

        print("    ", ' '.join([str(a) for a in range(1, ROWS + 1)]))

        for seat_number, row in enumerate(self.__hall):
            print(seat_number + 1, "  ", ' '.join(row))

    def make_new_reservation(self, user, proj_id, row, col):
        cursor = self.__conn.cursor()

        cursor.execute(""" INSERT INTO Reservations(username,projection_id,row,col)
                           VALUES(?, ?, ?, ?)""", (user,
                                                   proj_id,
                                                   row - 1,
                                                   col - 1))

        self.__conn.commit()

    def delete_reservation(self, name):
        cursor = self.__conn.cursor()

        cursor.execute("""DELETE
                          FROM Reservations
                          WHERE username=?""", (name, ))

        self.__conn.commit()
