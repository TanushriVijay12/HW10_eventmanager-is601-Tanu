# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

## Closed Issues and Resolutions (COULDN'T FIND THE ISSUES; BUT I HAVE COMMITTED THE CHANGES TO GITHUB)
1. **Fix Username Validation and Schema Adjustments**  
   Adjusted the user base data to include the required field `nickname` and updated tests accordingly.

2. **Improve Password Validation**  
   Updated password validation logic and test cases to ensure stronger password criteria.

3. **Resolve Profile Field Edge Cases**  
   Fixed issues with updating multiple profile fields simultaneously and added more comprehensive tests.

4. **Fix JWT Token Generation Issue**  
  Modified JWT token fixtures to include proper payload keys and adjusted the JWT service accordingly.

5. **SMTP Email Sending Fixes for Testing**  
   Added a DummySMTP class and patched SMTP calls in tests to prevent real network calls.

## Docker Image

This project uses a Docker image built from the provided Dockerfile. The image is built and tagged as:
hw10webn-fastapi:latest

You can run this image locally by executing:
docker run -p 8000:8000 hw10webn-fastapi:latest

If you need to rebuild the image, run the following command in your project root (where the Dockerfile is located):
docker build -t hw10webn-fastapi:latest .

## Reflection
I have learned a lot from working on the Event Manager API project.  I gained a lot of knowledge about utilizing FastAPI to create a secure REST API and how JWT-based authentication contributes to system security.  I also learned the importance of having a strong test suite to maintain code reliability and facilitate future improvements through testing, both manually and with automated tools.  Resolving issues with user profiles, usernames, and passwords improved my comprehension of how to create a robust API.