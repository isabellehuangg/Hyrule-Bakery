const searchBar = () => {
    const ingredients = ['Wheat', 'Sugar', 'Apple'];
    const [input, setInput] = useState('');
    const [autoOptions, setAutoOptions] = useState([]); // Auto options: all possible verified options in input

    // Function for onChange event
    const handleOnChange = (e) => {
        const userInput = e.target.trim().toLowerCase(); 
        setInput(userInput);
        const matchingIngredients = ingredients.filter((ingredient) => {
            ingredient.startsWith(userInput);
        });
        setAutoOptions(matchingIngredients);
    };

    // Handle choosing one of the matching ingredients (selected: ingredient from handleOnChange)
    const chooseOne = (ingredient) => {
        setInput(ingredient);
        setAutoOptions([]);
    };

    return (  
        <input className="search" type="text" placeholder="Search (e.g. Sugar Cane)" />
    );
}
 
export default searchBar;