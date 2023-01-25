INSERT INTO dana_ods.yelp_business
SELECT 
	b.business_id, 
   	b.name, 
    b.address, 
    b.city,
    b.state,
    b.postal_code,
    b.latitude,
    b.longitude,
    b.stars,
    b.review_count,
    b.is_open,
    JSON_EXTRACT(b.attributes, '$.key') as outdoor_seating, #one example parameter that have correlation with weather
    b.categories,
    b.hours
FROM  `yelp_business` as b
where b.state = 'PA' #we took 'PA' state since the weather data that we used were there
and b.categories like '%Restaurant%' #we took restaurant since we want to look the correlation