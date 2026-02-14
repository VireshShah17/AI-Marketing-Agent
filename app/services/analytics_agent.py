import random 
from .. import models


def generate_analytics(db, post):
    analytics = models.Analytics(
        post_id = post.id,
        impressions = random.randint(100, 1000),
        clicks = random.randint(10, 100),
        engagement_rate = round(random.uniform(0.1, 10.0), 2)
    )

    db.add(analytics)
    db.commit()
    
