SELECT 
	MONTH(r.date) AS month, 
    #avg(wr.business_stars) as business_stars,
    wr.review_stars,
    count(wr.review_stars) as total_stars
FROM `f_weather_on_review` as wr 
inner join dana.yelp_review as r 
on wr.review_id = r.review_id
group by MONTH(r.date), wr.review_stars
order by MONTH(r.date) desc, wr.review_stars desc