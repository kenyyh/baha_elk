create database baha;
USE baha;
SELECT k.kanban_name, r.ranking, r.hot FROM ranking r JOIN kanban k ON r.kanban_id = k.kanban_id ORDER BY r.ranking;
SELECT * FROM ranking WHERE rank_day = "2020-05-08";
DELETE FROM ranking WHERE rank_day = "2020-05-08";
SET foreign_key_checks = 1;
SELECT * FROM kanban;
SELECT * FROM kanban WHERE class_id = 400 and kanban_id > 30000;
SELECT * FROM kanban_class;
SELECT * FROM baha.kanban WHERE kanban_name LIKE "%百聞%";

SELECT r.ranking, k.kanban_name, r.hot FROM ranking r 
JOIN kanban k ON r.kanban_id = k.kanban_id
WHERE r.rank_day = "2020-05-06" -- AND k.class_id = 94
ORDER BY r.hot DESC;

SELECT r.rank_day, r.ranking, k.kanban_name, r.hot FROM ranking r JOIN kanban k ON r.kanban_id = k.kanban_id;


SELECT kc.class_name, COUNT(k.kanban_id) FROM kanban k 
JOIN kanban_class kc ON k.class_id = kc.class_id 
GROUP BY k.class_id 
ORDER BY COUNT(k.kanban_id);

-- SET foreign_key_checks = 0;
-- SET foreign_key_checks = 1;

-- TRUNCATE kanban;
-- TRUNCATE ranking;
-- TRUNCATE kanban_class;
-- DROP TABLE kanban;
-- DROP TABLE ranking;
-- DROP TABLE kanban_class;


-- 建表格
CREATE TABLE kanban
(
    kanban_id   INT  NOT NULL ,
    kanban_name VARCHAR(100) NOT NULL,
    class_id    INT NOT NULL,
    PRIMARY KEY (kanban_id),
    FOREIGN KEY (class_id) REFERENCES kanban_class (class_id)
);

CREATE TABLE  kanban_class
(
    class_id     INT    NOT NULL,
    class_name   VARCHAR(30)    NOT NULL,
    PRIMARY KEY (class_id)
);

CREATE TABLE  ranking
(
    rank_day             DATE NOT NULL ,
    kanban_id            INT NOT NULL,
    ranking              INT NOT NULL,
    hot                  INT NOT NULL,
    article              INT NOT NULL,
    PRIMARY KEY (rank_day, kanban_id),
    FOREIGN KEY (kanban_id) REFERENCES kanban (kanban_id)
);

