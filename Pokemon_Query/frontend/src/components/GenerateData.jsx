import { useState } from "react";

const GenerateData = ({ refreshPokemons }) => {
    const [query, setQuery] = useState("https://pokeapi.co/api/v2/pokemon/");

    const createData = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch("http://127.0.0.1:5000/create", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify( {query} ),
        });
        const data = await response.json();
        let output;
        if (typeof data.data == "string") {
            output = data.data 
        } else {
            output = JSON.stringify(data, null, 2);
        }
        alert(output);
        refreshPokemons();
        } catch (err) {
            console.log("Error")
        }       
    }

    return (
        <div style={{ display: "flex", gap: "10px", alignItems: "center", justifyContent: "center" , marginTop:"40px"}}>
            <input
                type="text"
                value={query}
                placeholder="https://pokeapi.co/api/v2/pokemon/"
                onChange={(e) => setQuery(e.target.value)}
                style={{ width: "400px",     
                    padding: "10px",
                    fontSize: "16px",
                    border: "1px solid #ccc",
                    borderRadius: "5px"}}
            />
            <button onClick={createData} type="button">Generate Data</button>
        </div>
    )
}

export default GenerateData