import argparse

def generate_emails(name, domain):
    emails = []
    if " " in name:
        first_name, last_name = name.split(" ", 1)
    else:
        first_name = name
        last_name = ''
    email_parts = []
    if first_name:
        email_parts.append(first_name[0])
    if last_name:
        email_parts.append(last_name)
    email = '.'.join(email_parts)
    if domain:
        emails.append(f"{email}@{domain}")
    else:
        emails.append(email)
    if last_name:
        email = f"{first_name}.{last_name}"
        if domain:
            emails.append(f"{email}@{domain}")
        else:
            emails.append(email)
    if last_name and first_name:
        email = f"{first_name}{last_name}"
        if domain:
            emails.append(f"{email}@{domain}")
        else:
            emails.append(email)
    if first_name:
        if domain:
            emails.append(f"{first_name}@{domain}")
        else:
            emails.append(first_name)
    return emails

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate email addresses from name and domain')
    parser.add_argument('-n', '--name', help='Name (e.g. John Doe)', required=True)
    parser.add_argument('-d', '--domain', help='Domain (e.g. example.com)')
    parser.add_argument('-f', '--file', help='File containing names, one per line')
    parser.add_argument('-o', '--output', help='Output file for generated email addresses')
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            names = f.read().splitlines()
        emails = []
        for name in names:
            emails.extend(generate_emails(name, args.domain))
    else:
        name = args.name
        emails = generate_emails(name, args.domain)

    if args.output:
        with open(args.output, 'w') as f:
            f.write('\n'.join(emails))
    else:
        print('\n'.join(emails))
