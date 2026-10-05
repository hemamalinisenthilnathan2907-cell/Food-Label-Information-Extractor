import re


def extract_information(text):
    """
    Extract common food-label information
    using regular expressions.
    """

    # Weight
    weight = re.findall(
        r"\b\d+(?:\.\d+)?\s?(?:mg|g|kg|ml|l)\b",
        text,
        re.IGNORECASE
    )

    # Calories
    calories = re.findall(
        r"\b\d+(?:\.\d+)?\s?(?:kcal|calories|cal)\b",
        text,
        re.IGNORECASE
    )

    # Dates
    dates = re.findall(
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        text
    )

    # Protein
    protein = re.findall(
        r"protein\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:g|mg)",
        text,
        re.IGNORECASE
    )

    # Fat
    fat = re.findall(
        r"(?:total\s+)?fat\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:g|mg)",
        text,
        re.IGNORECASE
    )

    # Carbohydrates
    carbohydrates = re.findall(
        r"(?:total\s+)?carbohydrate[s]?\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:g|mg)",
        text,
        re.IGNORECASE
    )

    # Ingredients
    ingredients = []

    for line in text.splitlines():
        if "ingredient" in line.lower():
            ingredients.append(line.strip())

    return {
        "weight": weight,
        "calories": calories,
        "dates": dates,
        "protein": protein,
        "fat": fat,
        "carbohydrates": carbohydrates,
        "ingredients": ingredients
    }
