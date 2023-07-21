import { useState } from "react";

const Home = () => {
    // Initialized dynamic ingredient tracker 
    const [ingredients, setIngredients] = useState(0);

    return (  
        <div className="home">
            <h2 className="title">Hyrule Bakery</h2>
            <p className="description">Predict your next dessert</p>
            <input className="search" type="text" placeholder="Search (e.g. Sugar Cane)" />
            <button className="submit">Submit</button>
        </div>
    );
}
 
export default Home;