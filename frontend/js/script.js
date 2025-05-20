const destino = {
    "paris": {
        nome: "Paris, França",
        pontos: ["Torre Eiffel", "Museu do Louvre", "Catedral de Notre-Dame"],
        hoteis: ["Hotel le Meurice", "Hotel Ritz Paris"],
        atividades: ["Passeio pelo Rio Sena", "Tour Gastronômico"]
    },
    "tokyo": {
        nome: "Tóquio, Japão",
        pontos: ["Templo Senso-ji", "Shibuya Crossing", "Torre de Tóquio"],
        hoteis: ["Hotel Park Hyatt", "Mandarin Oriental Tokyo"],
        atividades: ["Comida de rua", "Visita a Akihabara"]
    }
};

function buscardestino() {
    const input = document.getElementById('inputProcura').value.toLowerCase();
    const infoDiv = document.getElementById('infoDestino');

    if (destino[input]) {
        const d = destino[input];
        infoDiv.innerHTML = `
            <h3>${d.nome}</h3>
            <p><strong>Pontos turísticos:</strong> ${d.pontos.join(", ")}</p>
            <p><strong>Acomodações:</strong> ${d.hoteis.join(", ")}</p>
            <p><strong>Atividades:</strong> ${d.atividades.join(", ")}</p>
        `;
    } else {
        infoDiv.innerHTML = `<p>Destino não encontrado.</p>`;
    }
}


