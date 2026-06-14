def get_health_prediction(glucose, haemoglobin, cholesterol):

    remarks = []

    if glucose > 140:
        remarks.append("High glucose level. Risk of diabetes.")

    if cholesterol > 200:
        remarks.append("High cholesterol. Risk of heart disease.")

    if haemoglobin < 12:
        remarks.append("Low haemoglobin. Possible anemia.")

    if not remarks:
        remarks.append("All values appear within normal range.")

    return " ".join(remarks)