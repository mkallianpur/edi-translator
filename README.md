This Python-based application automatically translates X12 EDI files (specifically those starting with an ISA segment) from a retailer-to-wholesaler communication format into a custom PH1 format. Designed for high-throughput environments, it supports:

Multithreading for processing large volumes of files (100+)

Retry logic and error logging

Linux/Windows compatibility

Dockerization for consistent deployment

CI/CD pipeline on Azure DevOps to build, test, and deploy on every push

EDI parsing using the bots library

Unit testing via pytest

This solution is ideal for businesses needing automated EDI workflows that are portable, testable, and production-grade.
