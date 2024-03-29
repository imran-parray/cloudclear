import ipaddress
import argparse
import dns.resolver

parser = argparse.ArgumentParser()
parser.add_argument('--domains',help='input file conintaning domains',required=True,type=str)
args = parser.parse_args()


def readfile(file):
	words=[]
	try:
		with open(file,'r') as fh:
			for line in fh:
				words.append(line.rstrip())
	except Exception as e:
		pass
	else:
		return words



def getips(domain):
	ips=[]
	myResolver = dns.resolver.Resolver() 
	try:
		myAnswers = myResolver.query(domain, "A") 
	except Exception as e:
		return False
	else:
		for rdata in myAnswers:
			ips.append(rdata.address)
	return ips	




domains=readfile(args.domains)


ips=["103.21.244.0/22",
"103.22.200.0/22",
"103.31.4.0/22",
"104.16.0.0/12",
"108.162.192.0/18",
"111.51.66.0/24",
"116.129.226.0/25",
"116.129.226.128/26",
"118.193.97.128/25",
"118.193.97.64/26",
"119.147.182.0/25",
"119.147.182.128/26",
"120.232.236.0/25",
"120.232.236.128/26",
"120.253.240.192/26",
"120.253.241.160/27",
"120.253.245.128/26",
"120.253.245.192/27",
"120.52.12.64/26",
"120.52.153.192/26",
"120.52.22.96/27",
"120.52.39.128/27",
"130.176.0.0/16",
"131.0.72.0/22",
"13.113.196.64/26",
"13.113.203.0/24",
"13.124.199.0/24",
"13.210.67.128/26",
"13.224.0.0/14",
"13.228.69.0/24",
"13.233.177.192/26",
"13.249.0.0/16",
"13.32.0.0/15",
"13.32.0.0/15",
"13.35.0.0/16",
"13.48.32.0/24",
"13.54.63.128/26",
"13.59.250.0/26",
"141.101.64.0/18",
"143.204.0.0/16",
"144.220.0.0/16",
"15.188.184.0/24",
"15.207.13.128/25",
"162.158.0.0/15",
"172.64.0.0/13",
"173.245.48.0/20",
"180.163.57.0/25",
"180.163.57.128/26",
"18.200.212.0/23",
"18.216.170.128/25",
"18.229.220.192/26",
"188.114.96.0/20",
"190.93.240.0/20",
"197.234.240.0/22",
"198.41.128.0/17",
"204.246.164.0/22",
"204.246.168.0/22",
"204.246.172.0/24",
"204.246.173.0/24",
"204.246.174.0/23",
"204.246.176.0/20",
"205.251.192.0/19",
"205.251.200.0/21",
"205.251.208.0/20",
"205.251.249.0/24",
"205.251.250.0/23",
"205.251.252.0/23",
"205.251.254.0/24",
"210.51.40.0/24",
"216.137.32.0/19",
"223.71.11.0/27",
"223.71.71.128/25",
"223.71.71.96/27",
"3.10.17.128/25",
"3.11.53.0/24",
"3.128.93.0/24",
"3.134.215.0/24",
"3.231.2.0/25",
"3.234.232.224/27",
"3.236.169.192/26",
"3.236.48.0/23",
"34.195.252.0/24",
"34.216.51.0/25",
"34.223.12.224/27",
"34.223.80.192/26",
"34.226.14.0/24",
"34.232.163.208/29",
"35.158.136.0/24",
"35.162.63.192/26",
"35.167.191.128/26",
"36.103.232.0/25",
"36.103.232.128/26",
"44.227.178.0/24",
"44.234.108.128/25",
"44.234.90.252/30",
"52.124.128.0/17",
"52.15.127.128/26",
"52.199.127.192/26",
"52.212.248.0/26",
"52.220.191.0/26",
"52.222.128.0/17",
"52.46.0.0/18",
"52.47.139.0/24",
"52.52.191.128/26",
"52.56.127.0/25",
"52.57.254.0/24",
"52.66.194.128/26",
"52.78.247.128/26",
"52.82.128.0/19",
"52.84.0.0/15",
"54.182.0.0/16",
"54.192.0.0/16",
"54.230.0.0/16",
"54.233.255.128/26",
"54.239.128.0/18",
"54.239.192.0/19",
"54.240.128.0/18",
"58.254.138.0/25",
"58.254.138.128/26",
"64.252.128.0/18",
"64.252.64.0/18",
"65.8.0.0/16",
"65.9.0.0/17",
"65.9.128.0/18",
"70.132.0.0/18",
"71.152.0.0/17",
"99.79.169.0/24",
"99.84.0.0/16",
"99.86.0.0/16"]


def expandrange(range):
	t_list=[]
	for ip in ipaddress.IPv4Network(range):
		t_list.append(str(ip))
	return t_list



list_all=[]
done=[]
for ip in ips:
	list_all=list_all+expandrange(ip)

for domain in domains:
	r_ips=getips(domain)
	if r_ips:
		for x in r_ips:
			if x not in list_all:
				if domain not in done:
					print(domain)
					done.append(domain)
				
					

