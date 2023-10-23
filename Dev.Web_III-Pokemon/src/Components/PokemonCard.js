import React, { useState, useEffect } from "react";
import './PokemonCard.css';

function PokemonCard({ pokemon }) {
  const [details, setDetails] = useState(null);

  useEffect(() => {
    if (!pokemon) {
      return;
    }

    fetch(pokemon.url)
      .then(response => response.json())
      .then(data => {
        setDetails(data);
      })
      .catch(error => console.error(error));
  }, [pokemon]);

  if (!pokemon) {
    return null;
  }

  return (
    <div className="pokemon-card">
      {details && (
        <>
          <img src={details.sprites.front_default} alt={details.name} />
          <div className="pokemon-info">
            <div className="pokemon-name">{details.name}</div>
            <div>Número: {details.id}</div>
            <div>Peso: {details.weight / 10}kg</div>
            <div>Altura: {details.height / 10}m</div>
            <div>Tipo(s): {details.types.map(type => type.type.name).join(', ')}</div>
          </div>
        </>
      )}
    </div>
  );
}

export default PokemonCard;