let products;

fetch('products.json').then(function (response) {
	if (response.ok) {
		response.json().then(function (json) {
			products = json;
			console.log({products});
			initialise(products);
		});
	} else {
		console.log(response.status);
	}
});

// function init(arr) {
// 	const main = document.querySelector('main');
// 	const heading = document.createElement('h2');
// 	const section = document.createElement('section');

// 	// Array.map((product, Index) => )
// 	const el = arr?.map((product, index) => {
// 		console.log('name', product.name);
// 		heading.textContent += product.name;
// 		main.appendChild(heading);
// 	});
// }

function initialise(products) {
	for (let i = 0; i < products.length; i++) {
		fetchBlob(products[i]);
	}
}

function fetchBlob(product) {
	let url = 'images/' + product.image;

	fetch(url)
		.then(res => {
			return res.blob();
		})
		.then(blob => {
			let objURL = URL.createObjectURL(blob);

			display(objURL, product);
		});
}

function display(objURL, product) {
	// query the tag
	const main = document.querySelector('main');

	// create the tag
	const section = document.createElement('section');
	const heading = document.createElement('h2');
	const para = document.createElement('p');
	const image = document.createElement('img');

	section.setAttribute('class', product?.type);

	heading.textContent = product?.name?.replace(product?.name?.charAt(0), product?.name?.charAt(0).toUpperCase());

	para.textContent = '$' + Number(product?.price).toFixed(2);

	image.src = objURL;
	image.alt = product?.name;

	// append them
	main.appendChild(section);
	section.appendChild(heading);
	section.appendChild(para);
	section.appendChild(image);
}
