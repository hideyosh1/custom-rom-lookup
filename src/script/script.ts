import phones from "../../data.json";
import "../../node_modules/popper.js/dist/popper.min.js";
import "../../node_modules/bootstrap/dist/js/bootstrap.bundle.js";

let vendor_set = new Set<string>();

for (const [key, value] of Object.entries(phones)) {
  let element = document.createElement("tr");
  element.id = key;

  element.innerHTML = `
  <th>${value.name}</th>
  <td>${value.vendor}</td>
  <td class="codename-td">${key}</td>
  <td>${value.support}</td>
  `;

  vendor_set.add(value.vendor);

  document.querySelector("tbody")?.appendChild(element);
}

for (const vendor of vendor_set) {
  let element = document.createElement("option");
  element.value = vendor;
  element.innerHTML = vendor;
  document.querySelector(".dropdown-menu")?.appendChild(element);
}

const name_search = document.querySelector("#name-search")!;
const codename_search = document.querySelector("#codename-search")!;

codename_search.addEventListener("input", (e) => {
  let val = (e.target! as HTMLInputElement).value;
  const re = new RegExp(RegExp.escape(val), "di");

  for (const phone of document
    .querySelector("tbody")!
    .querySelectorAll("tr")!) {
    if (re.test(phone.querySelector(".codename-td")!.innerHTML)) {
      phone.classList.remove("d-none");
    } else {
      phone.classList.add("d-none");
    }
  }
});
name_search.addEventListener("input", (e) => {
  let val = (e.target! as HTMLInputElement).value;
  const re = new RegExp(RegExp.escape(val), "di");

  for (const phone of document
    .querySelector("tbody")!
    .querySelectorAll("tr")!) {
    if (re.test(phone.querySelector("th")!.innerHTML)) {
      phone.classList.remove("d-none");
    } else {
      phone.classList.add("d-none");
    }
  }
});
