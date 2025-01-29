# Django Portfolio

Overview
This is a personal portfolio website built using Django, showcasing skills, projects, and contact information. 
The website allows users to view details about projects, download resumes, and connect via contact forms.

Features
- Home Page: Introduction and brief about me.
- Projects Section: Display of completed projects with descriptions.
- Skills Section: List of technical skills and expertise.
- Contact Form: Users can send messages directly through the website.
- Responsive Design: Works on both desktop and mobile devices.

Installation
Prerequisites
Ensure you have the following installed:
- Python (3.11 or later recommended)
- Django
- Virtual Environment (optional but recommended)

Setup
1. Clone the Repository
   ```
   git clone <repository_url>
   cd django-portfolio
   ```

2. Create and Activate a Virtual Environment (Optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run Migrations
   ```
   python manage.py migrate
   ```

5. Create a Superuser (Admin Access, Optional)
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. Run the Development Server
   ```
   python manage.py runserver
   ```

7. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

Usage
- Navigate through different sections to explore skills and projects.
- Use the contact form to send messages.
- Admins can log in to manage content through the Django admin panel.

Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Django
- **Database**: SQLite (default) or PostgreSQL/MySQL (optional)

Contribution
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and create a pull request.

License
This project is licensed under the MIT License.

Contact
For any queries or support, feel free to reach out:
- Email: sekar.gauthamraj@gmail.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourprofile)
