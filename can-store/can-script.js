let products;

fetch('products.json').then(function (response) {
	if (response.ok) {
		response.json().then(function (json) {
			products = json;
			console.log(products);
		});
	} else {
		console.log(response.status);
	}
});
