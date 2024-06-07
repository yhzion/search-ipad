import requests
import bs4

headers = {
    'accept': '*/*',
    'accept-language': 'en,ko-KR;q=0.9,ko;q=0.8',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

start_products = 8106271463

def get_product_info(products):
    url = f"https://www.coupang.com/vp/products/{products}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

products = start_products

## write to file


## loop start_products 10 times
for i in range(1000000000000):
    products = start_products + i
    html = get_product_info(products)    
    ## parse html
    bs4Obj = bs4.BeautifulSoup(html, "html.parser")
    ## remove script block
    # print(bs4Obj.select("body")[0])
    ## .prod-description-attribute .prod-attr-item
    innerText = bs4Obj.select("body")[0].getText()
    ## innerText to upper case and contains "APPLE" or "아이패드" or "M4"
    if "APPLE" in innerText.upper() or "아이패드" in innerText.upper() or "M4" in innerText.upper():
        dom_list = bs4Obj.select(".prod-buy-header__title")
        ## innerText
        str = ""
        for dom in dom_list:
            str += dom.getText() + " "
        if str != "":
            # write to file
            f = open("coupang-search-product.txt", "w")
            f.write(f"{products} {str}\n")
            f.close()
            print(f"{products} {str}")

    
    
    

