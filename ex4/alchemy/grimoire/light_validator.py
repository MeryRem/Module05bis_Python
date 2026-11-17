def validate_ingredients(ingredients: str) -> str:
    # Import inside funct: no circular endless loop
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    text = ingredients.lower()
    if any(item in text for item in allowed):
        return f"{ingredients}- VALID"
    return f"{ingredients}- INVALID"