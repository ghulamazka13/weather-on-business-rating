insert into dana_dw.f_weather_on_review 
select 
	r.user_id, 
    r.review_id, 
    b.business_id, 
    u.review_count as user_review_count,
    b.review_count as business_review_count,
    t.compliment_count,
    r.stars as review_stars,
    b.stars as business_stars
from dana_ods.yelp_business as b 
inner join dana.yelp_review as r 
on b.business_id = r.business_id
inner join dana.yelp_user as u 
on u.user_id = r.user_id
inner join dana.yelp_tip as t 