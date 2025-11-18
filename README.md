🍽️ FoodBox: User-Owned Item Listing Platform (Django)

This project is a foundational web application built with Django, designed to demonstrate a grasp of core Django principles, including user authentication, CRUD operations, database relationships, and the use of Class-Based Views (CBVs) and Function-Based Views (FBVs).

The application allows authenticated users to list their food items (like a simple digital menu or marketplace), view items created by others, and manage their own listings.

✨ Key Features Implemented

1. Robust User Management

Custom Registration: Implements a custom registration form (users/forms.py) to handle user sign-up.

Authentication: Utilizes Django's built-in LoginView and LogoutView for secure session management.

User Profiles (Profile Model):

A One-to-One relationship (OneToOneField) is established between the core Django User model and a custom Profile model (users/models.py).

Uses Signals (users/signals.py) to automatically create a corresponding Profile instance whenever a new User is registered, ensuring data integrity.

Includes an ImageField in the profile for handling user avatars.

2. Food Item Management (Items Model)

Model Relationships: The Items model maintains a Foreign Key relationship (ForeignKey) with the User model, ensuring every listed food item is explicitly linked to its creator.

CRUD Operations: Full Create, Read, Update, and Delete functionality is implemented for food items:

Create: Uses a Class-Based View (CreateView) which automatically assigns the currently logged-in user as the item creator (form.instance.user_name = self.request.user).

Read (List): Uses a Class-Based View (ListView) to display all food items on the index page.

Read (Detail): Uses a Class-Based View (DetailView) to show detailed information for a single item.

Update & Delete: Implemented using Function-Based Views (update_item, delete_item), demonstrating proficiency in both view styles.

3. Frontend & Template Design

Template Inheritance: The application uses base.html for consistent navigation and structure across all pages.

Bootstrap 5: Styled using Bootstrap 5 for a clean, responsive, and modern interface.

Messages Framework: Implements the Django Messages framework to display user feedback (e.g., successful registration messages) in a visually appealing way.

🛠️ Concepts Demonstrated

This project showcases competence in the following fundamental Django areas:

Models: Defining fields, relationships (ForeignKey, OneToOneField), and model methods (get_absolute_url).

Views: Effective mixture of Class-Based Views (CBVs) and Function-Based Views (FBVs).

Forms: Creating and handling ModelForm instances for data persistence, and custom forms (RegisterForm) extending built-in forms.

URLs: Using path() and include() for clean application routing and defining the app_name namespace.

Signals: Implementing database signals (post_save) for automatic, detached business logic (profile creation).

Media Handling: Configuration of MEDIA_ROOT and MEDIA_URL to serve user-uploaded content (profile pictures).
