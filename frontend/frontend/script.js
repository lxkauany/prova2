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
  item.textContent = data ? {data} - {atividade} : atividade;
  lista.appendChild(item);

  document.getElementById('atividade').value = '';
  document.getElementById('data').value = '';
}

