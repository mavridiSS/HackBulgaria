DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(movie_id INTEGER PRIMARY KEY,
					movie_name TEXT,
					movie_rating REAL);

INSERT INTO Movies(movie_name,movie_rating)
VALUES ("The Hunger Games: Catching Fire", 7.8),
	   ("Her", 8.3),
	   ("Wreck-It Ralph", 7.9);

DROP TABLE IF EXISTS Projections;

CREATE TABLE Projections(projection_id INTEGER PRIMARY KEY,
						 movie_id INTEGER,
						 type TEXT,
						 date TEXT,
						 time TEXT,
						 FOREIGN KEY(movie_id) REFERENCES Movies(movie_id));

INSERT INTO Projections(movie_id,type,date,time)
VALUES (1, "3D", "2014-04-01", "19:10"),
	   (1, "2D", "2014-04-01", "19:00"),
	   (1, "4DX", "2014-04-02", "21:00"),
	   (3, "2D", "2014-04-05", "20:20"),
	   (2, "3D", "2014-04-02", "22:00"),
	   (2, "2D", "2014-04-02", "19:30");

DROP TABLE IF EXISTS Reservations;

CREATE TABLE Reservations(reservation_id INTEGER PRIMARY KEY,
						  username TEXT,
						  projection_id INTEGER,
						  row INTEGER,
						  col INTEGER,
						  FOREIGN KEY(projection_id) REFERENCES Projections(projection_id));


INSERT INTO Reservations(username,projection_id,row,col)
VALUES ("RadoRado", 1, 2, 1),
	   ("RadoRado", 1, 3, 5),
	   ("RadoRado", 1, 7, 8),
	   ("Ivo", 3, 1, 1),
	   ("Ivo", 3, 1, 2),
	   ("Georgi", 5, 2, 3),
	   ("Georgi", 5, 2, 4);

