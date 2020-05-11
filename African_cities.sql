-- African Cities
SELECT City.Name
FROM City
LEFT JOIN Country on City.COUNTRYCODE = Country.Code
WHERE Country.CONTINENT = "Africa";