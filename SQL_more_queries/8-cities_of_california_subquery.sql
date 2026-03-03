-- Script pour lister toutes les villes de California dans la database hbtn_0d_usa
SELECT id, name
FROM hbtn_0d_usa.cities
WHERE state_id = (
    SELECT id
    FROM hbtn_0d_usa.states
    WHERE name = "California"
    LIMIT 1
)
ORDER BY id ASC;
