let data;

fetch('data.json').then(response => {
	if (response.ok) {
		response.json().then(json => {
			data = json;
			console.log({data});
			initialise(data);
		});
	} else {
		console.log(response.status);
	}
});

function initialise(datas) {
	for (i = 0; i < data.length; i++) {
		fetchBlob(datas[i]);
	}
}

function fetchBlob(data) {
	let url = 'img/' + data.image;
	fetch(url)
		.then(res => {
			return res.blob();
		})
		.then(blob => {
			let objURL = URL.createObjectURL(blob);

			display(objURL, data);
		});
}

function display(objURL, data) {
	// query the tag
	const main = document.querySelector('main');

	// create the tag
	const section = document.createElement('section');
	const heading = document.createElement('h2');
	const para = document.createElement('p');
	const image = document.createElement('img');

	section.setAttribute('class', data?.type);

	heading.textContent = data?.name?.replace(data?.name?.charAt(0), data?.name?.charAt(0).toUpperCase());
	para.textContent = '$' + Number(data?.price).toFixed(2);

	image.src = objURL;
	image.alt = data?.name;

	// append them
	main.appendChild(section);
	main.appendChild(heading);
	main.appendChild(para);
	main.appendChild(image);
}
