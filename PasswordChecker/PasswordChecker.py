import requests,hashlib



def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError ("failed with fetching Data with error code:"+str(res.status_code))
    return res
def pwned_api_check(password):
    hashed_PW= hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    res=request_api_data(hashed_PW[:5])
    return res,hashed_PW[5:]

def Process (response,hashed_PW):
    hashes=(i.split(":") for i in response.text.splitlines())
    for element,count in hashes:

        if element==hashed_PW:
            return count
    return 0


(response,hash)=pwned_api_check("BOBOS")
print(Process(response,hash))
