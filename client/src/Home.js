import { useState, useEffect } from "react";

const Home = () => {
    const ingredients = ['Wheat', 'Sugar', 'Apple']; // Sample ingredients
    const [input, setInput] = useState('');
    const [autoIngredients, setAutoIngredients] = useState([]);
    const [selectedIngredients, setSelectedIngredients] = useState([]); 

    const handleInput = (e) => {
        const userInput = e.target.value.toLowerCase();
        setInput(userInput);
        const matchingIngredients = ingredients.filter((ingredient) => {
            return ingredient.toLowerCase().startsWith(userInput);
        });
        setAutoIngredients(matchingIngredients);
    };

    const chooseOne = (ingredient) => {
        setInput('');
        setAutoIngredients([]);
        setSelectedIngredients((pastIngredients) => [...pastIngredients, ingredient]);
    };

    const removeOption = (ingredientToRemove) => {
        setSelectedIngredients((pastIngredients) =>
            pastIngredients.filter((ingredient) => ingredient !== ingredientToRemove)
        );
    };

    const displaySelectedIngredients = () => {
        return selectedIngredients.map((ingredient) => (
            <div key={ingredient} className="selectedIngredient">
                {ingredient}
                <button onClick={() => removeOption(ingredient)} className="closeButton">X</button>
            </div>
        ));
    };

    return (  
        <div className="home">
            <h2 className="title">Hyrule Bakery</h2>
            <p className="description">Predict your next dessert, bookmark favorite recipes</p>
            <div className="searchBar">
                {displaySelectedIngredients()}
                <input className="search" type="text" placeholder="Search (e.g. Wheat)" value={input} onChange={handleInput} />
            </div>
            {
                // Display Ingredients as buttons under the search bar when Ingredients length < 6
                // value = {input} allows for search bar to empty when chooseOne is called
                selectedIngredients.length < 5 && (
                    <div className="optionButtons">
                        {autoIngredients.map((option) => (
                            <div key={option} className="option" onClick={() => chooseOne(option)}>
                                {option}
                            </div>
                        ))}
                    </div>
                )
            }
        </div>
    );
}
 
export default Home;
