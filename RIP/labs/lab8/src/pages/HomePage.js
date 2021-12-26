import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";

function HomePage() {
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Фильмы</h2>
            <Link to="/Films"><button>К списку фильмов</button></Link>
        </div>
    );
}

export default HomePage;
