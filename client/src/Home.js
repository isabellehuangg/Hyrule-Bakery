import { useState, useEffect } from "react";
import searchBar from "./Search";

const Home = () => {
    return (  
        <div className="home">
            <h2 className="title">Hyrule Bakery</h2>
            <p className="description">Predict your next dessert, bookmark favourite recipes</p>
            <searchBar />
        </div>
    );
}
 
export default Home;