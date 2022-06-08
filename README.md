# NUAR
Network Utility for Active Recon

## Description
A very basic network utility for active recon in LAN, the recipe it's simple: an arp-scan sauce with a pinch of portscan and a squeeze of os-guessing full of doubt.
The recipe leaves something to be desired but the result it's edible.

## Why?
The code born as **educational purpose** only.
Data extraction in csv for later use because i'm mad.

<sup>_Don't judge me._</sup>

## Usage
It's simple, but it could be more, like NOT existing.

    L.             :
    EW:        ,ft Ef                  j.
    E##;       t#E E#t              .. EW,
    E###t      t#E E#t             ;W, E##j
    E#fE#f     t#E E#t            j##, E###D.
    E#t D#G    t#E E#t fi        G###, E#jG#W;
    E#t  f#E.  t#E E#t L#j     :E####, E#t t##f
    E#t   t#K: t#E E#t L#L    ;W#DG##, E#t  :K#E:
    E#t    ;#W,t#E E#tf#E:   j###DW##, E#KDDDD###i
    E#t     :K#D#E E###f    G##i,,G##, E#f,t#Wi,,,
    E#t      .E##E E#K,   :K#K:   L##, E#t  ;#W:
    ..         G#E EL    ;##D.    L##, DWi   ,KK:
                fE :     ,,,      .,,
                ,                       @brmk

    Network Utility for Active Recon

    usage: nuar.py [-h] -n NETWORK -i INTERFACE -o OUTPUT [-p portlist] [-name] [-os] [-pnd] [-in input_file]

    A simple-network-recon tool that enumerates endpoints and define open-ports, for now.

    optional arguments:
    -h, --help                                     - show this help message and exit
    -n NETWORK, --network NETWORK                  - choose a network IP/MASK
    -i INTERFACE, --interface INTERFACE            - interface used for network recon
    -o output_file, --output output_file           - define an output file .csv
    -name,                                         - allow hostname detection [only win*]
    -os                                            - try to guess remote operating system
    -p PORTSCAN, --portscan PORTSCAN               - define a port list to perform a scan ex: 53,88,80,8080
    -pnd, --paranoid                               - use a random sleeping time for each packet sent
    -in input_file , --input input_file            - import a csv file in nuar.py format

## Example

Simple endpoint enumeration in LAN:
```
nuar.py -n 10.100.0.0/16 -i eth1 -o inventory.csv
```

Portscan, hostname detection and os-guessing:
```
nuar.py -n 10.100.0.0/16 -i eth1 -o inventory.csv -p 80,443,8080,445,139,135 -os -name
```

Add only newest endpoint on LAN:
```
nuar.py -n 10.100.0.0/16 -i eth1 -o inventory.csv -in alredy_identified.csv
```

## Requirements
Yes, you need something.

    pip3 install scapy

<sub><sup><sub><sup>OR SOMEONE GOOD, VERY GOOD.</sup></sub></sup></sub>

## REFERENCES

[Scapy](https://scapy.net/)

[NetBIOS Over TCP/IP](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v%3dtechnet.10))

[inbtscan](https://github.com/iiilin/inbtscan) -> inspiration for retrieving hostname from Windows OS