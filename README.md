# cloudclear


![xxx](https://raw.githubusercontent.com/imran-parray/bugbounty_files/master/qqq.png)

## Intorduction

Cloudclear is an automation tool which takes a list domains as input and filters out all the domain which are protected under cloudflair and cloudfront.


## Why

Most of the subdomains running under cloudflair and cloudfront are completely protective against any most of recon techniques like dir busting, Port scanning, Vulneribility scanning etc. So i most prefer to focus on non cloudflair and non cloudfront domains at the beginning as they are more likely to be easy targets than others.

## How do it work

- It has the list of all `cloudflair` and `cloudfront` ip ranges.
- It takes the list of domains.
- Resolves them one by one.
- Matches their Ip adresses with `cloudflair` and `cloudfront` ip ranges.
- If they are matched with any of the ip in the whole range they are considered to be under `cloudflair` or `cloudfront`.

## How to use it

__Help__

```console
python3 script.py -h
```
```
usage: script.py [-h] --domains DOMAINS

optional arguments:
  -h, --help         show this help message and exit
  --domains DOMAINS  input file conintaning domains

```

__Scanning the list of domains__
```console
python3 script.py --domains domains.txt 
```
> this will print the list of domains which are not running under cloudflair or cloudfront.
```
1password.example.tf
airflow.dops.example.tf
atlantis.security.example.tf
```

---

Fallow me on Twitter [https://twitter.com/imranparray101](https://twitter.com/imranparray101)
