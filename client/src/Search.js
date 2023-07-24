import React, { useState, useEffect } from "react";

const SearchBar = () => {
    const ingredients = ['Wheat', 'Sugar', 'Apple']; // Sample ingredients
    const [input, setInput] = useState('');
    const [autoOptions, setAutoOptions] = useState([]); // Auto options: all possible verified options in input

    // Function for onChange event, search input
    const handleOnChange = (e) => {
        const userInput = e.target.value.toLowerCase(); 
        setInput(userInput);
        const matchingIngredients = ingredients.filter((ingredient) => {
            return ingredient.toLowerCase().startsWith(userInput);
        });
        setAutoOptions(matchingIngredients);
        console.log(autoOptions.length);
    };

    // Handle choosing one of the matching ingredients (selected: ingredient from handleOnChange)
    const chooseOne = (ingredient) => {
        setInput(ingredient);
        setAutoOptions([]);
    };

    return (  
        <div className="searchComponent">
            <div className="searchBar">
                <input className="search" type="text" placeholder="Search (e.g. Sugar Cane)" onChange={ handleOnChange } />
            </div>
            {
                // Display options as buttons under search bar when autocomplete options length is greater than 0
                autoOptions.length > 0 && (
                    <div className="optionButtons">
                        {autoOptions.map((option) => (
                            <div key = { option } className="option" onClick={ () => chooseOne(option) }>{ option }</div>
                        ))}
                    </div>
                )
            }
        </div>
    );
}
 
export default SearchBar;