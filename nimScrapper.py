import requests
from lxml import html


# Set session requests
session_requests = requests.session()

# set login url
login_url = "https://login.itb.ac.id/cas/login?service=https%3A%2F%2Fnic.itb.ac.id%2Fmanajemen-akun%2Fpengecekan-user"

result = session_requests.get(login_url)

# get tree
tree = html.fromstring(result.text)

# Get auth tokens
lt_token = list(set(tree.xpath("//input[@name='lt']/@value")))
execution_token = list(set(tree.xpath("//input[@name='execution']/@value")))
payload = {

	"username" :"hanifadzkiya",
	"password" : "Kitaindonesia24",
	"lt" : lt_token[0],
	"execution" : execution_token[0],
	"_eventId" : "submit"
}


result = session_requests.post(
	login_url,
	data=payload,
	headers=dict(referer=login_url)
)

# get main NIC url
nic_url = 'https://nic.itb.ac.id/manajemen-akun/pengecekan-user'

# send request for UID
nimList = ["%03d" % x for x in range(1,56)]
for nim in nimList :
	payload = {
		'uid' : '18214' + str(nim)
	}

	result = session_requests.post(
		nic_url,
		data=payload,
		headers=dict(referer=nic_url)
	)



	tree = html.fromstring(result.text)
	# Get name
	Name = set(tree.xpath('//table/child::tr[position()=3]/child::td[position()=3]/text()'))
	print(nim)
	data = {
		'nim' : '18214' + str(nim),
		'nama' : Name,
		'email' : '18214' + str(nim) + '@std.stei.itb.ac.id',
		'jurusan' : 'STI',
		'angkatan' : 2014
	}
	r = requests.post(url = 'http://localhost:8000/student', data = data) 
	print(r)