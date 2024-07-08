# Trip Planner AI

Trip Planner AI is an AI-driven application that helps you plan your trips by generating detailed itineraries, selecting the best cities to visit, and gathering comprehensive city information based on your interests and preferences.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python >= 3.10, < 3.13
- Poetry (for managing dependencies and virtual environments)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AnishHassan/crewai_travel_planner.git
    cd crewai_travel_planner
    ```

2. **Set up the virtual environment**:
    ```bash
    poetry shell
    ```

3. **Install dependencies**:
    ```bash
    poetry install --no-root
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory of the project and add your API keys:
    ```env
    GROQ_API_KEY=your_groq_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

## Usage

To run the project, use the following command:
```bash
python main.py

Project Structure

trip-planner-ai/
├── agents.py
├── main.py
├── pyproject.toml
├── tasks.py
├── README.md
└── tools
    ├── calculator_tools.py
    ├── search_tools.py


