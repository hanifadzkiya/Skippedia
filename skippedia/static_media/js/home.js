function createTableActive(angkatan,jurusan,sort,nama){
	//Function for making a table that conatain student list 
	//Input : Angkatan, jurusan, sort type, and nama
	//Output : Print Table 
	rating_list = document.getElementById("rating-list-active");
	rating_list.innerHTML = "";
	table = document.createElement("table");
	row = document.createElement("tr");
	col_no = document.createElement("th");
	col_no.textContent += "No";
	col_no.classList.add("th-no");
	col_nama = document.createElement("th");
	col_nama.textContent += "Nama";
	col_nama.classList.add("th-nama");
	col_nim = document.createElement("th");
	col_nim.textContent += "NIM";
	col_nim.classList.add("th-nim");
	col_rating = document.createElement("th");
	col_rating.textContent += "Rating";
	col_rating.classList.add("th-rating");
	row.appendChild(col_no);
	row.appendChild(col_nama);
	row.appendChild(col_nim);
	row.appendChild(col_rating);
	table.classList.add("table-list");
	table.appendChild(row);
	belum = false;
	blm = true;
	params = "";
	if(angkatan != ""){
		params = "angkatan=" + angkatan;
		blm = false;
	}
	if(jurusan != ""){
		if(blm){
			params = params + "jurusan=" + jurusan;
			blm = false;
		} else {
			params = params + "&jurusan=" + jurusan;
		}
	}
	if(blm){
		params = params + "sort=" + sort;
		blm = false;
	} else {
		params = params + "&sort=" + sort;
	}
	if(nama != ""){
		if(blm){
			params = params + "nama=" + nama;
		} else {
			params = params + "&nama=" + nama;
		}	
	}
	var Http = new XMLHttpRequest();
	var url = "http://127.0.0.1:1924/api/students?" + params;
	console.log(url);
	Http.open("GET", url);
	Http.responseType = 'text';
	Http.send();
	Http.onreadystatechange = function (e) {
		console.log(Http.responseText);
	  if (Http.responseText != "" && belum == false) {
	  	console.log("MASUK");
	  	belum = true;
	    answer = JSON.parse(Http.responseText);
	    for(i = 0;i<answer.length;i++){
			console.log(i);
			row = document.createElement("tr");
			col_no = document.createElement("td");
			col_no.textContent += (i+1).toString();
			col_no.classList.add("col-no");
			col_nama = document.createElement("td");
			col_nama.classList.add("col-nama");
			link = document.createElement("a");
			link.textContent += answer[i][1];
			att = document.createAttribute("href");
			att.value = "student/" + answer[i][2];  
			link.setAttributeNode(att);
			col_nama.appendChild(link);  
			col_nim = document.createElement("td");
			col_nim.textContent += answer[i][2];
			col_nim.classList.add("col-nim");
			col_rating = document.createElement("td");
			col_rating.textContent += answer[i][3].toString();
			col_rating.classList.add("col-rating");
			row.appendChild(col_no);
			row.appendChild(col_nama);
			row.appendChild(col_nim);
			row.appendChild(col_rating);
			table.appendChild(row);
		}
		rating_list.appendChild(table);
	  }
	};
}

function createTableSkip(angkatan,jurusan,sort,nama){
	//Function for making a table that conatain student list 
	//Input : Angkatan, jurusan, sort type, and nama
	//Output : Print Table 
	rating_list2 = document.getElementById("rating-list-skip");
	rating_list2.innerHTML = "";
	table2 = document.createElement("table");
	row2 = document.createElement("tr");
	col_no2 = document.createElement("th");
	col_no2.textContent += "No";
	col_no2.classList.add("th-no");
	col_nama2 = document.createElement("th");
	col_nama2.textContent += "Nama";
	col_nama2.classList.add("th-nama");
	col_nim2 = document.createElement("th");
	col_nim2.textContent += "NIM";
	col_nim2.classList.add("th-nim");
	col_rating2 = document.createElement("th");
	col_rating2.textContent += "Rating";
	col_rating2.classList.add("th-rating");
	row2.appendChild(col_no2);
	row2.appendChild(col_nama2);
	row2.appendChild(col_nim2);
	row2.appendChild(col_rating2);
	table2.classList.add("table-list");
	table2.appendChild(row2);
	belum2 = false;
	blm2 = true;
	params2 = "";
	if(angkatan != ""){
		params2 = "angkatan=" + angkatan;
		blm2 = false;
	}
	if(jurusan != ""){
		if(blm2){
			params2 = params2 + "jurusan=" + jurusan;
			blm2 = false;
		} else {
			params2 = params2 + "&jurusan=" + jurusan;
		}
	}
	if(blm2){
		params2 = params2 + "sort=" + sort;
		blm2 = false;
	} else {
		params2 = params2 + "&sort=" + sort;
	}
	if(nama != ""){
		if(blm2){
			params2 = params2 + "nama=" + nama;
		} else {
			params2 = params2 + "&nama=" + nama;
		}	
	}
	var Http2 = new XMLHttpRequest();
	var url2 = "http://127.0.0.1:1924/api/students?" + params2;
	console.log(url2);
	Http2.open("GET", url2);
	Http2.responseType = 'text';
	Http2.send();
	Http2.onreadystatechange = function (e) {
	  if (Http2.responseText != "" && belum2 == false) {
	  	belum2 = true;
	    answer2 = JSON.parse(Http2.responseText);
	    for(i = 0;i<answer2.length;i++){
			console.log(i);
			row2 = document.createElement("tr");
			col_no2 = document.createElement("td");
			col_no2.textContent += (i+1).toString();
			col_no2.classList.add("col-no");
			col_nama2 = document.createElement("td");
			col_nama2.classList.add("col-nama");
			link2 = document.createElement("a");
			link2.textContent += answer2[i][1];
			att2 = document.createAttribute("href");
			att2.value = "student/" + answer2[i][2];  
			link2.setAttributeNode(att2);
			col_nama2.appendChild(link2);  
			col_nim2 = document.createElement("td");
			col_nim2.textContent += answer2[i][2];
			col_nim2.classList.add("col-nim");
			col_rating2 = document.createElement("td");
			col_rating2.textContent += answer2[i][3].toString();
			col_rating2.classList.add("col-rating");
			row2.appendChild(col_no2);
			row2.appendChild(col_nama2);
			row2.appendChild(col_nim2);
			row2.appendChild(col_rating2);
			table2.appendChild(row2);
		}
		rating_list2.appendChild(table2);
	  }
	};
}

function newFilterActive(){
	//Function tu make new table given by new filter
	console.log("tes")
	angkatan = document.getElementById("angkatan");
	angkatan_value = angkatan.value;
	jurusan = document.getElementById("jurusan");
	jurusan_value = jurusan.value;
	createTableActive(angkatan_value,jurusan_value,"DESC","");	
}

function newFilterSkip(){
	//Function tu make new table given by new filter
	console.log("tes")
	angkatan = document.getElementById("angkatan2");
	angkatan_value = angkatan.value;
	jurusan = document.getElementById("jurusan2");
	jurusan_value = jurusan.value;
	createTableSkip(angkatan_value,jurusan_value,"ASC","");	
}

document.addEventListener("DOMContentLoaded", function() {
	console.log("KENAPA SIH");
   createTableActive("","","DESC","");
   createTableSkip("","","ASC","");
});
