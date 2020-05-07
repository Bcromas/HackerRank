SELECT salary*months as earnings, count(*) 
FROM employee
GROUP BY earnings
ORDER BY earnings DESC limit 1;