from pydantic import BaseModel
from enum import Enum
from typing import Optional


class FitnessGoal(str, Enum):
    build_muscle = "build_muscle"
    lose_weight = "lose_weight"
    maintain_weight = "maintain_weight"
    stay_balanced = "stay_balanced"
    lose_cholesterol = "lose_cholesterol"
    improve_digestion = "improve_digestion"


class DietPreference(str, Enum):
    vegan = "vegan"
    low_carb = "low_carb"
    ovo_vegetarian = "ovo_vegetarian"
    pescatarian = "pescatarian"
    gluten_free = "gluten_free"
    vegetarian = "vegetarian"
    none = "none"


class MealPlanRequest(BaseModel):
    country: str
    fitness_goal: FitnessGoal
    diet_preference: Optional[DietPreference] = DietPreference.none

    model_config = {
        "json_schema_extra": {
            "example": {
                "country": "Pakistan",
                "fitness_goal": "build_muscle",
                "diet_preference": "none"
            }
        }
    }


class DayMeal(BaseModel):
    day: int
    breakfast: str
    lunch: str
    dinner: str
    snack: str


class MealPlanResponse(BaseModel):
    country: str
    fitness_goal: str
    diet_preference: str
    total_days: int
    meal_plan: list[DayMeal]