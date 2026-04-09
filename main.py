from fastapi import FastAPI, HTTPException
from schemas import MealPlanRequest, MealPlanResponse, DayMeal
from prompts.mealplan import build_meal_plan_prompt
from services.llm import generate

app = FastAPI(
    title="FoodieFlow",
    description="AI-powered meal planning — Module 1: Personalised Meal Planning Engine",
    version="0.1",
)

@app.get("/")
def index():
    return {"status: API is up and running."}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/meal-plan", response_model=MealPlanResponse)
async def generate_meal_plan(request: MealPlanRequest):
    prompt = build_meal_plan_prompt(
        country=request.country,
        fitness_goal=request.fitness_goal.value,
        diet_preference=request.diet_preference.value,
    )

    try:
        result = await generate(prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {str(e)}")

    raw_plan = result.get("meal_plan")
    if not raw_plan or len(raw_plan) != 30:
        raise HTTPException(
            status_code=500,
            detail=f"LLM returned an unexpected response. Got {len(raw_plan) if raw_plan else 0} days."
        )

    return MealPlanResponse(
        country=request.country,
        fitness_goal=request.fitness_goal.value,
        diet_preference=request.diet_preference.value,
        total_days=30,
        meal_plan=[DayMeal(**day) for day in raw_plan],
    )