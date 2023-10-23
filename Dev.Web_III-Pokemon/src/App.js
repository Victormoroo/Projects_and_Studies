import React, { useEffect, useState } from "react";
import './App.css';
import PokemonCard from "./Components/PokemonCard";

function App() {
  const [pokemonList, setPokemonList] = useState([]);
  const [filteredPokemonList, setFilteredPokemonList] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [searchTerm, setSearchTerm] = useState("");
  const [totalPages, setTotalPages] = useState(0);

  const pokemonPerPage = 25;

  useEffect(() => {
    fetch(`https://pokeapi.co/api/v2/pokemon?limit=${pokemonPerPage}&offset=${(currentPage - 1) * pokemonPerPage}`)
      .then(response => response.json())
      .then(data => {
        setPokemonList(data.results);
        setTotalPages(Math.ceil(data.count / pokemonPerPage));
      })
      .catch(error => console.error(error));
  }, [currentPage]);

  useEffect(() => {
    const searchTermLower = searchTerm.toLowerCase();
    const filtered = pokemonList.filter(pokemon =>
      pokemon.name.toLowerCase().includes(searchTermLower)
    );
    setFilteredPokemonList(filtered);
  }, [searchTerm, pokemonList]);

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  return (
    <div className="App">
      <header>
        <strong>Pokemon API</strong>
      </header>

      <input
        type="text"
        placeholder="Digite o nome do Pokémon"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <button onClick={() => setCurrentPage(1)}>Buscar</button>

      <div className="pokemon-card-container">
        {filteredPokemonList.map((pokemon, index) => (
          <PokemonCard key={index} pokemon={pokemon} />
        ))}
      </div>

      <div className="pagination">
        <button onClick={handlePreviousPage} disabled={currentPage === 1}>
          Página Anterior
        </button>
        <button onClick={handleNextPage} disabled={currentPage === totalPages}>
          Próxima Página
        </button>
      </div>
    </div>
  );
}

export default App;