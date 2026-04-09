def build_meal_plan_prompt(country: str, fitness_goal: str, diet_preference: str) -> str:
    diet_line = (
        f"- Diet preference: {diet_preference}"
        if diet_preference != "none"
        else "- No specific diet preference"
    )

    return f"""You are a professional meal planner. Generate a 30-day personalized meal plan based on the user profile below.

USER PROFILE:
- Country/Cuisine preference: {country}
- Fitness goal: {fitness_goal}
{diet_line}

INSTRUCTIONS:
- Use meals typical of {country} cuisine where possible.
- Tailor meals to support the goal: {fitness_goal}.
- Each day must have breakfast, lunch, dinner and snack.
- Keep meal names short (e.g. "Grilled Chicken Rice", "Vegetable Omelette").
- meal name should based on country (e.g. like for pakistan karahi / korma etc).
- No explanations, no extra text — return ONLY valid JSON.

Return this exact JSON structure:
{{
  "meal_plan": [
    {{"day": 1, "breakfast": "...", "lunch": "...", "dinner": "...", "snack": "..."}},

    {{"day": 2, "breakfast": "...", "lunch": "...", "dinner": "..." "snack": "..."}},
    ...
    {{"day": 30, "breakfast": "...", "lunch": "...", "dinner": "..." "snack": "..."}}
  ]
}}"""