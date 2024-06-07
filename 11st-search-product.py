import requests
import json

headers = {
    'accept': '*/*',
    'accept-language': 'en,ko-KR;q=0.9,ko;q=0.8',
    'content-type': 'application/json',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

start_product = 7189335774

def get_product_info(product):
    url = f"https://www.11st.co.kr/products/v1/pc/products/{product}/detail?redirectedOptionYn=N&trTypeCd=&trCtgrNo="
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return json.loads(response.text)


product = start_product

## loop start_products 10 times
for i in range(100000000):
    product = product + 1
    jsonDic = get_product_info(product)    
    if 'title' not in jsonDic:
        continue
    elif 'name' not in jsonDic['title']:
        continue
    title = jsonDic['title']['name']
    # contains "M4" in title
    if "M4" in title:
      print(f"{product} {title}")


# https://www.11st.co.kr/products/pa/7189337466 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 2TB (Nano-Texture 글래스) 실버 MWT23KH/A
# https://www.11st.co.kr/products/pa/7189337491 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 2TB (Nano-Texture 글래스) 스페이스블랙 MWT13KH/A
# https://www.11st.co.kr/products/pa/7189337533 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 1TB (Nano-Texture 글래스) 실버 MWT03KH/A
# https://www.11st.co.kr/products/pa/7189337565 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 1TB (Nano-Texture 글래스) 스페이스블랙 MWRY3KH/A
# https://www.11st.co.kr/products/pa/7189337597 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 2TB (Nano-Texture 글래스) 실버 MWRT3KH/A
# https://www.11st.co.kr/products/pa/7189337629 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 2TB (Nano-Texture 글래스) 스페이스블랙 MWRR3KH/A
# https://www.11st.co.kr/products/pa/7189337647 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 1TB (Nano-Texture 글래스) 실버 MWRQ3KH/A
# https://www.11st.co.kr/products/pa/7189337675 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 1TB (Nano-Texture 글래스) 스페이스블랙 MWRP3KH/A
# https://www.11st.co.kr/products/pa/7189337701 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 2TB (Nano-Texture 글래스) 실버 MWRJ3KH/A
# https://www.11st.co.kr/products/pa/7189337731 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 2TB (Nano-Texture 글래스) 스페이스 블랙 MWRH3KH/A
# https://www.11st.co.kr/products/pa/7189337760 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 1TB (Nano-Texture 글래스) 실버 MWRG3KH/A
# https://www.11st.co.kr/products/pa/7189337796 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 1TB (Nano-Texture 글래스) 스페이스 블랙 MWRF3KH/A
# https://www.11st.co.kr/products/pa/7189337825 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 2TB (Nano-Texture 글래스) 실버 MWR93KH/A
# https://www.11st.co.kr/products/pa/7189337861 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 2TB (Nano-Texture 글래스) 스페이스 블랙 MWR83KH/A
# https://www.11st.co.kr/products/pa/7189337889 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 1TB (Nano-Texture 글래스) 실버 MWR73KH/A
# https://www.11st.co.kr/products/pa/7189337920 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 1TB (Nano-Texture 글래스) 스페이스 블랙 MWR63KH/A
# https://www.11st.co.kr/products/pa/7189337946 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 2TB (스탠다드 글래스) 실버 MVY03KH/A
# https://www.11st.co.kr/products/pa/7189337976 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 2TB (스탠다드 글래스) 스페이스블랙 MVXY3KH/A
# https://www.11st.co.kr/products/pa/7189338003 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 1TB (스탠다드 글래스) 실버 MVXX3KH/A
# https://www.11st.co.kr/products/pa/7189338036 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 1TB (스탠다드 글래스) 스페이스블랙 MVXW3KH/A
# https://www.11st.co.kr/products/pa/7189338064 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 512GB 실버 MVXV3KH/A
# https://www.11st.co.kr/products/pa/7189338090 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 512GB 스페이스 블랙 MVXU3KH/A
# https://www.11st.co.kr/products/pa/7189338122 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 256GB 실버 MVXT3KH/A
# https://www.11st.co.kr/products/pa/7189338141 (1차예약) 아이패드 프로 13(M4 모델) 셀룰러 256GB 스페이스 블랙 MVXR3KH/A
# https://www.11st.co.kr/products/pa/7189338177 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 2TB (스탠다드 글래스) 실버 MVX93KH/A
# https://www.11st.co.kr/products/pa/7189338206 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 2TB (스탠다드 글래스) 스페이스 블랙 MVX83KH/A
# https://www.11st.co.kr/products/pa/7189338248 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 1TB (스탠다드 글래스) 실버 MVX73KH/A
# https://www.11st.co.kr/products/pa/7189338271 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 1TB (스탠다드 글래스) 스페이스 블랙 MVX63KH/A
# https://www.11st.co.kr/products/pa/7189338306 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 512GB 실버 MVX53KH/A
# https://www.11st.co.kr/products/pa/7189338327 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 512GB 스페이스 블랙 MVX43KH/A
# https://www.11st.co.kr/products/pa/7189338353 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 256GB 실버 MVX33KH/A
# https://www.11st.co.kr/products/pa/7189338380 (1차예약) 아이패드 프로 13(M4 모델) Wi-Fi 256GB 스페이스 블랙 MVX23KH/A
# https://www.11st.co.kr/products/pa/7189338415 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 2TB (스탠다드 글래스) 실버 MVW83KH/A
# https://www.11st.co.kr/products/pa/7189338446 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 2TB (스탠다드 글래스) 스페이스블랙 MVW73KH/A
# https://www.11st.co.kr/products/pa/7189338467 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 1TB (스탠다드 글래스) 실버 MVW63KH/A
# https://www.11st.co.kr/products/pa/7189338495 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 1TB (스탠다드 글래스) 스페이스블랙 MVW53KH/A
# https://www.11st.co.kr/products/pa/7189338521 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 512GB 실버 MVW43KH/A
# https://www.11st.co.kr/products/pa/7189338565 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 512GB 스페이스 블랙 MVW33KH/A
# https://www.11st.co.kr/products/pa/7189338599 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 256GB 실버 MVW23KH/A
# https://www.11st.co.kr/products/pa/7189338623 (1차예약) 아이패드 프로 11(M4 모델) 셀룰러 256GB 스페이스 블랙 MVW13KH/A
# https://www.11st.co.kr/products/pa/7189338650 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 2TB (스탠다드 글래스) 실버 MVVH3KH/A
# https://www.11st.co.kr/products/pa/7189338717 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 2TB (스탠다드 글래스) 스페이스 블랙 MVVG3KH/A
# https://www.11st.co.kr/products/pa/7189338753 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 1TB (스탠다드 글래스) 실버 MVVF3KH/A
# https://www.11st.co.kr/products/pa/7189338809 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 1TB (스탠다드 글래스) 스페이스 블랙 MVVE3KH/A
# https://www.11st.co.kr/products/pa/7189338854 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 512GB 실버 MVVD3KH/A
# https://www.11st.co.kr/products/pa/7189338887 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 512GB 스페이스 블랙 MVVC3KH/A
# https://www.11st.co.kr/products/pa/7189338942 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 256GB 실버 MVV93KH/A
# https://www.11st.co.kr/products/pa/7189338992 (1차예약) 아이패드 프로 11(M4 모델) Wi-Fi 256GB 스페이스 블랙 MVV83KH/A