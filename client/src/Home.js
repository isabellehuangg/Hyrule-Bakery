import SearchBar from "./SearchBar";

const Home = () => {
    return (  
        <div className="home">
            <h2 className="title">Hyrule Bakery</h2>
            <p className="description">Predict your next dessert, bookmark favorite recipes</p>
            <SearchBar />
        </div>
    );
}
 
export default Home;
