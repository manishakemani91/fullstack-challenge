**W&D Lead Fullstack Engineering Challenge**

Welcome to our Lead Fullstack Engineering Challenge repository. This document will guide you through the challenge. Please fork this repo before you begin, as we will evaluate the code on your fork.

**Challenge Overview:**

Design and implement a system that enables users to search for properties in the database using filters. Users should be able to log in, search for properties with filters, and view them on a map (Google Maps, Leaflet, or similar).

**Requirements:**

1. **User Authentication**:
    - Use a hardcoded basic authentication with admin/admin user/password.

2. **Database Design and Implementation**: 
    - We recommend using SQLite for the sake of simplicity, but feel free to choose another database if you have a specific preference. Justify your choice.
    - Initiate the database using the data from the provided Excel file. Automation is not necessary. 

3. **Backend Development**:
    - Develop a backend in Python to interact with the database.
    - Choose a suitable Python framework (e.g., Flask, Django, FastAPI, Falcon) and justify your choice.

4. **Frontend Development**:
    - Implement the frontend using Vue.js.
    - Once logged in, users should see the property list.
    - Each property in the list should display:
        - Full Address
        - Class Description
        - Estimated Market Value
        - Building Use
        - Building Square Feet
    - Users should be able to search for properties from the database.
        - Users should be able to search on the following values:
            - Full Address
            - Class
            - Estimated_Market_Value
            - BLDG_USE
            - BUILDING_SQ_FT
    - User should be able to see the properties on a map.
    - Each marker on the map should be clickable and show the property ID.
    - The map should be centered on the properties.
    

5. **Documentation**:
    - Provide a brief README detailing how to set up and run your application.

6. **Running / Deployment**:
    - Package the application using Docker or Docker Compose.
    - Include a `run.sh` script to simplify the running process: `docker run ...` or `docker-compose up ...`
  
7. **Bonus**:
    - **Optimization**: Propose at least one optimization that can help the application perform better under increased data loads.
    - **Additional Feature**: Propose a feature you believe would enhance the user's experience while searching for properties.

## Solution
Here is a brief description of my solution and approach to solving the problem. [Link](https://github.com/manishakemani91/fullstack-challenge/tree/master/property-mapper-mvp)