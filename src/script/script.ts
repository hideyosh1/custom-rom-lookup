import phones from "../../data.json";
import "../../node_modules/popper.js/dist/popper.min.js";
import "../../node_modules/bootstrap/dist/js/bootstrap.bundle.js";

let vendor_set = new Set<string>();
let support_set = new Set<string>();

for (const [key, value] of Object.entries(phones)) {
  let element = document.createElement("tr");
  element.id = key;

  element.innerHTML = `
  <th>${value.name}</th>
  <td class="vendor-td">${value.vendor}</td>
  <td class="codename-td">${key}</td>
  <td>${value.support}</td>
  `;

  vendor_set.add(value.vendor);

  value.support.forEach((element) => {
    support_set.add(element);
  });

  document.querySelector("tbody")?.appendChild(element);
}

for (const vendor of vendor_set) {
  let element = document.createElement("li");
  element.innerHTML = `   
<div class="dropdown-item">
  <div class="form-check ">
  <input class="form-check-input vendor-check" type="checkbox" value="" id="${vendor}-vendor" checked>
  <label class="form-check-label" for="${vendor}-vendor">
    ${vendor}
  </label>
</div>
</div>
`;
  document.querySelector("#vendor-dropdown")!.appendChild(element);
}
for (const support of support_set) {
  let element = document.createElement("li");
  element.innerHTML = `   
<div class="dropdown-item">
  <div class="form-check ">
  <input class="form-check-input support-check" type="checkbox" value="" id="${support}-support" checked>
  <label class="form-check-label" for="${support}-support">
    ${support}
  </label>
    </div>
</div>
`;
  document.querySelector("#support-dropdown")!.appendChild(element);
}
const name_search = document.querySelector(
  "#name-search input",
)! as HTMLInputElement;

const codename_search = document.querySelector(
  "#codename-search input",
)! as HTMLInputElement;

const reset = function () {
  let re = new RegExp(RegExp.escape(codename_search.value), "di");
  let visible = new Map<string, boolean>();

  for (const phone of document
    .querySelector("tbody")!
    .querySelectorAll("tr")!) {
    if (!re.test(phone.querySelector(".codename-td")!.innerHTML)) {
      visible.set(phone.id, false);
    }
  }

  re = new RegExp(RegExp.escape(name_search.value), "di");

  for (const phone of document
    .querySelector("tbody")!
    .querySelectorAll("tr")!) {
    if (!re.test(phone.querySelector("th")!.innerHTML)) {
      visible.set(phone.id, false);
    }
  }

  let enabled_vendors = new Set();
  for (const vendor of document.querySelectorAll(".vendor-check")!) {
    enabled_vendors.add(
      vendor.parentElement.querySelector("label")!.innerHTML.trim(),
    );
  }
  console.log(enabled_vendors);
  for (const phone of document.querySelector("tbody")!.querySelectorAll("tr")) {
    console.log(phone.querySelector(".vendor-td")!.innerHTML);
    if (
      !enabled_vendors.has(phone.querySelector(".vendor-td")!.innerHTML.trim())
    ) {
      visible.set(phone.id, false);
    }
  }

  for (const phone of document
    .querySelector("tbody")!
    .querySelectorAll("tr")!) {
    if (visible.get(phone.id) === false) {
      phone.classList.add("d-none");
    } else {
      phone.classList.remove("d-none");
    }
  }
};

name_search.addEventListener("input", () => reset());
codename_search.addEventListener("input", () => reset());

document.body
  .querySelectorAll(".vendor-check")
  .forEach((vendor) => vendor.addEventListener("click", () => reset()));

document.body
  .querySelectorAll(".support-check")
  .forEach((support) => support.addEventListener("click", () => reset()));
