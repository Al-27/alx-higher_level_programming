-- DESC
SELECT tv_genres.name FROM tv_show_genres 
    FULL OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
    FULL OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = "Dexter" ORDER BY tv_show_genres.title ASC;
