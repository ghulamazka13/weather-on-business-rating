SELECT 
	wr.business_id,
    wr.review_stars,
    r.text
FROM `f_weather_on_review` as wr 
inner join dana.yelp_review as r 
on wr.review_id = r.review_id
where wr.review_stars in (1,2)
order by wr.review_stars desc;