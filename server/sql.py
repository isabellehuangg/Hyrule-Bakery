create_ingredients_table = """
        CREATE TABLE IF NOT EXISTS ingredients (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """

create_recipes_table = """
    CREATE TABLE IF NOT EXISTS recipes (
        id SERIAL PRIMARY KEY,
        recipe VARCHAR(255) NOT NULL,
        ingredient_1 VARCHAR(255) NOT NULL,
        ingredient_2 VARCHAR(255),
        ingredient_3 VARCHAR(255),
        ingredient_4 VARCHAR(255),
        ingredient_5 VARCHAR(255)
    )
"""