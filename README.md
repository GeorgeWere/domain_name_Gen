# domain_name_Gen.py

domain_name_Gen is a command line tool to generate email addresses from a given name and domain. It can generate email addresses in several formats based on the provided name and domain.

# Requirements
- Python 3.6 or later

# Installation

There is no need for installation. Just download or clone the script from the repository and run it using Python3.

# Usage
## Generate Email Addresses from a Single Name

To generate email addresses from a single name, run the script with the `-n` or `--name` option followed by the name and the `-d` or `--domain` option followed by the domain name. If the domain name is not provided, the script will generate email addresses without the domain.

```sh
python domain_name_Gen.py -n "John Doe" -d example.com
```

# Generate Email Addresses from a List of Names

To generate email addresses from a list of names, put the names in a text file (one name per line) and run the script with the -f or --file option followed by the path to the file and the -d or --domain option followed by the domain name. If the domain name is not provided, the script will generate email addresses without the domain.

```sh
python domain_name_Gen.py -f names.txt -d example.com
```
# Saving Generated Email Addresses to a File

To save the generated email addresses to a file, use the -o or --output option followed by the path to the file.

```sh
python domain_name_Gen.py -n "John Doe" -d example.com -o output.txt

```

# Providing Names with Spaces

If the name contains spaces, put it in quotation marks.

```sh
python domain_name_Gen.py -n "John Doe" -d example.com
```
# Examples

Here are some examples of using the domain_name_Gen script:

```sh
python domain_name_Gen.py -n "John Doe" -d example.com
```

This will generate email addresses for the name "John Doe" with the domain "example.com".

```sh
python domain_name_Gen.py -f names.txt -d example.com
```
This will generate email addresses for the names in the names.txt file with the domain "example.com".

```sh
python domain_name_Gen.py -n "John Doe" -d example.com -o output.txt
```

This will generate email addresses for the name "John Doe" with the domain "example.com" and save them to the output.txt file.

Contributing
If you find any bugs or issues with the script, please open an issue on the GitHub repository.
