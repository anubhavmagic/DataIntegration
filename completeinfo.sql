SELECT *
FROM `countryinfo`.`ageinfo` 
natural join `countryinfo`.`land` 
natural join countryinfo.populationinfo
natural join  countryinfo.populationrateinfo
natural join  countryinfo.regiondata
where country = "India"
;