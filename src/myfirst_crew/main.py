#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from .crew import MyFirstCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# 👤 Modify these input values based on your user profile / UI input
user_inputs = {
    "height": "170 cm",
    "weight": "68 kg",
    "age": "30",
    "gender": "female",
    "health_goals": "Lose fat and improve energy",
    "meal_type": "indian vegetarian",
    "problem_areas": "hips and thighs",
    "mental_health_inputs": "feels stressed and tired often",
    "front_image_path": "C:/Projects/CrewAI/myfirst_crew/images/front_image.jpg",
    "back_image_path": "C:/Projects/CrewAI/myfirst_crew/images/back_image.jpg"
}


def run():
    """
    Run the fitness crew with current inputs.
    """
    try:
        MyFirstCrew().crew().kickoff(inputs=user_inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the fitness crew.
    Usage: python main.py train <iterations> <output_filename>
    """
    try:
        n_iterations = int(sys.argv[2])
        filename = sys.argv[3]

        MyFirstCrew().crew().train(n_iterations=n_iterations, filename=filename, inputs=user_inputs)
    except IndexError:
        print("❌ Usage: python main.py train <iterations> <output_filename>")
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def test():
    """
    Test the fitness crew with a specific model.
    Usage: python main.py test <iterations> <openai_model_name>
    """
    try:
        n_iterations = int(sys.argv[2])
        model_name = sys.argv[3]
        MyFirstCrew().crew().test(n_iterations=n_iterations, openai_model_name=model_name, inputs=user_inputs)
    except IndexError:
        print("❌ Usage: python main.py test <iterations> <openai_model_name>")
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def replay():
    """
    Replay a task by ID.
    Usage: python main.py replay <task_id>
    """
    try:
        task_id = sys.argv[2]
        MyFirstCrew().crew().replay(task_id=task_id)
    except IndexError:
        print("❌ Usage: python main.py replay <task_id>")
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


# 🏁 Entrypoint
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a valid command: run | train | test | replay")
        sys.exit(1)

    command = sys.argv[1]

    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "test":
        test()
    elif command == "replay":
        replay()
    else:
        print(f"❌ Unknown command: {command}")
