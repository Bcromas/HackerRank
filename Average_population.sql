SELECT Country.CONTINENT, FLOOR(AVG(City.POPULATION))
FROM CITY
INNER JOIN Country on City.COUNTRYCODE = Country.CODE
GROUP BY Country.CONTINENT;