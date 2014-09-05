select `country`,`region`,`Death Rate(per 1000 population)` from countryinfo.regiondata natural join countryinfo.populationrateinfo
order by region;