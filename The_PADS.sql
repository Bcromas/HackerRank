SELECT CONCAT(Name,
CASE
    WHEN Occupation = "Doctor" THEN "(D)"
    WHEN Occupation = "Actor" THEN "(A)"
    WHEN Occupation = "Singer" THEN "(S)"
    ELSE "(P)"
END
              )
FROM OCCUPATIONS
ORDER BY Name ASC;

SELECT CONCAT("There are a total of ", COUNT(*)," ", LOWER(Occupation),"s.")
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*) ASC, Occupation ASC;