def calculate_risk(event_type):

    score = 0

    if event_type == " UNKNOWN_DEVICE":
        score += 20

    elif event_type == "MASS_COPY":
        score += 40

    return score

def get_risk_level(score):

    if score <= 20:
        return "LOW"
    
    elif score <= 50:
        return "MEDIUM"
    
    elif score <= 70 :
        return "HIGH"
    
    else :
        return "VERY_HIGH"