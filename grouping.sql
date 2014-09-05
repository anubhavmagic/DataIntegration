create view grouping as

select `region` as r, avg(`Death Rate(per 1000 population)`) as a from
countryinfo.regiondata natural join countryinfo.populationrateinfo
group by `region`
order by `region`
;