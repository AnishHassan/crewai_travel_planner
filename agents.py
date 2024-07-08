import os
from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

        self.llm_groq = ChatGroq(
            temperature=0,
            model_name="llama3-70b-8192",
            api_key=os.environ['GROQ_API_KEY']
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                """Expert in travel planning and logistics.
                I have decades of experience making travel itineraries."""
            ),
            goal=dedent(
                """Create a 7-day travel itinerary with detailed per-day plans,
                including budget, packing suggestions, and safety tips."""
            ),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.llm_groq,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                """Expert at analyzing travel data to pick ideal destinations."""
            ),
            goal=dedent(
                """Select the best cities based on weather, season, prices, and traveler interests."""
            ),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.llm_groq,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                """Knowledgeable local guide with extensive information
                about the city, its attractions, and customs."""
            ),
            goal=dedent(
                """Provide the best insights about the selected city."""
            ),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.llm_groq,
        )
