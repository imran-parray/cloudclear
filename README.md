# Cloudclear


## Intorduction

Cloudclear is an automated tool designed to receive a list of domains as input and then identify and remove all the domains that have cloudflair and cloudfront protection.





## Why

A significant number of subdomains that operate under cloudflair and cloudfront are highly secure against various reconnaissance techniques such as directory busting, port scanning, vulnerability scanning, and more. Therefore, I tend to prioritize non-cloudflair and non-cloudfront domains initially, as they are more likely to be less secure and easier targets compared to their counterparts.




## How do it work

- It has the list of all `cloudflair` and `cloudfront` ip ranges.
- It takes the list of domains.
- Resolves them one by one.
- Matches their Ip adresses with `cloudflair` and `cloudfront` ip ranges.
- If they are matched with any of the ip in the whole range they are considered to be under `cloudflair` or `cloudfront`.

## How to use it


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

Get in touch with me on Twitter [https://twitter.com/imranparray101](https://twitter.com/imranparray101)
