# Pokémon Card Detection Demo

Welcome to the Pokémon Card Detection Demo! This project showcases the capabilities of our machine learning model to recognize and extract information from Pokémon cards, specifically focusing on the Base Set. 

## Project Overview

The Pokémon Card Detection Demo is a web application designed to identify and extract details from Pokémon Base Set cards. The model was initially trained on French Base Set 2 cards but can effectively recognize all Base Set cards, including those in English.

### Key Features

- **Card Detection:** Recognizes Pokémon cards from the Base Set.
- **Detail Extraction:** Extracts and displays card information, such as name, number, set, and year.
- **Language Support:** While optimized for French cards, the model can accurately detect English Base Set cards as well.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework in Python for building the server-side logic.
- **TensorFlow:** An open-source machine learning library used to develop and train the card detection model.
- **HTML/CSS/JavaScript:** Front-end technologies used to build the web interface for the application.
- **Git and Git LFS:** Version control systems for managing the project's code and large files.
- **Jinja2:** A templating engine for Python, used to render dynamic content on the web pages.

## Setup Instructions

To get started with the project, follow these steps:

### Prerequisites

- **Python 3.7+**: Ensure Python 3.7 or later is installed.
- **Virtual Environment**: Use a virtual environment to manage project dependencies.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AmmarKheder/pokemoncards.git
   cd pokemoncards

2. **Create a Virtual Environment:**
   

  python3 -m venv env
  source env/bin/activate  # On Windows, use `env\Scripts\activate`
  
3. **Install Dependencies:**

Install all the required Python packages using the requirements.txt file:

pip install -r requirements.txt

4. **Add Static Files:**

Ensure that v.gif and name.png are placed in the app/static directory.

5. **Running the Application**
Start the Flask Server:

flask run

6. **Access the Application:**

Open your web browser and navigate to http://localhost:5000 to view the demo.


