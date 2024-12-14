const theoryListElement = document.getElementById("theory-list");

theories.forEach(theory => {
  const theoryCard = document.createElement("div");
  theoryCard.className = "theory-card";

  theoryCard.innerHTML = `
    <img src="${theory.image}" alt="${theory.name}">
    <h2>${theory.name}</h2>
    <p>${theory.description.substring(0, 100)}...</p>
    <a href="theory.html?id=${theory.id}">Learn More</a>
  `;

  theoryListElement.appendChild(theoryCard);
});
