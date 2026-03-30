from urllib.parse import urlparse, parse_qs

def extract_video_id(url:str):

    parsed_url = urlparse(url)

    domain = parsed_url.netloc
    query_params = parsed_url.query


    if "youtube.com" in domain:
        query_dict = parse_qs(query_params)
        return query_dict.get("v", [None])[0]
    
    elif "youtu.be" in domain:
        # Short URLs: youtu.be/<video_id>
        return parsed_url.path.lstrip("/")
    else:
        return None