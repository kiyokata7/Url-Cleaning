lastDomain = set()

print("......Working")

with open('url.txt', 'r', errors='ignore') as file:
    urls = file.readlines()
    total = len(urls)
    valid_urls = []

    print(f"Total Links: {total}")

    for url in urls:
        if '?' in url and '=' in url and url.startswith('http') and ".kr" not in url:
            try:
                current_domain = url.split('/')[2].strip()

                if current_domain in lastDomain:
                    continue  # Skip saving to output file
                else:
                    lastDomain.add(current_domain)

                    with open("valid.txt", 'a') as output_file:
                        output_file.write(url)

                    valid_urls.append(url)

            except IndexError:
                continue

    total_valid = len(valid_urls)
    print(f"Valid Links: {total_valid}")

input("Finished......")
