CREATE DATABASE IF NOT EXISTS football_db;
USE football_db;

DROP TABLE players;

CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    team VARCHAR(255) NOT NULL,
    games_played INT NOT NULL,
    yellow_cards INT NOT NULL,
    red_cards INT NOT NULL
);

INSERT INTO players (name, team, games_played, yellow_cards, red_cards)VALUES ("Joao", "Santos", "50", "10", "1");