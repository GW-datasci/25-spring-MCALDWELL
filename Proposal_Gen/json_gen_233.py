#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """233""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Modeling fires in California""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal is to create a tool (dashboard most likely) which will help Californians determine what areas are most prone to fires.  
            This can help them to determine what areas are safest to build new developments, purchase real estate, or take preemptive action to defend their homes from fires.  
            It will also provide a guideline which could allow state authorities to better optimize resource allocation, as well as determine what areas of wilderness may require additional fire observation posts.  
            This will allow private users to determine what areas may be safest, and preferably, it could also be used by state authorities to help determine which areas require more resources to help prevent fires.  
            On a microlevel, individuals could use it to inform themselves on how ready they need to be in the event of a fire in the area.  
            On a macrolevel, it could allow for state fire departments to predict, or at least in some capacity, anticipate where a fire may be, and divert additional engines and air assets before the outbreak of a fire.  
            This could massively help containment, and prevent fires growing out of control.
 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            https://www.fire.ca.gov/incidents - 
            This database contains a csv and geo json fill containing all fires in California in recent years.  
            This will be the basis of the map, as it will allow us to observe temporal trends, and diagnose which areas have seen repeat fires. 
            This is regulated and published by the state, so it is likely highly reliable.

            https://www.fire.ca.gov/what-we-do/fire-resource-assessment-program/gis-mapping-and-data-analytics - 
            This database contains the rest of the data needed.  
            Including critical resources such as land type, vegetation coverage, and past fire incident and their causes.  
            Similarly, it contains key tangential data, such as administrative boundaries and cities.  
            This is regulated and published by the state, so it is likely highly reliable.

            https://data.ca.gov/ - This is a massive repository of open source data, including most importantly, utility lines and maps, which have historically caused many fires.  
            This is state regulated, despite being open source, and is likely well vetted and reliable.
  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help both agency level and private users to analyze the risk of fires in the areas, improving resource allocation, fire awareness, and emergency response.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Automate data capturing from Google Earth Engine (Python code in the engine).
            2. Work on the covariate features importance.  
            3. Use covariate features to model degree of poverty (Classical Models).
            4. Use a model developed in on city and apply it to other cities (Transfer Learning)
            5. Combine satellite images with covariate features.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (3 Weeks) Data Processing
            	- (3 Weeks) Feature Importance/Experiment with causes 
            	- (1 Weeks) Compile  
            	- (3 Weeks) Data verification  
            	- (2 Weeks) Visualization/UI creation  
            	- (2 Week) Writing up the report/Beta testing
            	- (1 Week) Poster and Final Presentation  

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 1 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is on data analysis part , find a good features and train a decent model.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Matthew Caldwell",
        "Proposed by email": "mcaldwell25@gwu.edu",
        "instructor": "Sushovan Majhi",
        "instructor_email": "s.majhi@gwu.edu",
        "github_repo": "https://github.com/GW-datasci/25-spring-MCALDWELL",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
