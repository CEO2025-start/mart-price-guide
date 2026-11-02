from datetime import datetime
import json
import os


def scrape_prices():
  # 가격 데이터 구조 정의 (실제 마트 연동 시 이 부분을 크롤링 로직으로 고도화)
  products_data = [
      {
          "name": "신라면 120g x 5개입",
          "category": "라면/스낵",
          "unit_info": "봉지면 멀티팩",
          "image_url": (
              "https://static.ssgcdn.com/item/decisions/00/00/01/"
              "1000000000100_i_1_500.jpg"
          ),
          "coupang_price": 4150,
          "emart_price": 4280,
          "traders_price": 3980,
      },
      {
          "name": "햇반 210g x 12개입",
          "category": "가공식품",
          "unit_info": "즉석밥 박스",
          "image_url": (
              "https://static.ssgcdn.com/item/decisions/00/00/01/"
              "1000000000200_i_1_500.jpg"
          ),
          "coupang_price": 13900,
          "emart_price": 14500,
          "traders_price": 12900,
      },
  ]

  output_data = {
      "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "products": products_data,
  }

  # data.json 파일로 저장
  with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

  print("가격 데이터 갱신 완료!")


if __name__ == "__main__":
  scrape_prices()
