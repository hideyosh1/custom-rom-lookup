import phones from "../../data.json";
import "../../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js";
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";

for (const [key, value] of Object.entries(phones)) {
  let element = document.createElement("tr");
  element.id = key;

  element.innerHTML = `
  <th>${value.name}</th>
  <td>${value.vendor}</td>
  <td>${key}</td>
  <td>${value.support}</td>
  `;

  document.querySelector("tbody")?.appendChild(element);
}
