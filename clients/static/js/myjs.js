function editMode() {
	document.getElementById('myfieldset').disabled = false;
	document.getElementById('btncancel').hidden = false;
	document.getElementById('btnsave').hidden = false;
}

function readMode() {
	document.getElementById('myfieldset').disabled = true;
	document.getElementById('btncancel').hidden = true;
	document.getElementById('btnsave').hidden = true;
}