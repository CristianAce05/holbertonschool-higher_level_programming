-- Lists all shows contained in the database hbtn_0d_tvshows
-- Displays: tv_shows.title - tv_show_genres.genre_id
-- If a show doesn't have a genre, displays NULL
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
