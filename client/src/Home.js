import SearchBar from "./SearchBar";
import Zelda from "./zelda.png"

const Home = () => {
    return (  
        <div className="home">
            <img src={Zelda} className="title"/>
            <p className="description">Predict your next dessert, bookmark favorite recipes</p>
            <SearchBar />
        </div>
    );
}
 
export default Home;
