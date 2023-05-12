from urllib.parse import urlparse, parse_qs

url = "https://vk.com/public52308489?w=wall-52308489_164"

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

group_id = parsed_url.path.split('/')[-1]
group_name = query_params.get('w', [''])[0].split('-')[-1]
group_name_parts = group_name.split('_')
if len(group_name_parts) > 1:
    group_name = group_name_parts[0]

print("Group ID:", group_id)
print("Group Name:", group_name)