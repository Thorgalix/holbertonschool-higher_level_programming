-- Script pour lister tous les enregistrements d'une table
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
