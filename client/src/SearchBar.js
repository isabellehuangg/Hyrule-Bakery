import { useState, useEffect } from "react";

const SearchBar = () => {
    const [ingredients, setIngredients] = useState([]);
    const [input, setInput] = useState('');
    const [autoIngredients, setAutoIngredients] = useState([]);
    const [selectedIngredients, setSelectedIngredients] = useState([]); 

    useEffect(() => {
        fetch('/ingredients').then(
            res => res.json()
        ).then(

            data => {
                setIngredients(data)
            }
        )
    }, [])

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

    const removeOption = (indexToRemove) => {
        setSelectedIngredients((pastIngredients) =>
            pastIngredients.filter((_, index) => index !== indexToRemove)
        );
    };

    const displaySelectedIngredients = () => {
        // index is provided from the map function
        return selectedIngredients.map((ingredient, index) => (
            <div key={index} className="selectedIngredient">
                {ingredient}
                <button onClick={() => removeOption(index)} className="closeButton">X</button>
            </div>
        ));
    };

    const handleEnter = (e) => {
        if (e.key === 'Enter' && autoIngredients.length > 0 && input.length > 0) {
            chooseOne(autoIngredients[0]);
        }
    }

    const placeHolder = () => {
        if (selectedIngredients.length < 5) {
            return 'Search...';
        } else {
            return '';
        }
    };

    return ( 
        <div className="search" onKeyDown={handleEnter}>
            <div className="searchBar">
                {displaySelectedIngredients()}
                {
                    selectedIngredients.length < 5 && (
                        <input className="search" type="text" placeholder={placeHolder()} value={input} onChange={handleInput} />
                    )
                }
            </div>
            {
                // Display Ingredients as buttons under the search bar when Ingredients length < 6
                // value = {input} allows for search bar to empty when chooseOne is called
                selectedIngredients.length < 5 && (
                    <div className="optionButtons">
                        {input.length > 0 && <p className="matching">Matching Ingredients: </p>}
                        {input.length > 0 && (autoIngredients.map((option) => (
                            <div key={option} className="option" onClick={() => chooseOne(option)}>
                                {option}
                            </div>
                        )))}
                    </div>
                )
            }
        </div>
     );
}
 
export default SearchBar;
