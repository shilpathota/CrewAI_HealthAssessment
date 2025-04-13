# 🧘 Personalized Wellness Plan using CrewAI

## 🔧 Project Summary
This project uses **CrewAI**, a multi-agent AI framework, to deliver a **personalized fitness, nutrition, and mental wellness plan**. The agents collaborate to collect user input, analyze body composition, assess mental health, and generate tailored recommendations.

---

## 🚀 Setup Instructions

### 1. Environment Setup
```bash
# Clone or create project directory
cd myfirst_crew

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install CrewAI and dependencies
pip install crewai crewai-tools
```

### 2. Project Structure
```
myfirst_crew/
│
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
├── images/
│
├── src/
│   └── myfirst_crew/
│       ├── main.py
│       └── crew.py
```

### 3. Execution
```bash
# Run with default inputs
python -m myfirst_crew.main run
```

---

## 🧠 Agents and Their Roles

| Agent              | Role Description |
|--------------------|------------------|
| **Intake Agent**       | Collects basic user inputs: height, weight, age, gender, health goals, dietary preferences, mental health, and images. |
| **Body Analyzer**      | Uses height, weight, and front/back images to estimate **body fat percentage**, **BMI**, **posture**, and **body type**. |
| **Therapist**          | Analyzes mental health inputs and suggests calming or motivational practices. |
| **Personal Trainer**   | Creates a 5-day workout plan based on body composition and problem areas. |
| **Nutritionist**       | Generates an Indian vegetarian meal plan using user goals, fitness level, and body fat percentage. |
| **Marketing Expert**   | Compiles all outputs into a well-formatted wellness plan in Markdown. |

---

## ✅ Tasks and Dependencies

| Task Name             | Description | Agent | Context |
|-----------------------|-------------|--------|---------|
| **intake_task**       | Collect and structure user input fields. | Intake Agent | — |
| **body_analysis_task**| Analyze images + metrics for body composition. | Body Analyzer | intake_task |
| **therapist_task**    | Recommend mental wellness routines. | Therapist | intake_task |
| **trainer_task**      | Generate a 5-day workout plan. | Personal Trainer | body_analysis_task |
| **nutritionist_task** | Create a diet plan based on user input and analysis. | Nutritionist | body_analysis_task |
| **marketing_task**    | Compile all results into a structured markdown report. | Marketing Expert | All above tasks |

---

## 📤 Input Fields

```json
{
  "height": "170 cm",
  "weight": "68 kg",
  "age": "30",
  "gender": "female",
  "health_goals": "Lose fat and improve energy",
  "meal_type": "indian vegetarian",
  "problem_areas": "hips and thighs",
  "mental_health_inputs": "feels stressed and tired often",
  "front_image_path": "images/front_image.jpg",
  "back_image_path": "images/back_image.jpg"
}
```

---

## 📄 Final Output

After execution, the crew generates a markdown file `wellness_plan.md` which includes:

- **User Profile**
- **Body Analysis**
- **5-Day Workout Plan**
- **Mental Wellness Suggestions**
- **Nutrition Plan**

---

## 🧪 How It Works (Execution Flow)

1. `intake_task`: Collects and validates user input.
2. `body_analysis_task`: Estimates body fat % and posture using AI.
3. `therapist_task`: Provides mental health practices.
4. `trainer_task`: Prepares personalized workouts.
5. `nutritionist_task`: Crafts an Indian meal plan using body fat data.
6. `marketing_task`: Merges all outputs into a beautiful markdown report.

---

## 🧠 What Makes This Cool?

- 🔁 **Task-to-task context sharing** (body fat % passed to diet plan)
- 🤖 **Modular multi-agent design** using CrewAI
- 📊 **Image-based body analysis**
- 📄 **Auto-generated personalized wellness plan**