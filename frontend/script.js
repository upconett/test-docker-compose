function get_number() {
	promise = fetch("http://localhost:8000/number");
	promise.then(resp=>{
		resp.text().then(number=>{
			assignNumber(number)
		})
	})
}

function assignNumber(number) {
	document.getElementById("number").textContent = number;
}