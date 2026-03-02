-- Script pour lister le nombre d'apparition avec le même score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
