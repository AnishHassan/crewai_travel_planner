import os
from textwrap import dedent
from dotenv import load_dotenv
from crewai import Crew
from agents import TravelAgents
from tasks import TravelTasks

load_dotenv()

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )

        crew = Crew(
            agents=[
                expert_travel_agent,
                city_selection_expert,
                local_tour_guide
            ],
            tasks=[
                plan_itinerary,
                identify_city,
                gather_city_info
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result

def get_user_input(prompt):
    print(f"\n{prompt}\n{'-'*50}")
    return input("> ").strip()

if __name__ == "__main__":
    print("🚩🚩 Welcome to Trip Planner Crew 🚩🚩")
    print("################################\n")

    origin = get_user_input(dedent("""
        🚩 From where will you be traveling?
    """))
    cities = get_user_input(dedent("""
        🚩  What cities are you interested in visiting?
    """))
    date_range = get_user_input(dedent("""
        📅 What is the date range you are interested in traveling?
    """))
    interests = get_user_input(dedent("""
        🚩 What are some of your high-level interests and hobbies?
        (Please separate multiple interests with commas)
    """))

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()

    print("\n\n########################")
    print("🚩🚩 Here is your Trip Plan by CREWBOT 🚩🚩")
    print("########################\n")
    print(result)
