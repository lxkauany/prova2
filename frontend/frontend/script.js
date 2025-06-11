function mostrarDetalhes() {
  const lista = document.getElementById('lista-destinos');
  lista.style.display = lista.style.display === 'none' ? 'block' : 'none';
}

function adicionarItem(event) {
  event.preventDefault();
  const atividade = document.getElementById('atividade').value;
  const data = document.getElementById('data').value;
  const lista = document.getElementById('lista-itinerario');

  const item = document.createElement('li');
  item.innerHTML = `${data ? data + ' - ' : ''}${atividade} <button onclick="removerItem(this)">Remover</button>`;
  lista.appendChild(item);

  document.getElementById('atividade').value = '';
  document.getElementById('data').value = '';
}

function removerItem(btn) {
  btn.parentElement.remove();
}

function buscarDestinos(event) {
  event.preventDefault();
  const filtro = document.getElementById('filtro').value.toLowerCase();
  const cards = document.querySelectorAll('.packages .card');

  cards.forEach(card => {
    if (!card.dataset.destino) return;
    const texto = card.dataset.destino;
    card.style.display = texto.includes(filtro) ? 'block' : 'none';
  });
}



