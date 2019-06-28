function createTable(angkatan,jurusan,sort,nama){
	//Function for making a table that conatain student list 
	//Input : Angkatan, jurusan, sort type, and nama
	//Output : Print Table 
	rating_list = document.getElementById("rating-list");
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
	  if (Http.responseText != "" && belum == false) {
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

function newFilter(){
	//Function tu make new table given by new filter
	angkatan = document.getElementById("angkatan");
	angkatan_value = angkatan.value;
	jurusan = document.getElementById("jurusan");
	jurusan_value = jurusan.value;
	sort = document.getElementById("sort");
	sort_value = sort.value;
	nama = document.getElementById("nama");
	nama_value = nama.value;
	createTable(angkatan_value,jurusan_value,sort_value,nama_value);	
}

document.addEventListener("DOMContentLoaded", function() {
	console.log("TES")
   createTable("","","DESC","");
});
