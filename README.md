# MealRecipeTracker: Python CRUD App

This project was created as a recipe management system for individuals who want to organize, calculate, and share their cooking recipes digitally. It offers a simple CRUD (Create, Read, Update, Delete) interface using Python, ideal for those who need a structured way to store and explore personal and shared recipes.

The app also includes features to estimate total cost and calories per recipe, making it useful for both home cooking and personal nutrition tracking.

# Target Users

1. **Home Cooks and Families**  
   Want to store family recipes or personal creations in one place, while calculating costs and nutrition.

2. **Beginner Food Bloggers**  
   Need a simple way to organize, find ideas and share their recipes.

3. **Python Learners / Students**  
   Use this as a real-world practice project to understand CRUD operations, input validation, and logic control.

| Feature                        | Benefit                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| 🔐 Login & Registration       | Personal accounts ensure data security and separation between users     |
| 🍳 Add & Manage Recipes       | Serves as a digital recipe book with editable and structured format      |
| 🌍 Share Recipes              | Public sharing of recipes while retaining a private copy                |
| 🔍 Filter & Search            | Easily browse recipes by category, difficulty, or favorite               |
| 💸 Cost & Calorie Tracking    | Helps users plan meals and budgets with estimated totals                 |
| 🎓 Learn CRUD in Python       | Ideal for beginners learning data management, loops, and conditions     |


## 🔧 Function Overview (CRUD)
# 🟢 Create: `create_recipe()`
**Purpose**:  
Allows logged-in users to create a new personal recipe by entering structured data via console inputs.

**What it does**:
- Asks for recipe name, duration, rating, favorite status, difficulty level, instructions, and category
- Prompts user to enter multiple ingredients with:
  - name, quantity, unit, calories per unit, and price per unit
- Validates all inputs (numbers, options, yes/no decisions)
- Optionally allows the user to share the recipe to `resep_lain` (public collection)

## 🔵 Read: `browse_recipes()`
**Purpose**:  
Enables users (login or guest) to browse, search, and filter recipes from both private and public collections.

**Key Functions**:
- `browse_recipes()`: Main navigation for exploring recipes
- `lihat_semua_resep(resep_list)`: Displays full details of all recipes in table format
- `input_kategori_untuk_browse_recipes(resep_list)`: Filter by category (main, drink, etc.)
- `input_tingkat_kesulitan_browse_recipe(resep_list)`: Filter by difficulty
- `fav(resep_list)`: Show only recipes marked as favorites
- `total_biaya_per_resep(resep_list)`: Calculates and shows total cost per recipe
- `total_kalori_per_resep(resep_list)`: Calculates and shows total calories per recipe

**What it does**:
- Provides both full views and filtered views of the recipe database
- Supports structured output with headers and formatting
- Works for both personal (`resep_ku`) and public (`resep_lain`) collections

## 🟡 Update: `update_recipes()`

**Purpose**:  
Allows users to update specific parts of an existing recipe from their private collection.

**What it does**:
- Shows list of recipes with `id_resep`
- Prompts the user to select which part of the recipe to update:
  - name, category, ingredients, instructions, time, rating, favorite, or difficulty
- Validates input types (e.g., numbers, True/False, allowed strings)
- If the recipe was previously shared, it removes the public version to preserve consistency
- Updates the field in `resep_ku` and informs the user

## 🔴 Delete: `delete_recipes()`

**Purpose**:  
Allows users to permanently remove a recipe from their private collection.

**What it does**:
- Displays full list of personal recipes
- Asks for the `id_resep` to delete
- Confirms deletion via yes/no input
- If the recipe was shared (`is_shared == True`), also removes the corresponding item from `resep_lain`
- Renumbers the remaining recipes in both lists to keep `id_resep` in sequence



## ▶️ How to Run & Use This Application

### 🔧 Requirements
- Python 3.x installed on your system  
- No external libraries required (uses only built-in Python)

---

### 🏁 How to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing the source code:
   ```bash
   cd path/to/MealRecipeTracker
3. Run the application : python3 {filename}.py



### 🧭 How to Use the Application

Once you run the program, you'll be guided through an interactive menu in your terminal.

---

#### 1. **Login or Register**

- **Login (1)**  
  Enter your username and password to access all features.

- **Register (0)**  
  Create a new account by choosing a username and password.

- If you choose not to register, you can still **browse public recipes** as a guest.

#### 2. **Main Menu (After Login)**

You will see this menu:

===Menu===
1. Create Recipe
2. Browsing Recipe
3. Update Recipe
4. Delete Recipe
5. Exit

| Option | Action                  | Description                                                                 |
|--------|-------------------------|-----------------------------------------------------------------------------|
| `1`    | Create Recipe           | Add a new recipe to your private collection                                |
| `2`    | Browse Recipes          | View all recipes, filter by category/difficulty/favorite/cost/calories     |
| `3`    | Update Recipe           | Edit part of an existing recipe (e.g., name, ingredients, rating, etc.)    |
| `4`    | Delete Recipe           | Remove a recipe from your private collection permanently                    |
| `5`    | Exit                    | Close the program                                                           |

#### 3. **Browsing Recipes**

You can browse **personal** or **public** recipes.

Browsing options include:
- View all recipes
- Filter by:
  - Category (`main`, `dessert`, `snack`, `drink`, `side`)
  - Difficulty (`easy`, `medium`, `hard`)
  - Favorites
  - Total cost per recipe
  - Total calories per recipe

> 🔒 Note: Guests can only browse public recipes. Logged-in users can manage their personal recipes.

#### 4. **Creating a Recipe**

When adding a recipe, you will be prompted to enter:
- Recipe name
- Time to prepare
- Rating (1–5)
- Favorite status (yes/no)
- Difficulty (easy, medium, hard)
- Instructions
- Category (main, dessert, etc.)
- Ingredients:
  - Name
  - Quantity
  - Unit
  - Calories per unit
  - Price per unit

You will then confirm if you want to save the recipe to your private collection.


#### 5. **Updating a Recipe**

You can update:
- Name
- Category
- Instructions
- Ingredients (you must re-enter the full list)
- Time to prepare
- Rating
- Favorite status
- Difficulty level

If the recipe was previously shared to the public, the public version will be removed to prevent inconsistency.


#### 6. **Deleting a Recipe**

- Select the ID of the recipe to delete
- Confirm your choice
- If the recipe is shared, it will be removed from the public collection as well
- The remaining recipes will be re-numbered automatically










