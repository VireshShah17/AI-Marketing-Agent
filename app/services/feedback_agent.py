def generate_feedback_strategy(analytics):
    strategy = ""
    if analytics.impressions < 500:
        strategy += "Improve hook to grab attention. Add stronger opening line. "

    if analytics.clicks < 50:
        strategy += "Add curiosity-driven CTA and value-focused messaging. "

    if analytics.engagement_rate < 3:
        strategy += "Make tone more emotional and conversational. "

    if analytics.engagement_rate > 7:
        strategy += "Style performed well. Maintain similar tone and structure. "

    return strategy
