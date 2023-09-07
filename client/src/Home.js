import SearchBar from "./SearchBar";
import Zelda from "./zelda.png"

const Home = () => {
    return (  
        <div className="home">
            <img src={Zelda} className="title"/>
            <p className="description">Find your next dessert to bake in TOTK!</p>
            <SearchBar />
        </div>
    );
}
 
export default Home;
