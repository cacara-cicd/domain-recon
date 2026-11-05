# domain-recon

Automated Domain Reconnaissance & Attack Surface Monitoring

`domain-recon` is a GitHub Actions-powered security reconnaissance tool that resolves domains and subdomains to IP addresses, discovers exposed network ports, identifies running services, and publishes browsable HTML reports directly to the repository.

The project is designed to help domain owners monitor their external attack surface, identify unnecessary exposed services, and maintain visibility into their internet-facing infrastructure.

> [!WARNING]
> **Authorization required.** Only assess domains, IP addresses, and infrastructure that you own or have explicit written permission to test. Ensure all targets are within your approved assessment scope. Follow the acceptable-use policies of your CI provider.

## Features

* **Domain resolution:** Converts domains and subdomains into IPv4 addresses.
* **Port discovery:** Uses RustScan to identify accessible TCP ports.
* **Service fingerprinting:** Uses Nmap to identify running services and software versions.
* **Automated scanning:** Runs through GitHub Actions without requiring a dedicated scanning server.
* **HTML reporting:** Converts Nmap XML output into browsable HTML reports.
* **Report archiving:** Maintains historical reports for tracking changes over time.
* **Scheduled or manual execution:** Supports manual workflow execution and automatic scans when the target list changes.
* **Extensible architecture:** Designed to support additional security assessment modules.

## How it works

The scanning pipeline follows this workflow:

```text
                 domains.txt
                      |
                      v
              Domain Normalization
                      |
                      v
                DNS Resolution
                      |
                      v
                   ips.txt
                      |
                      v
                  RustScan
               Port Discovery
                      |
                      v
                    Nmap
           Service / Version Detection
                      |
                      v
                   scan.xml
                      |
                      v
              HTML Report Generation
                      |
                      v
                 reports/
                 |       |
                 v       v
              latest   archive/
                 |
                 v
           GitHub Repository

## Repository structure

domain-recon/
│
├── .github/
│   └── workflows/
│       └── scan.yml             # GitHub Actions workflow
│
├── scripts/
│   └── resolve.py               # Domain-to-IP resolver
│
├── domains.txt                  # Target domain inventory
│
├── ips.txt                      # Generated resolved IP addresses
│
├── scan.xml                     # Generated Nmap XML output
│
├── reports/
│   ├── latest.html              # Latest scan report
│   │
│   └── archive/
│       ├── YYYY-MM-DD.html      # Historical scan reports
│       └── ...
│
├── .gitignore
│
└── README.md