select country, `landarea(sq.km)` from land
where `landarea(sq.km)` in
(select min(`landarea(sq.km)`) from land)
;