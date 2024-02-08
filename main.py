# import scrapy
# import pandas as pd
# import time
#
# class LookFantasticSpider(scrapy.Spider):
#     name = "look"
#     allowed_domains = ["www.lookfantastic.com"]
#     start_urls = ['https://www.lookfantastic.com/health-beauty/face/skincare-products.list']
#
#     def parse(self, response):
#         for page_num in range(1, 100):
#             yield scrapy.Request(url=response.urljoin(f'?pageNumber={page_num}'), callback=self.parse_page)
#
#     def parse_page(self, response):
#         products = response.css('li.productListProducts_product')
#
#         for product in products:
#             product_link = product.css('a.productBlock_link::attr(href)').extract_first()
#             yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product)
#
#         time.sleep(10)
#
#     def parse_product(self, response):
#         name = response.css('h1.productName_title::text').get()
#         price = response.css('p.productPrice_price::text').get()
#         ingredients = response.css('div#product-description-content-lg-7 div div p::text').get()
#
#         data = {'Name': [name], 'Price': [price], 'Ingredients': [ingredients]}
#         self.save_to_csv(data)
#
#     def save_to_csv(self, data):
#         csv_file_path = 'products_dt.csv'
#
#         try:
#             existing_df = pd.read_csv(csv_file_path)
#         except FileNotFoundError:
#             existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients'])
#
#         updated_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
#
#         updated_df.to_csv(csv_file_path, index=False)
#         self.log(f'Data successfully written to {csv_file_path}')




import scrapy
import pandas as pd
import time

# class LookFantasticSpider(scrapy.Spider):
#     name = "look"
#     allowed_domains = ["www.lookfantastic.com"]
#     start_urls = ['https://www.lookfantastic.com/health-beauty/face/skincare-products/lip-balm.list']
#
#     def parse(self, response):
#         for page_num in range(1, 5):
#             yield scrapy.Request(url=response.urljoin(f'?pageNumber={page_num}'), callback=self.parse_page)
#
#     def parse_page(self, response):
#         products = response.css('li.productListProducts_product')
#
#         for product in products:
#             product_link = product.css('a.productBlock_link::attr(href)').extract_first()
#             yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product, meta={'product_link': product_link})
#
#         time.sleep(10)
#
#     def parse_product(self, response):
#         name = response.css('h1.productName_title::text').get()
#         price = response.css('p.productPrice_price::text').get().replace('\n',
#                                                                          '').strip()
#         ingredients = response.css('div#product-description-content-lg-7 div div p::text').get()
#         product_link = response.meta.get('product_link')
#         full_product_link = "https://www.lookfantastic.com" + product_link
#         category = "Lip Balm"
#
#         data = {'Name': name, 'Price': price, 'Ingredients': ingredients, 'Product_Link': full_product_link, 'Category': category}
#         self.save_to_csv(data)
#
#     def save_to_csv(self, data):
#         csv_file_path = 'product12.csv'
#
#         try:
#             existing_df = pd.read_csv(csv_file_path)
#         except FileNotFoundError:
#             existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients', 'Product_Link', 'Category'])
#
#         updated_df = pd.concat([existing_df, pd.DataFrame([data])], ignore_index=True)
#
#         updated_df.to_csv(csv_file_path, index=False)
#         self.log(f'Data successfully written to {csv_file_path}')


class LookFantasticSpider(scrapy.Spider):
    name = "look"
    allowed_domains = ["www.lookfantastic.com"]
    start_urls = ['https://www.lookfantastic.com/health-beauty/face/micellar-water.list?gclid=CjwKCAiA8NKtBhBtEiwAq5aX2HZ5DEuoCLu8zoq2ONNJH_wuYBgN39zlI1mZOwtnSd4VTGpeCeh-DxoC9ssQAvD_BwE&gclsrc=aw.ds']

    def parse(self, response):
        for page_num in range(1, 2):
            yield scrapy.Request(url=response.urljoin(f'?pageNumber={page_num}'), callback=self.parse_page)

    def parse_page(self, response):
        products = response.css('li.productListProducts_product')

        for product in products:
            product_link = product.css('a.productBlock_link::attr(href)').extract_first()
            yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product, meta={'product_link': product_link})

        time.sleep(10)

    def parse_product(self, response):
        name = response.css('h1.productName_title::text').get()
        price = response.css('p.productPrice_price::text').get().replace('\n', '').strip()
        ingredients = response.css('div#product-description-content-lg-7 div div p::text').get()
        product_link = response.meta.get('product_link')
        full_product_link = "https://www.lookfantastic.com" + product_link
        category = "Micellar Water"

        # Scrape rating and total number of reviews
        rating = response.xpath('//span[@class="athenaProductReviews_aggregateRatingValue"]/text()').get()
        total_reviews = response.xpath('//p[@class="athenaProductReviews_reviewCount Auto"]/text()').get()

        data = {
            'Name': name,
            'Price': price,
            'Ingredients': ingredients,
            'Product_Link': full_product_link,
            'Category': category,
            'Rating': rating,
            'Total_Reviews': total_reviews
        }
        self.save_to_csv(data)
    def save_to_csv(self, data):
        csv_file_path = 'Pro11.csv'

        try:
            existing_df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            existing_df = pd.DataFrame(
                columns=['Name', 'Price', 'Ingredients', 'Product_Link', 'Category', 'Rating', 'Total_Reviews'])

        updated_df = pd.concat([existing_df, pd.DataFrame([data])], ignore_index=True)

        updated_df.to_csv(csv_file_path, index=False)
        self.log(f'Data successfully written to {csv_file_path}')